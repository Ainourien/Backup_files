import os
from pathlib import Path
import shutil
import hashlib
import re

cwd = Path(__file__).parents[0]
os.chdir(cwd)

#Начать с того, что достать из файла путь и дату последнего изменения файла.
# Скрипт будет проходиться по всем файлам каждый час и сравнивать даты последнего...

# Не, с таким подходом нафиг... или можно сделать два варианта, один:
# 1. скрипт будет каждый час искать измененные сегодня файлы, сверять хэш-суммы и если
# они отличаются - копировать.
# 2. раз в сутки скрипт будет сверять все файлы в выбранных директориях (включая подпапки)
# по хэш-суммам. И если они отличаются - то копировать из рабочей директории в бэкап с заменой.
# 3. Сделать 2й бэкап, который будет обновляться раз в неделю по вечерам понедельника (например).

"""import hashlib


def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()""" # -- получение хэш суммы файла
        

with open("pathes.txt") as f:
    value = list(f)
    value0 = value[0].split('/n')
    value1 = value[1].split('/n')

print(value0)
print(value1)
print(value)
print(value[0])

srcfolder = [str[:-1] for str in value] # Убирает символ переноса строки (\n) в конце каждого элемента списка
srcfiles = os.listdir(srcfolder[1]) # Выводит список файлов по указанному пути


dest = 'C:\\backup\\ШК на коробки'

#shutil.rmtree(dest, ignore_errors=True) #Удаляет папку и все подпапки с файлами
#shutil.copytree(srcfolder[0], dest)

#print(os.stat(str(a[0] + '\\' + b[0])))


def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest() # -- получение хэш суммы файла

print(get_hash_md5(str(srcfolder[1] + '\\' + srcfiles[0])))

#Теперь надо в цикле сравнивать хэши и если какие-то файлы не совпадут - то их копировать.

print(srcfiles)

for i in range(len(srcfiles)):
    ext = re.findall(r'.\w+', srcfiles[i])
    print(ext)
    ext = ext[-1]


    '''if ext != '.py':
        os.makedirs(('.\\' + ext), exist_ok=True)
        shutil.move(a[i], ('.\\' + ext))'''