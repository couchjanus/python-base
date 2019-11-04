# -*- coding: utf-8 -*-
# write.text.test.py

with open("hello.txt", "w") as file:
    file.write("hello world")

with open("hello.txt", "a") as file:
    file.write("\ngood bye, world")
