'''
Author:Kalpana Baigar
Program to print following number pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


'''

num=int(input("enter number"))  #accepting input from user

def numberpattrn(inum):         #function defination
    for x in range(1,num):
        for y in range(1,x+1):
            print(y,end=" ")    #printing number

        print()                 #printing new line



numberpattrn(num)               #calling to function
