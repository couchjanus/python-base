# fim_calc_hash_cli.py

import os, hashlib, time, base64
import sys

monitor=[]

def monit(dir):
  mon=[]
  for dirname, dirnames, filenames in os.walk(dir):
    for subdirname in dirnames:
        d = {
        'path': os.path.join(dirname, subdirname),
        'recursive':True
        }
        mon.append(d)
  return mon

files={}

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

def getBytes(file):
  return base64.b64encode(open(file, "rb").read())

def fim():
  while True:
    for file in getFiles():
      hash = hashlib.sha256()
      with open(file) as f:
        for chunk in iter(lambda: f.read(2048), ""):
          hash.update(chunk.encode('utf-8'))
      sha256 = hash.hexdigest()
      if file in files and sha256 != files[file]['sha256']:
        print(f'{file} has been changed at {time.strftime("%Y-%m-%d %H:%M:%S")}!')
      files[file]={'sha256':sha256,'bytes':getBytes(file)}
    time.sleep(1)

if len (sys.argv) == 1:
    print ("Hello, {}!".format (sys.argv[0]))
    
    monitor = monit(os.getcwd())
    fim()
else:
    if len (sys.argv) < 3:
        print ("Ошибка. Слишком мало параметров.")
        sys.exit (1)

    if len (sys.argv) > 3:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    param_name = sys.argv[1]
    param_value = sys.argv[2]

    if (param_name == "--name" or param_name == "-n"):
        print ("Привет, {}!".format (param_value) )
        path = os.getcwd()
        os.chdir(path + '/' + param_value)
        
        monitor.append({
        'path': os.getcwd(),
        'recursive':True
        })
        monitor += monit(os.getcwd())
        print(monitor)
        fim()
    else:
        print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
        sys.exit (1)

