# compile/05.py
import re

r = re.compile(r'.at')  # "." заменяет один любой символ

print(r.findall('The cat in the hat sat on the flat mat.'))

# Чтобы заставить "." заменять все символы, в том числе и "\n" нам нужно воспользоваться вторым аргументом re.compile() и назначить его re.DOTALL

# (.*) - ищем все символы, re.DOTALL - включая "\n"
r = re.compile(r'(.*)', re.DOTALL)  

print(r.findall('The cat in the hat \nsat on the flat mat.'))

# вторым аргументом так же может быть re.IGNORECASE (или re.I) - игнорирует регистр букв, к сожалению второй аргумент re.compile() принимает только одно значение, чтобы использовать одновременно re.DOTALL и re.IGNORECASE нужно записать их через "|" 

r = re.compile(r'cat', re.IGNORECASE | re.DOTALL)

print(r.findall('On the flat mat \nsat the Cat in the hat'))