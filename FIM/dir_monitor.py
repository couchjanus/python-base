# dir_monitor.py
import os

monitor=[]
d = {}
for dirname, dirnames, filenames in os.walk(os.getcwd()):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        d = {
        'path': os.path.join(dirname, subdirname)
        }

        monitor.append(d)
        print(os.path.join(dirname, subdirname))

print(monitor)