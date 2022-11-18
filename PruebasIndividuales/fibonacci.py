'''
Created on Oct 31, 2022

@author: estudiante
'''
rango=int(input("Cantidad de numeros: "))
numero=1
numero2=0
contador=0
lista=[]
while contador<=rango:
    contador+=2
    numero=numero2+numero
    numero2=numero+numero2
    lista.append(numero)
    lista.append(numero2)
print(lista[0:rango])
    