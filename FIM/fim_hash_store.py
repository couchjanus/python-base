# fim_hash_store.py
import os, hashlib
import shelve

def walk(dir):
    files={}
    for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
        hash = hashlib.md5()
        with open(os.path.join(dir,file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8'))
        md5 = hash.hexdigest()
        files[file]=md5
    return files


files = walk(os.getcwd() + '/repo')
print(files)
print(type(files))

FILENAME = "repohash"

for k, v in files.items():
    print(k,v)

for k, v in files.items():
    with shelve.open(FILENAME) as repo:
        repo[k] = v

with shelve.open(FILENAME) as repo:
    for f in repo.keys():
        print(f)       
    print()
    for h in repo.values():
        print(h) 
