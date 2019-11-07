# fim_base.py
import os

path = os.getcwd()
print(path)

dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
   print(file)
