'''
Author:Kalpana Baigar
Program to count total digits in number
'''


num=5187                #assign value to variable

def digit(inum):        #function defination 
    count=0
    while(inum>0):
          digit=inum%10
          count+=1

          inum=(inum//10)

    return count           


iret=digit(num) #return value of function store in iret
print("total digits in number is:",iret) #prining total digits
