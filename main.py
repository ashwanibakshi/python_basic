# input function always takes data as string only 
name = input("enter name ")
print("hello",name)

# here we can use a special symbol f in print() to show the output
print(f"hello,{name}")

#Remove whitespace from string
name = name.strip()

#Capitalize user's name first letter
name = name.capitalize()

#Capitalize users name as title like 'Jon Doe'
name = name.title()

print("hello,",name)

