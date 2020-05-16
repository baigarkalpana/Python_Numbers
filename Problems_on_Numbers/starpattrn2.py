'''
Author:Kalpana Baigar
Program to print following star pattern

* * * * *
* * * *
* * *
* *
*

'''


num=int(input("enter number"))    #accepting number from user

def starpattrn(numbr):            #function defination
    for x in range(numbr,0,-1):
        for y in range(0,x):
            print("*",end=" ")    #printing star
        print()                   #new line printing


starpattrn(num)                    #function call
