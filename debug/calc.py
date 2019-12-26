# Filename: calc.py

operators = ['+', '-', '*', '/']
numbers = [10, 20]

def calculator():
    print("Operators available: ")
    for op in operators:
        print(op)

    print("Numbers to be used: ")
    for num in numbers:
        print(num)

def main():
    calculator()

main()
