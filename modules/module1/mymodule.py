# mymodule.py:
def sayhi():
    print("Hi! Cool module said it!")

__version__ = '0.1'

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
