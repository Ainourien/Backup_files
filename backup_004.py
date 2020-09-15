import os
from pathlib import Path
import shutil
import hashlib
import re
from shutil import copy
import datetime

cwd = Path(__file__).parents[0]
os.chdir(cwd)

# В файле записан путь откуда копировать. Получаем его и помещаем в массив:
with open("..\\source_pathes.txt") as f: 
    src_value = list(f)

src_folder = []
for i in range(len(src_value)):
    a = re.sub('\n', '', src_value[i]) # Убирает символ переноса строки (\n) в конце каждого элемента списка
    src_folder.append(a)

# В файле записан путь куда копировать. Получаем его и помещаем в массив:
with open("..\\destination_pathes.txt") as f:
    dest_value = list(f)
    
dest_folder = []
for i in range(len(dest_value)):
    a = re.sub('\n', '', dest_value[i]) # Убирает символ переноса строки (\n) в конце каждого элемента списка
    dest_folder.append(a)

list_of_dest_folders = []
list_of_src_files = []
list_of_dest_files = []

# Надо как-то сгруппировать эти две последующие функции в одну.
# Они используют os.walk, чтобы обойти все папки по указанному пути и создают два списка:
# Список файлов и список папок.
def file_and_path(path):
    list_of_files = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            list_of_files.append(os.path.join(root, name))      
    return list_of_files

def folders_and_path(path):
    list_of_folders = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            list_of_folders.append(os.path.join(root, name))      
    return list_of_folders

list_of_src_files = file_and_path(src_folder[0])
list_of_dest_files = file_and_path(dest_folder[0])

list_of_dest_folders = folders_and_path(src_folder[0])

# Создаем дерево подпапок, которое содержится по указанному в файле пути. Если какая-то папка уже существует, то пропускаем её.
# Сделать это отдельно нужно потому что функция copy из библиотеки shutil сама все директории по пути файла не создаёт.
for i in range(len(list_of_dest_folders)):
    os.makedirs(list_of_dest_folders[i].replace(src_folder[0], dest_folder[0]), exist_ok=True)

# Функция для получения хэш-суммы файла:
# В главном цикле (ниже) будет условие, что копировать файлы нужно только, если хэш-сумма не совпадает.
def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

'''print(re.split('\\\\', list_of_src_files[3])[-1])''' # Разделяем строку с путь+имя файла по слэшам \ и выбираем последний элемент массива, чтобы получить имя файла

#a = list_of_src_files[3].replace(src_folder[0], dest_folder[0])
#print(a)
list_of_new_dest_files = []
for i in range(len(list_of_src_files)):
    list_of_new_dest_files.append(list_of_src_files[i].replace(src_folder[0], dest_folder[0]))
    if os.path.isfile(list_of_new_dest_files[i]):  # Проверяем, существует ли в целевой директории соответствующий файл. Если нет, то копируем.
        if re.split('\\\\', list_of_new_dest_files[i])[-1] == re.split('\\\\', list_of_src_files[i])[-1]: # Проверяем, совпадают ли имена файлов. Если да, то 
            if get_hash_md5(list_of_new_dest_files[i]) != get_hash_md5(list_of_src_files[i]): # проверяем, совпадает ли хэш-сумма. Если нет, то копируем, если да, то ничего не делаем в этом цикле.
                    copy(list_of_src_files[i], list_of_new_dest_files[i])
                    print('duplicated ' + list_of_src_files[i] + ' at ' + str(datetime.datetime.now()))
    else: 
        copy(list_of_src_files[i], list_of_new_dest_files[i]) 
        print('duplicated ' + list_of_src_files[i] + ' at ' + str(datetime.datetime.now()))
        
# Получается единственное условие, при котором цикл ничего не делает - это если совпадают имена файлов и их хэш-суммы.

