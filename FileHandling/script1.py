# program 1
# open the file for writing data
f = open("myfile.txt",'w')                 # open == object , w for write operation
# # enter the characters from keyword
e = input('Enter the name')
# # write the string into the file
f.write(e)
# # closing th file
f.close()


# program 2
f2 = open('myfile.txt','r')   # r for read operation   # when myfile.text file alresdy create then not new file create.
str = f2.read()
print(str)
f2.close()


f3 = open('myfile2.txt','w')              # open == new file create name as myfile.text
print("Enter '@' to exit")
while str != '@':
    str = input("Please enter multiple names")
    if str != '@':
        f3.write(str + "\n")
f3.close()


# program 4
f4 = open('myfile.txt','+a')             #+a ----for read and write
print("Enter '@' to exit")
while str != '@':
    str = input("Please enter multiple names")
    if str != '@':
        f.write(str + "\n")
f4.seek(0,0)                      #seek----move curser at the top for read the file
str = f4.read()
print(str)
f4.close()                          #close()---- it protect the file from curruption







