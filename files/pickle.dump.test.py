# -*- coding: utf-8 -*-
# pickle.dump.test.py

from pickle import dump, load
 
data = [['!', '@', '#'],
        [200, 300, 900],
        b'qwertyuiopas',
        'йцукенгшщзхъф']
 
with open('data', 'wb') as f:
    dump(data, f)
 
with open('data', 'rb') as f:
    data = load(f)
     
for j in data:
    print(j)
