'''
Created on 17 oct 2022

@author: rafam
'''
numero=int(input("Enter a number (negative to finish):"))
b=0
while numero>0:
    b+=1
    numero=int(input("Enter a number (negative to finish):"))

print("You have entered %s positive numbers." %(b))