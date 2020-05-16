'''
Author:Kalpana Baigar
Program to print addition of total digits in number
'''


num=5187                #assign value to variable

def digit(inum):        #function defination 
    sum=0
    while(inum>0):
          digit=inum%10 
          sum=sum+digit
          inum=(inum//10) #number dividing by 10

    return sum           


iret=digit(num)
print("addition of digits in number is:",iret)
