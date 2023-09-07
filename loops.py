#while loop

i = int(input("enter value of i :"))

j=0;

while j<i :
    print("hello")
    j=j+1

while True:
    n = int(input("enter value of n :"))
    if n<=0:
        continue
    else:
        break 

print(n)  

#for loop 
#range() it always take integer
for _ in range(n):
    print('hi')

#list
students = ["adam","john","marya"]

for s in students:
    print(s)

print("\n")

#print data using index in for loop
for s in range(len(students)): 
    print(students[s],s)   