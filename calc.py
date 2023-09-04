#Using integer

x = input("enter x value in integer?")
y = input("enter y value in integer?")

print(int(x)+int(y))

#Using float

x = input("enter x value in float?")
y = input("enter y value in float?")

#print(round (float(x)+float(y)))

z = float(x)+float(y)

print(z ,round(z))

z = float(x)/float(y)

print(f"Value without round off {z}")

#This will give 2 digits after decimal
print(f"value after round off {z:.2f}")