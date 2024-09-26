import os

import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime(os.getcwd())
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(os.getcwd())
        parent_dir = os.path.dirname(os.getcwd())

print(f'Обнаружен файл: {file}, Путь: {filepath}'
      f', \nРазмер: {filesize} байт, Время изменения: {formatted_time}'
      f', \nРодительская директория: {parent_dir}')
