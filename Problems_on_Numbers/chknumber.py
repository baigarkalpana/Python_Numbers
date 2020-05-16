#Program to check wether number is positive,negative or zero


#accepting number
x=int(input("enter number"))
print(x)

#function defination to chk given number
def numberchk(num):
    if(num>0):
       print("positive number") 
    elif(num<0):
        print("negative number")
    else:
        print("zero number")

#function call
numberchk(x)
