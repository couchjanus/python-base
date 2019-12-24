# search 02.py
import re

string = 'test'

pattern1 = 'that$'
pattern2 = '^I once'
pattern3 = '^test$'

# Строка заканчивается на 'test'
if re.search(pattern1, string) is None:
    print("Строка заканчивается на 'test'")

# Строка не начинается на 'test'
if re.search(pattern2, string) is None:
    print("Строка не начинается на 'test'")

# Строка не является строкой 'test'
if re.search(pattern2, string) is None:
    print("Строка не является строкой 'test'")

# Строка является строкой 'test'
if re.search(pattern3, string):
    print("Строка является строкой 'test'")
