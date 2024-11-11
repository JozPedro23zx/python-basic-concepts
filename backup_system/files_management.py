import compress_files

import sys
import os
import shutil
import glob
import logging

from decimal import Decimal
from collections import defaultdict

iamge_format = ['*.png', '*.jpeg', '*.jpg', '*.svg']
text_format = ['*txt']

def get_files(file_types, files_directory):
    match file_types:
        case "img":
            return define_format(iamge_format, files_directory)
        case "text":
            return define_format(text_format, files_directory)
        case "both":
            return define_format((iamge_format + text_format), files_directory)
        case "" | "*":
            return define_format("*", files_directory)
        case _:
            sys.stderr.write("==== Invalid format ==== \n")

def define_format(extension_list, files_directory):
    return [f for ext in extension_list for f in glob.glob(os.path.join(files_directory, ext))]

def copy_files(files_list, backup_directory):
    report = defaultdict(list)
    size_before = 0
    size_after = 0
    for file_path in files_list:
        try:
            file_compressed = compress_files.compress(file_path)

            size_before += Decimal(os.path.getsize(file_path))
            size_after += Decimal(os.path.getsize(file_compressed))

            shutil.copy(file_compressed, backup_directory)
            os.remove(file_compressed)
            report['compressed'].append(file_compressed)
        except Exception as e:
            logging.error(f'Error to process file {os.path.basename(file_path)}: {e}')
            report['errors'].append(str(e))
    report['space_saved'].append(size_before - size_after)
    return report
