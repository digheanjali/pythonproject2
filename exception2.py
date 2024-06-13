# compile time error
# runtime errors
# logical error

# program 1
# def addition(x,y)
#     print(x+y)
# addition(8,4)

# program 2
# x = input("Enter the number one")
# y = input("Enter the number two")
# print("hello")
# print(int(x)/int(y))
# print("bye")

# program 3
# def calculateAge(age):
#     return age
#
# e = calculateAge(20)
# print(e)

# program 4
# print("hello")
# print(10 /0)
# print("bye")

print("hello")
try:
    print(10/0)
except Exception:
    print("Division by zero")
print("hello")

print("-----------------------------")
try:
    print(10/5)
    print([11,22,33,44,5].index(67))
except Exception:
    print("hi")
except Exception:
    print("Bye")
else:
    print('hello')
finally:
    print('this will always executed')