#string as a parameter and string as a return type
def greet(name):
    return "hello" + name
q1 = greet("chinmay")
print(q1)

# list as parameter and list as return type
city = ["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
q2 = addCity(city)
print(q2)

# dictionary as a parameter and dictionary as a return type
info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
def addLanguage(information):
    information.update({"language":"marathi"})
    return information
q3 = addLanguage(info)
print(q3)

# tuple as a parameter and tuple as return type
names = ("chinmay","ninad","sachin","ramesh","suresh")
def addElementToTupe(nmT):
    nmT = list(nmT)
    nmT.append("vijeet")
    nmT = tuple(nmT)
    return nmT

q4 = addElementToTupe(names)
print(q4)

# set as parameter and set as a return type

setA = {11,22,33,44,55}

def addSetCValue(setToAdd):
    setToAdd.add(34)
    return setToAdd

q5 = addSetCValue(setA)
print(q5)

# int as parameter and int as return
a = 15
B = a
def addvalue(B):
    B = B + a
    return B
w1 = addvalue(a)
print(w1)

# float as a parameter and float as return

# boolean as parameter and boolean return type

# def add(x,y):
#     return x + y
# q1 = add(12,3)
# print(q1)
#
# add = lambda x,y:x+y
# print(add)
# q2 = add(23,4)
# print(q2)


# function as a parameter
sub = lambda x,y:x-y
def subtraction(fn,x,y):
    # fn = lambda x,y:x-y
    q3 = fn(x,y)
    return q3

q4 = subtraction(sub,10,5)
print(q4)