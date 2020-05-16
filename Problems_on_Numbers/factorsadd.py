'''
Author Name:Kalpana Baigar
program to accept one number and print addition of its factors 
'''


#accepting number
num=int(input("enter number"))

#function defination to print factors using for loop
def factors(inum):
    sum=0                        
    for x in range(1,inum):
        if(inum%x==0):
           sum=sum+x    
    print(sum,end=" ")         #printing addition of all factors

#function call
factors(num)
            
