# fim_get_file_monitor.py
import os, hashlib
import shelve
import time

files={}

monitor=[]
d = {}

for dirname, dirnames, filenames in os.walk(os.getcwd()):
    for subdirname in dirnames:
        d = {
        'path': os.path.join(dirname, subdirname),
        'recursive':True
        }
        monitor.append(d)

# print(monitor)

def getFiles():
    filesList=[]
    for x in monitor:
        if os.path.isdir(x['path']):
            if x['recursive']:
                filesList.extend([os.path.join(root, f) for (root, dirs, files) in os.walk(x['path']) for f in files])
            else:
                filesList.extend([item for item in os.listdir(x['path']) if os.path.isfile(item)])
        elif os.path.isfile(x['path']):
            filesList.append(x['path'])
    return filesList

while True:
    for file in getFiles():
        hash = hashlib.sha256()
        with open(file, encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8'))
        sha256 = hash.hexdigest()
        if file in files and sha256 != files[file]:
            print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}!')
        files[file]=sha256
    time.sleep(1)