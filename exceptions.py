#This line of code will give Sytax Error as we didnt close the double quotes
# print("hello,world)
print("hello,world")

#This line of code will give ValueError if we enter wrong value so 
#we can use try except block 
# x = int(input("Enter Value Of X ? "))
# print(f"x is {x}")

try:
     x = int(input("Enter Value Of X ? "))
     print("x is ",x)
except ValueError:
     print("x value should be integer only")

#This line of code will give NameError when provide any value other than int.Then int() function will through this error
# and no value be assigned to y variable.
# This error will be displayed " NameError: name 'y' is not defined "
try:
     y = int(input("Enter Value Of y ? "))
except ValueError:
     print("y value should be integer only")

print("y is ",y)