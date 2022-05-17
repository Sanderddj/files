__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os.path
import os
from zipfile import ZipFile


path_cache = os.getcwd()+'\\files'
def clean_cache():
    path = path_cache
    if os.path.isdir('files\cache'):
        for file in os.scandir(path+'\cache'):
            os.remove(file.path)
        #print('aanwezig')
    else:
        #print('niet aanwezig')
        os.mkdir('files\cache')
    return

def cache_zip(path_zip,path_cache1):
    clean_cache()
    with ZipFile(path_zip, 'r') as zipObj:
        zipObj.extractall(path_cache1)
    #print('File is unzipped in cache folder') 

a = os.getcwd()+'\\files\\data.zip'
b = os.getcwd()+'\\files\\cache'
#cache_zip(a,b)
def cached_files():
    mypath = os.getcwd()+'\\files\\cache'
    path = os.path.abspath(mypath)
    list_dirs = [entry.path for entry in os.scandir(path) if entry.is_file()]
    #print(list_dirs)
    return list_dirs

cached_files()
list_dirs = cached_files()

def find_password(list_dirs):
    for files in list_dirs:
        with open(files, "r") as f:
            for line in f:
                if 'password' in line:
                    print(line)
                    password = line[line.find(' ')+1:-1]
                    print(password)
                    return(password)
find_password(list_dirs)