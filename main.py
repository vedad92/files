__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from importlib.resources import path
import os
import shutil

def clean_cache():
    path = os.path.join(os.getcwd(), 'cache')
    if os.path.isdir(path) is True:
        print("Folder already exists")
    else:
        print("Folder created")
        os.makedirs("cache")
    return
clean_cache()

def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, cache_dir)
    return

cache_zip(os.path.join(os.getcwd(), 'files', 'data.zip'), os.path.join(os.getcwd(), 'cache'))


def cached_files():
    path = os.path.join(os.getcwd(), 'cache')
    files = [os.path.join(path, f) for f in os.listdir(path)]
    return files
print(cached_files())


def find_password(file_list):
    for file in file_list:
        with open(file, "r") as f:
            contents = f.readlines()
            for text in contents:
                if "password" in text:
                    return text
    return 'Password not found'

print(find_password(cached_files()))
