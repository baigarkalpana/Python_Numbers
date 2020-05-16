#program for accepting number and print that number of "*"


#accepting number from user
num=int(input("enter number"))

#function defination
def displaystar(x):
    for a in range(x):
        print("*",end=" ")
        

#function call
displaystar(num)
