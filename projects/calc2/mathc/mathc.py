# module mathc.py:

def add(a, b):
    return a + b
    
def sub(a, b):
    return a-b
 
def mul(a, b):
    return a * b
 
def div(a, b):
    return a / b

def idiv(a, b):
    return a // b

def mod(a, b):
    return a % b

def sqrt(a):
    return a**(.5)

def pow(a, n):
    return a**n

def area_triangle(a, b, c):
    x = (a+b+c)/2
    result = x*(x-a)*(x-b)*(x-c)
    return sqrt(result)
