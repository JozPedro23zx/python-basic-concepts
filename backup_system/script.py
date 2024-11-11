import time
import files_management

import logging
import argparse
import os
import datetime

logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Script of Backup and File Reports')
    parser.add_argument('--source', default='', type=str, help='Origin directory')
    parser.add_argument('--destination', default='', type=str, help='Destiny directory')
    parser.add_argument('--type', type=str, default='', help='The file type (img, text or both)')
    return parser.parse_args()

def generate_report(report):
    date = datetime.datetime.now()
    date_formated = date.strftime("%Y-%m-%d %H:%M:%S")
    with open('backup_report.txt', 'w') as report_file:
        report_file.write(f"Backup Report - {date_formated}\n")
        report_file.write("====================\n")
        report_file.write(f"Compressed files: {len(report['compressed'])}\n")
        report_file.write(f"Erros: {len(report['errors'])}\n")
        report_file.write("\nCompressed files:\n")
        for file in report['compressed']:
            report_file.write(f"- {file}\n")
        report_file.write("\nErros:\n")
        for error in report['errors']:
            report_file.write(f"- {error}\n")
        report_file.write(f"\nSpace saved: {report['space_saved']} bytes\n")

if __name__ == "__main__":
    start_time = time.time()

    default_files_directory = ('files')
    default_backup_directory = ('backup')

    args = parse_arguments()

    files_directory = args.source if os.path.isdir(args.source) else default_files_directory
    backup_directory = args.destination if os.path.isdir(args.destination) else default_backup_directory
    file_types = args.type

    name_list = files_management.get_files(file_types, files_directory)
    report = files_management.copy_files(name_list, backup_directory)
    generate_report(report)

    elapsed_time = time.time() - start_time
    logging.info(f'Success backup in {elapsed_time:.2f} seconds')