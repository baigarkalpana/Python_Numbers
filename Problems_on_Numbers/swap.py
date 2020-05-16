'''
   Author:Kalpana Baigar
   program to swap two numbers in different way
'''
 


print("method one:")               
no1,no2=input("enter two values:").split()
print("number1: {} and number2: {}".format(no1,no2))


def swap(no1,no2):
    temp=no1
    no1=no2
    no2=temp
    print("after swapping:")
    print("no1 is:",no1)
    print("no2 is:",no2)

swap(no1,no2)

print("********")
print("method two")

print("before swapping")
no1,no2=12,10
print("no1 is:",no1)
print("no2 is:",no2)
print("after swapping")
no1,no2=no2,no1
print("no1 is:",no1)
print("no2 is:",no2)


print("********")
print("method three using list:")
print("before swapping")
l=[10,20]
print("no1 is:",l[0])
print("no2 is:",l[1])

l[0],l[1]=l[1],l[0]
print("after swapping")
print("no1 is:",l[0])
print("no2 is:",l[1])




