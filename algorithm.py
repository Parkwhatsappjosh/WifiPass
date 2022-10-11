import random

list1= [1,2,3,4,5,6,7,8,9,0]
#for 8 digit password
passw = str()
for i in range(8):
    n1= random.randint(0,9)
    passw = passw+str(n1)
    
print(passw)
