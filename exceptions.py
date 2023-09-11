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

#We can use try except else block for solving this problem
#Now if we enter wrong value for z then except block will handle it.
try:
     z = int(input("Enter Value Of z ? "))
except ValueError:
     print("z value should be integer only")
else:
     print("z is ",z)

# using loop which will keep on taking the input from user untill user give the correct input

# while True:
#     try:
#         i = int(input("enter i value? "))
#     except ValueError:
#         print("i value be integer")
#     else:
#         break
# print("i is ",i)

while True:
    try:
        i = int(input("enter i value? "))
        break
    except ValueError:
        print("i value be integer")

print("i is ",i)

# def main():
#     x= getInt()
#     print('x is ',x)

# def getInt():

#      while True:    
#           try:
#                return int(input("enter i value? "))
#                # return i
#           except ValueError:
#                print("i value be integer")

# main()