'''
program accepting one number and return addition of its factors
12=(16)

prime  or not '''
#accepting number
num=int(input("enter number"))

def factors(inum):
    for x in range(1,inum):
        if(inum%x==0):
           print(x,end=" ") 
            
factors(num)
