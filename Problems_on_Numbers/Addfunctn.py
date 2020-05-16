'''
Writing program which contains Add() function,accepting two numbers from user and
return additon of two numbers
'''


#Accepting number from user
inum1, inum2 =int(input("Enter First number: ")), int(input("Enter second number: "))

#Function Defination of Add()
def Add(num1,num2):
    c=num1+num2
    return c

#Calling to Add function and taking return value in variable    
iret=Add(inum1,inum2)

#Printing addition of numbers
print(iret)
