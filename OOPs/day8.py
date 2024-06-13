# program
# class Calculator:

#     c = 10   //# class level variable
#     def __init__(self,x,y,z):
#         # instance variable
#         self.x = x
#         self.y = y
#         self.z = z
#
# anju = Calculator(122,133,144)
# tushar = Calculator(121,131,141)
# print(anju.x)
# print(anju.y)
# print(anju.z)
# print(anju.c)
#
# print(tushar.x)
# print(tushar.y)
# print(tushar.z)
# print(tushar.c)
# tushar.c = 99
#
# print(anju.c)
# print(tushar.c)

# program 2 changing value of instance level variable

class CalculatorB:
    a = 10
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # instance level method
    def changeX(self,change):
        self.x = change

siya = CalculatorB(12,3)
print(siya.x)
print(siya.y)
siya.changeX(45)
print(siya.x)


class CalculatorC:
    c = 10
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    @classmethod
    def changeC(cls,ch):
        cls.c = ch
rahul = CalculatorC(3,4)
print(rahul.x)
print(rahul.y)
print(rahul.c)


anjali = CalculatorC(13,14)
print(anjali.x)
print(anjali.y)
print(anjali.c)

CalculatorC.changeC(45)
print(anjali.c)
print(rahul.c)

# anjali.c = 99
# print(rahul.c)
# print(anjali.c)


anjali.c = 99
print(rahul.c)





