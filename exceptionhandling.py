# 👉 Exception handling
#################################################
a = 100
b = 200
# b = 0 #user input
c = a/b #ZeroDivisionError: division by zero
print(a)
print(b)
print(c)

name = "PALLAVI"
print(name)
print(name[0])
# print(name[10])#IndexError: string index out of range

print("Hello World")


# syntax

# try:
#   code
# except:
#   code
# except:
#   code
# else: # if no error in the code i.e with no exceptions
#   code
# finally:
#  code

a = 100

try:
  b = 0
  c = a/b
  print(c)
except:
  print("Something went wrong !!!")




name = "PALLAVI"
print(name)

try:
  print(name[10])
except:
  print("Something went wrong !!!")

print("Hello World")


# https://docs.python.org/3.12/library/exceptions.html#exception-hierarchy


#  adding more info to the  user/code
try:
  b = 0
  c = a/b
  print(c)
except Exception as i_am_error:
  print("Something went wrong !!!", i_am_error)


try:
  print(name[10])
except Exception as e:
  print("Something went wrong !!!",e)

print("Hello World")



# catching multiple exceptions

try:
  b = 100
  c = a/b
  print(c)
  print(name[3])
except Exception as e:
  print("Something went wrong !!!",e)
except Exception as f:
  print("Something went wrong !!!",f)
else:
  print("No error found")
finally:
  print("This line will always get excecuted !!!")