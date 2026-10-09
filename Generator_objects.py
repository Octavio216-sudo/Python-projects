choose = int(input("Choose a number: "))

#---------------------------------------------------------------------------------------------------1
#Demonstration of iter protocol using generator objects. There are simpler ways to do this with yield, but this is to demonstrate the iter protocol.
if choose == 1:
    class Fibonacci_generator:
        def __init__(self, n):
            self.__n = n
            self.__i = 0
            self.__v1 = 1
            self.__v2 = 1
        def __iter__(self):
            return self
        def __next__(self):
            if self.__i < self.__n:
                if self.__i == 0 or self.__i == 1:
                    self.__i += 1
                    return 1
                else:
                    self.__v1, self.__v2 = self.__v2, self.__v1 + self.__v2
                    self.__i += 1
                    return self.__v2
            else:
                raise StopIteration

    class Class: #composition of generator object in a class
        def __init__(self, n):
            self.__iter__ = Fibonacci_generator(n)
        def __iter__(self):
            return self.__iter__   
    object1 = Fibonacci_generator(10)
    for i in object1: #generator objects cannot be invoked explicitly, they are invoked implicitly by the for loop
        print(i)

    object2 = Class(10)
    for i in object2: #generator objects cannot be invoked explicitly, they are invoked implicitly by the for loop
        print(i)

#---------------------------------------------------------------------------------------------------2
#very simple yield demonstration
if choose == 2:
    def fibonacci_yield(n):
        a, b = 1, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    for i in fibonacci_yield(10):
        print(i)
