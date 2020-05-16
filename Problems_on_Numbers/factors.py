'''
Author:Kalpana Baigar
program accepting one number and printing its factors
'''

#accepting number
num=int(input("enter number"))

#function defination to print factors using for loop
def factors(inum):
    for x in range(1,inum):
        if(inum%x==0):
           print(x,end=" ") 

'''
#function defination to print factors using while loop
def factors(inum):
     i=1
     while(i<inum):
          if(inum%i==0):
             print(i,end=" ") 
          i+=1

'''




#function call            
factors(num)
