'''
Created on 17 oct 2022

@author: rafam
'''
numero=int(input("Enter an integer positive number"))

while numero<0:
    numero=int(input("The number is not valid, try again"))
    
total=1
c=1
while numero>=c:
    total*=c 
    c+=1
    
print("The factorial is",total)