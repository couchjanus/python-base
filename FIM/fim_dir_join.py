# fim_dir_join.py
import os

path = os.getcwd() + '/repo'
print(path)

for file in [item for item in os.listdir(path) if os.path.isfile(os.path.join(path,item))]:
  print(file)
