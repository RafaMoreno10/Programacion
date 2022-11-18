'''
Created on Oct 31, 2022

@author: estudiante
'''
#Triangulos
num=int(input("Introduce un numero"))
while num<0:
    num=int(input("Introduce un numero"))
    
cadena=""
for i in range(1,num+1):
    cadena=str(num)*i
    
    print(cadena)