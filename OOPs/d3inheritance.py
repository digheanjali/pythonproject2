#
# # ===========> INHERITANCE <===========
#
# class Mother:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#
#     def displayM(self):
#         print(self.firstname + self.lastname)
#
#
# class Father:
#     def __int__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#
#     def displayF(self):
#         print(self.firstname + self.lastname)
#
#
# # Mothers method call BCZ mother in first left side
# class son(Mother,Father):
#     def __int__(self,fn,ln,ssn):
#         super().__int__(fn,ln)
#         self.sname = ssn
#
# def displayS(self):
#     print(self.sname + self.lastname)
#
# anjali = son("suman","pawase","tushar")
#
#
#
# # Method resolution order

class A(object):
    def method(self):
        print("A is called")
        super().method()


class B(object):
    def method(self):
        print("B is called")
        super().method()

class C(object):
    def method(self):
        print("C is called")



class X(A,B):
    def method(self):
        print("X is called")
        super().method()

class Y(B,C):
    def method(self):
        print("Y is called")
        super().method()



class P(X,Y,C):
    def method(self):
        print("P is called")
        super().method()

# p is call,x is call,A is call,y is call,b is call,c is call

p = P()
p.method()




















