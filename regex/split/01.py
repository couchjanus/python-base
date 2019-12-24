# split 01.py

# re.split(pattern, string, [maxsplit=0]):
# Этот метод разделяет строку по заданному шаблону.

s = 'This is a test, short and sweet, of split().'
p = re.compile(r'\W+')
p.split(s)
re.split(',', s)

# если указать этот аргумент, то разделение будет произведено не более указанного количества раз
p.split(s, 3)

# Разделит текст по 1 или более пробелами  
re.split('\s+', s)  
# или
regex.split(s)  

# Разбить строку по нескольким разделителям

line = 'asdf fjdk;afed,fjek,asdf,foo' 
# String has multiple delimiters (";",","," ").
result = re.split(r'[;,\s]', line)
print result

# Split the string
result =re.split(r"a",line)
print(result)
