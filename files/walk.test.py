# -*- coding: utf-8 -*-
# walk.test.py

# В следующем примере мы получим статистическую информацию о текущем каталоге: 
# общий размер каталога в байтах, число файлов, число подкаталогов. 
# Стандартная функция os.path.walk имеет параметр каталог

import os, sys, os.path

sums = [0,0,1] # 0 bytes, 0 files, 1 directory so far

def stat(path):
    tree = os.walk(path)
    for address, dirs, files in tree:
        for file in files:
            if os.path.isfile(file):
                sums[0] += os.path.getsize(file)
                sums[1] += 1
            else:
                sums[2] += 1
            print(address+'/'+file)
    return sums
 
report = stat('/home/janus/www/pyton-fundamental')

print(report)
