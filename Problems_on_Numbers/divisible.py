#program which contains one function that accept one number and returns true if divisible by 5 otherwise return false


#accepting number from user
num=int(input("enter number"))
              
#function defination to check wether number is divisible by 5 or not
def numdivisible(inum):
    if(inum%5==0):
       return True
    else:
        return False

#function call
iret=numdivisible(num)
print(iret)
