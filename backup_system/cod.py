import os
import glob
import argparse
import sys
import re
import zipfile
import logging
import time
from datetime import datetime
from decimal import Decimal
from collections import defaultdict
import threading

# Configuração de logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def parse_arguments():
#     parser = argparse.ArgumentParser(description='Script de Backup e Relatórios de Arquivos')
#     parser.add_argument('source', type=str, help='Diretório de origem')
#     parser.add_argument('destination', type=str, help='Diretório de destino')
#     parser.add_argument('--pattern', type=str, default='*', help='Padrão de arquivos a serem copiados (ex: *.txt)')
#     return parser.parse_args()

def copy_and_compress_files(source, destination, pattern):
    files_to_backup = glob.glob(os.path.join(source, pattern))
    report = defaultdict(list)
    total_size_before = Decimal(0)
    total_size_after = Decimal(0)

    for file in files_to_backup:
        try:
            file_size = Decimal(os.path.getsize(file))
            total_size_before += file_size
            
            # Copiando o arquivo
            dest_file_path = os.path.join(destination, os.path.basename(file))
            with open(file, 'rb') as fsrc, open(dest_file_path, 'wb') as fdst:
                fdst.write(fsrc.read())
            report['copied'].append(file)

            # Comprimindo o arquivo
            with zipfile.ZipFile(dest_file_path + '.zip', 'w') as zipf:
                zipf.write(dest_file_path, os.path.basename(dest_file_path))
                os.remove(dest_file_path)  # Remove arquivo original após compressão
            report['compressed'].append(dest_file_path + '.zip')
            total_size_after += Decimal(os.path.getsize(dest_file_path + '.zip'))

        except Exception as e:
            logging.error(f'Erro ao processar {file}: {e}')
            report['errors'].append(str(e))

    return report, total_size_before, total_size_after

def generate_report(report, total_size_before, total_size_after):
    with open('backup_report.txt', 'w') as report_file:
        report_file.write("Relatório de Backup\n")
        report_file.write("====================\n")
        report_file.write(f"Arquivos Copiados: {len(report['copied'])}\n")
        report_file.write(f"Arquivos Comprimidos: {len(report['compressed'])}\n")
        report_file.write(f"Erros: {len(report['errors'])}\n")
        report_file.write("\nArquivos Copiados:\n")
        for file in report['copied']:
            report_file.write(f"- {file}\n")
        report_file.write("\nArquivos Comprimidos:\n")
        for file in report['compressed']:
            report_file.write(f"- {file}\n")
        report_file.write("\nErros:\n")
        for error in report['errors']:
            report_file.write(f"- {error}\n")
        space_saved = total_size_before - total_size_after
        report_file.write(f"\nEspaço Economizado: {space_saved} bytes\n")

def backup_thread(source="outros", destination="backup", pattern="*"):
    report, total_size_before, total_size_after = copy_and_compress_files(source, destination, pattern)
    generate_report(report, total_size_before, total_size_after)

if __name__ == "__main__":
    start_time = time.time()
    
    # args = parse_arguments()
    
    # if not os.path.isdir(args.source):
    #     logging.error(f'Diretório de origem inválido: {args.source}')
    #     sys.exit(1)
    
    # if not os.path.isdir(args.destination):
    #     logging.error(f'Diretório de destino inválido: {args.destination}')
    #     sys.exit(1)

    thread = threading.Thread(target=backup_thread)
    thread.start()
    thread.join()  # Aguarda a conclusão da thread

    elapsed_time = time.time() - start_time
    logging.info(f'Backup concluído em {elapsed_time:.2f} segundos')