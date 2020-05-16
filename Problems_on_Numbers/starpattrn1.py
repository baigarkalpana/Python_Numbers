'''
program which accepting one number display * pattern
*****
*****
*****
*****
*****
'''

#accepting number fron user
num=int(input("enter number"))

#function defination for displaying star pattern
def stardisplay(star):

    for x in range(star):         
        for y in range(star):
            print("*",end=" ")          
        print()


#function call
stardisplay(num)
