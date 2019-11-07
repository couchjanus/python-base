# fim_walk.py
import os

# Вывести список файлов для данного каталога: os.listdir(dir)

def walk(dir):
   for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
       print(file)

walk(os.getcwd() + '/repo')

