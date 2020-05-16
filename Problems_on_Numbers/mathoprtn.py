#program performing basic math operations


import operator

#accepting two numbers to perform operations
first=int(input("enter first number"))
second=int(input("enter second number"))

#function defination for addition
def addfun(num1,num2):
    print("addition is:",operator.add(num1,num2))
    subfun(first,second)

#function defination for subtraction
def subfun(num1,num2):
    print("subtraction is:",operator.sub(num1,num2))
    multfun(first,second)

#function defination for multiplication
def multfun(num1,num2):
    print("multiplication is:",operator.mul(num1,num2))
    divfun(first,second)


#function defination for division
def divfun(num1,num2):
    print("division is:",operator.truediv(num1,num2))
       

#function call
addfun(first,second)
