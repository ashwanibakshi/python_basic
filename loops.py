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

#dictionary(dict)

students = {
    "adam":"red house",
    "john":"red house",
    "paul":"green house"
} 

print(students["adam"])
print(students["john"])
print(students["paul"])

for student in students:
    print(student,students[student],sep=", ")

#here we are using dictionary("{}") in list("[]")
studentss = [
{"name":"adam","house":"red house","class":"6"},
{"name":"john","house":"red house","class":"7"},
{"name":"paul","house":"green house","class":"8"}
]

for student in studentss:
    print(student["name"],student["house"],student["class"],sep=",")

#using outer/inner for loop
size = int(input("enter width: "))

for i in range(size):
    for j in range(size):
        print("#",end="")
    print()
