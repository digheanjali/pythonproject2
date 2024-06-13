# Program 1
class Person:
    firstName = None
    lastName = None
    age = None
    rollNo = None
    def displayName(self):
        print(self.firstName + self.lastName)

anjali = Person()
print(anjali.firstName)
print(anjali.lastName)
print(anjali.age)
print(anjali.rollNo)
# anjali.displayName()

anjali.firstName = "anjali"
anjali.lastName = "pawase"
anjali.age = 25
anjali.rollNo = 18

print(anjali.firstName)
print(anjali.lastName)
print(anjali.age)
print(anjali.rollNo)


# program 2

# __init__ ==== constructor
class PersonB:
    def __init__(self,fn,ln,ag,roll):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.rollNo = roll

    def displayName(self):
        print(self.firstName  + self.lastName)

 anjaliB = PersonB("anjaliB","pawaseB",66,88)
rahulB= PersonB("rahulB","digheB",32,63)
