# fim_cli.py

import os, hashlib, time, base64
import sys

monitor=[]

for dirname, dirnames, filenames in os.walk(os.getcwd()):
    for subdirname in dirnames:
        d = {
        'path': os.path.join(dirname, subdirname),
        'recursive':True
        }
        monitor.append(d)

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

print(sys.argv)
print(sys.argv[1:])

argv = sys.argv
print(len(argv))
arg = argv.pop()
print(arg)
print(len(argv))

if len (sys.argv) > 0:
    print ("Привет, {}!".format (sys.argv[0]))

for param in sys.argv:
    print(param)

if len (sys.argv) == 1:
    print ("Привет, {}!".format (sys.argv[0]))
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
    else:
        print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
        sys.exit (1)
