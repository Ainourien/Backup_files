import os
from pathlib import Path
import shutil
import hashlib
import re
import glob


cwd = Path(__file__).parents[0]
os.chdir(cwd)

with open("..\\source_pathes.txt") as f:
    src_value = list(f)

src_folder = [str[:-1] for str in src_value] # Убирает символ переноса строки (\n) в конце каждого элемента списка
src_files = os.listdir(src_folder[0]) # Выводит список файлов по указанному пути

with open("..\\destination_pathes.txt") as f:
    dest_value = list(f)
dest_folder = [str[:-1] for str in dest_value]

# Берем список файлов в src, и список файлов в dest и сверяем сначала наличие, если есть, то хэш, если не совпадает, то копируем.
# А в начале проверяем каждый файл папка он или нет. Если да, то берем список файлов из этой папки и делаем что выше.

# Посчитаем количество файлов в источнике:
'''num_files = len ([f for f in os.listdir(src_folder[0]) 
                    if os.path.isfile(os.path.join(src_folder[0], f))])

print(num_files)

a = len([os.walk(src_folder[0])])
print(a)
b = 0

for i in os.walk(src_folder[0]):
    print(len(i))
    b += len(i)

print (b)

print(len([1 for x in list(os.scandir(src_folder[0])) if x.is_file()]))

print(len(glob.glob(src_folder[0])))'''
list_of_subfolders = []
#Находим папки в списке файлов из источника:
for csf01 in os.listdir(src_folder[0]):
    if not os.path.isfile(src_folder[0] + '\\' + csf01):
        subf_1 = src_folder[0] + '\\' + csf01   # Получили полный путь к первой внутренней папке
        list_of_subfolders.append(subf_1)   # 
        print(subf_1)
        for csf02 in os.listdir(subf_1):  # Список файлов и папок во внутренней папке
            if not os.path.isfile(subf_1 + '\\' + csf02): # Для каждой обнаруженной папки мы получаем список файлов и папок
                subf_2 = subf_1 + '\\' + csf02   # Получили полный путь ко второй внутренней папке
                list_of_subfolders.append(subf_2)
                print(subf_2)
print(list_of_subfolders)
#print(os.path.isfile('backup_003.py'))

# начнем с того, что скопируем один файл, потом один файл с проверкой, потом один файл с подпапкой
