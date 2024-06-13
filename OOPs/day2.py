# class Student:
#     def __init__(self,fn,ln,adhar):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adhar
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
# anju = Student("anju",'pawase',23)
# print(anju.firstName)
# print(anju.lastName)
# print(anju.adharNo)
#
#
# class Teacher:
#     def __init__(self, fn, ln, adhar,salary):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adhar
#         self.salary = salary
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#     def displaySalary(self):
#         print(self.salary)
#
# siya = Teacher("sity","dighe",3211,8888)





# class student:
#     def __init__(self,fn, ln, adhar):
#         self.firstname = fn
#         self.lastname = ln
#         self.adharno = adhar
#
#     def displayName(self):
#         print(self.firstname + self.lastname)
#
# class Teacher(student):
#     def __init__(self, fn, ln, adhar,salary):
#         super().__init__(fn, ln, adhar)
#         self.salary = salary
#
#
# def displaySalary(self):
#                 print(self.salary)
#
# siya = Teacher("siya","pawase",46734,859478)
# print(siya.firstname)
# print(siya.lastname)
# print(siya.adharno)
# print(siya.salary)
#
#
# siya.displaySalary()
# siya.displayName()
#
class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    def  displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname =  ssn
    def displaySName(self):
        print(self.sname + self.lastName)

rahul = Son("ambadas","pawase","santosh","rahul")

print(rahul.firstName)
print(rahul.lastName)
print(rahul.fname)
print(rahul.sname)

rahul.displayGName()
rahul.displayFName()
rahul.displaySName()










