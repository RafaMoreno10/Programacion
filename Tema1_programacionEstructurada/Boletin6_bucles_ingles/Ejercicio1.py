'''
Created on 17 oct 2022

@author: rafam
'''
#Creamos un programa que nos dira todos los numeros multiplos de 7 y 13, entre 1 y 100

for x in range (1,101): 
    print(x)
    if x%7==0:
        print("Es multiplo de 7")
    if x%13==0:
        print("Es multiplo de 13")
    if x%13==0 and x%7==0:
        print("Es multiplo de 7 y 13")
