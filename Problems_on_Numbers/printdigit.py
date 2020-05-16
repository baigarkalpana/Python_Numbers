'''
   Author:Kalpana Baigar
   program to break integer into digits
'''
 
num=int(input("enter number:")) #Accepting number from user
print(num)                      #printing number


def chkdigit(inum):             #funtion defination
 digit=0                        #assigning value
 cnt=1
 while(inum>0):          
     digit=inum%10
     print("digit at place{0} is {1}".format(cnt,digit)) #printing digits
     cnt+=1            #incremented by 1
     inum=inum//10



chkdigit(num)                    #function call

