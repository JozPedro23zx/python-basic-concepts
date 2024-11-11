import os
import shutil
import zipfile
from PIL import Image


def compress(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if(ext == ".txt"):
        return compress_text(file_path)
    if(ext == ".png" or ext == ".jpeg"):
        return compress_image(file_path)
    else:
        raise Exception("Unsuported file")

def compress_text(file_path):
    with zipfile.ZipFile(file_path + '.zip', 'w') as zipf:
        zipf.write(file_path, compresslevel=9)
        return f'{file_path}.zip'
    
def compress_image(file_path):
    copy = shutil.copy(file_path, ".")
    img = Image.open(copy)
    img.save(file_path, quality=75)
    return copy