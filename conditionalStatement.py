#conditional statements in python

#if
print("This is IF")
a = int(input("enter value of a "))
b = int(input("enter value of b "))

if a<b:
    print("a is less than b")

if a>b:
    print("a is greater than b")

if a==b:
    print("a is equal to b")

#elseif("elif") with else
print("This is ElseIf/Else")
a = int(input("enter value of a "))
b = int(input("enter value of b "))

if a<b:
    print("a is less than b")

elif a>b:
    print("a is greater than b")

else:
    print("a is equal to b")