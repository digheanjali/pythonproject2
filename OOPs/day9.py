# program 1
# class Employee:
#     def __init__(self,fn,ln,adharNo):
#         # instance properties
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
#
#     # Instance method
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#     def changeAdhar(self,change):
#         self.adharNo = change
#
# tusha = Employee("tusha","pawase","094")
# tusha.changeAdhar("23432")


# program 2
class Employee:
    country  = "India"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    @classmethod
    def changeCountry(cls):
        cls.country = "Bharat"

    def displayName(self):
        print(self.firstName + self.lastName)

anju  = Employee("anju","dighe")
print(anju.firstName)
print(anju.lastName)
print(anju.country)
anju.displayName()

rahul  = Employee("rahul","rahul")
print(rahul.firstName)
print(rahul.lastName)
print(rahul.country)
rahul.displayName()

rahul.country = "Bharat India"
print(rahul.country) # Bharat
print(anju.country) # India

Employee.changeCountry()
print(rahul.country)
print(anju.country)

# number of Objects

class Myclass:
    n = 0
    def __init__(self):
        Myclass.n = Myclass.n + 1

    @staticmethod
    def noObject():
        print(Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()

print(Myclass.noObject())
