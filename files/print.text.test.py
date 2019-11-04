# -*- coding: utf-8 -*-
# print.text.test.py

with open("hello.txt", "a") as hello_file:
    print("Hello, world", file=hello_file)
