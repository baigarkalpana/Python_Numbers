'''
Program which contains one function named as chknum() which accept on parameter as number.If the number is even then it should display "Even Number" otherwise
display "Odd number"
'''


#Accepting number fron user
num=int(input("enter number"))
print("your entered number is",num)


# Function chknum printing wether number is even or odd
def Chknum( inum):   
    if(num%2==0):
       print("Even Number")
    else:
       print("Odd Number") 


#calling fuction 
Chknum(num)
