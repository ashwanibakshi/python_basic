
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

#OR
print("Using OR")
a = int(input("enter value of a "))
b = int(input("enter value of b "))

if a>b or a<b:
    print("a is not equal b")
else:
    print("a is equal b")

#AND
print("Using AND")
totalmarks = int(input("enter total marks "))
if totalmarks>=90 and totalmarks<=100:
    print("Grade A") 
elif totalmarks>=80 and totalmarks<90:
    print("Grade B") 
elif totalmarks>=70 and totalmarks<80:
    print("Grade C")  
elif totalmarks>=60 and totalmarks<70:
    print("Grade D")
elif totalmarks>=50 and totalmarks<60:
    print("Grade E")
else:
    print("Grade F")     
