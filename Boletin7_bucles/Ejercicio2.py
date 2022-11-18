'''
Created on Oct 20, 2022

@author: estudiante
'''
num1=int(input("Introduce un numero: "))
multiplo=int(input("Introduce otro numero: "))

cadena=""   
inicio=0 
for i in range(num1, num1+(multiplo*10)):
    if i%multiplo==0:
        cadena += str(i)+","
        
print(cadena)
