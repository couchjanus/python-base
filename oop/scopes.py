# scopes.py

x = 10

def my_func(a, b):
    print(x)
    print(z)

# my_func(1, 2)


# def my_funci(a, b):
#     i = 2
#     print(x)

# x = 10
# my_funci(1, 2)
# print(i)


# def my_func(a, b):
#     x = 5
#     print(x)

# x = 10
# my_func(1, 2)
# print(x)


# def my_func(a, b):
#     x = 5
#     print(x)
# x = 10
# my_func(1, 2)
# print(x)


# Python содержит оператор global. Оператор global объявляет переменную доступной для блока кода, следующим за оператором. 

# def my_func(a, b):
#     global x
#     print(x)
#     x = 5
#     print(x)
# x = 10
# my_func(1, 2)
# print(x)

# В Python 3 было добавлено новое ключевое слово под названием nonlocal. С его помощью мы можем добавлять переопределение области во внутреннюю область. 

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
print(c)

print(c())
print(c())
print(c())


