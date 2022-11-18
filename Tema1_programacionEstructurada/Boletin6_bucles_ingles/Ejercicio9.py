'''
Created on 17 oct 2022

@author: rafam
'''
number= int(input("Enter an integer number greater than 0"))
while number <1:
    number=int(input("The number is not valid, try again"))
    
sumaDivisores=0

for i in range(1, (number//2)+1):
    if number%i==0:
        print(i)
        sumaDivisores+=i 
    
if sumaDivisores == number:
    print("The number is perfect")
else:
    print("The number is not perfect")