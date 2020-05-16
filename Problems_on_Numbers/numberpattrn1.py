'''
Author:Kalpana Baigar
Program to printing following pattern

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''


num=int(input("enter number"))

def numberpattrn(inum):
    for x in range(1,num):
        for y in range(1,num):
            print(y,end=" ")

        print()




numberpattrn(num)
