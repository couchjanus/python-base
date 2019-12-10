class DecoratorTest(object):
    def __init__(self):
        """Конструктор"""
        pass
    # обычный метод 
    def doubler(self, x):
        print("умножаем на 2")
        return x*2

    @classmethod
    def class_tripler(klass, x):
        print("умножаем на 3: %s" % klass)
        return x*3
    
    @staticmethod
    def static_quad(x):
        print("умножаем на 4")
        return x*4


if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))

    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)
