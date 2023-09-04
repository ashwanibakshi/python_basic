#Simple function

#we have to use def keyword for defining the function
def hello():
    print("hello world")

#Calling Function
hello()

#Creating function which will take parameter
def hello2(name):
    print("hello",name)

#Taking name input from user
name = input("enter any name")

#Calling hello2 function and passing value in it
hello2(name);

#Creating function with default value
def hello3(name="world"):
    print("hello",name)

hello3()