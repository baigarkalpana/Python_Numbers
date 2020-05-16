'''
Author:Kalpana Baigar
program to check accepted number is prime or not
'''

#accepting number from user
num1="7"                        #takinng input as a sting value
x=int(num1)                     #converting string type to integer typ
print(x)
print(type(x))

def prime(num):
    
    for x in range(2,num):                #values in the range of 2 to num-1
        if(num%x==0):                     #if number is divisible
         #  print("not a prime number")    #printing number is prime
           return True;
           break;
    else:
          # print("prime number")
          return False

iret=prime(x)
if(iret==True):
    print("not a prime number") 

else:
    print("prime number")
