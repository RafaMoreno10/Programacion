'''
Created on 17 oct 2022

@author: rafam
'''
numero=int(input("Enter one number: "))
pregunta=input("Do u want to enter more number (Y/N) ").upper()
while pregunta=="Y":
    menor=numero
    numero=int(input("Enter one number: "))
    if numero<menor:
        menor=numero
    pregunta=input("Do u want to enter more number (Y/N) ").upper()
else:
    print("The smallest number is %s"%(menor))
