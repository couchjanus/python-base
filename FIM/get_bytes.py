# get_bytes.py

import os,hashlib,base64

file='./repo/README.md'

def getBytes(file):
  return base64.b64encode(open(file, "rb").read())

print(getBytes(file))
