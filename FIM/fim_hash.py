# fim_hash.py
import os,hashlib

def walk(dir):
   for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir,item))]:
        # Создаем новый экземпляр класса hashlib.md5():
        hash = hashlib.md5()
        with open(os.path.join(dir,file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048), ""):
                hash.update(chunk.encode('utf-8'))
        md5 = hash.hexdigest()
        print(file,md5)

walk(os.getcwd() + '/repo')
