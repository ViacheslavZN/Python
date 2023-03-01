"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?"""
import os

mainfolder_name = 'my projects'
downfolder_names = ['mainapp', 'settings', 'adminapp', 'authapp']

for i in downfolder_names:
    pos = 0
    size = int(len(downfolder_names)) - 1
    while pos <= size:
        dir_path = os.path.join(mainfolder_name, downfolder_names[pos])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        pos = pos + 1

# написать скрипт, который выдаст статистику для заданной папки в виде словаря,
# в котором ключи - верхняя границ размера файла, а значения - общее количество файлов

import os
import stat
from os.path import relpath
from collections import defaultdict

size_100 = 0
size_1000 = 0
size_10000 = 0
size_100000 = 0
size_xxl = 0
size_base = {}
folder_path = r'C:\Users\Asus\Desktop'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        f_path = os.path.join(root, file)
        size = os.stat(f_path).st_size
        if 0 < size <= 1000:
            size_1000 += 1
        elif 1001 < size <= 10000:
            size_10000 += 1
        elif 10001 < size <= 100000:
            size_100000 += 1
        elif size > 100000:
            size_xxl += 1
size_name = ('100', '10000', '100000', '>100000')
m = (size_100, size_10000, size_100000, size_xxl)
for i in size_name:
    pos = 0
    for j in m:
        while pos < int(len(size_name)):
            size_base[size_name[pos]] = m[pos]
            pos += 1

print(size_base)
