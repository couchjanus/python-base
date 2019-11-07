# fim_dir_cd.py
import os

path = os.getcwd()
print(path)

dirs = os.listdir(path +'/repo')

# This would print all the files and directories
for file in dirs:
   print(file)

os.chdir(path +'/repo')

print(os.getcwd())

for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
  print(file)
