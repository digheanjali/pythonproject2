
# Abstrat class

# class Myclass:
#     def calculate(self,x):
#         print(x)
#

# obj using duck typing

# obj = Myclass()
# obj.calculate(1)
# obj1 = Myclass()
# obj.calculate(2)
# obj2 = Myclass()
# obj2.calculate(3)


from abc import ABC,abstractmethod

class myClass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass

class square(myClass):
    def calculate(self,x):
     print("square")


class Cube(myClass):
    def calculate(self,x):
        print("cube")

class squareRoot(myClass):
    def calculate(self,x):
        print("squareRoot")




obj = square()
obj1 = Cube()
obj2 = squareRoot()

print(obj.calculate(12))
print(obj1.calculate(34))
print(obj2.calculate(56))

# we cannot create object of abstract class
# abstract class can have - abstract method and non - abstract method
# it mandatory for class to implement abstract method if inherited

class vehicle(ABC):
    @abstractmethod
    def wheel(self,x):
        pass


    def country(self):
        print("India")

class Maruti(vehicle):
    def wheel(self, x):
        print("5 wheel")


class Audi(vehicle):
    def wheel(self, x):
        print("4 wheel")



a = Maruti()
a.country()
a.wheel(5)

b = Audi()
b.wheel(4)
b.country()




















