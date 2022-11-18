'''
Created on Nov 17, 2022

@author: estudiante
'''
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def estaOrdenada(lista):
    ordenada=True 
    numero1=lista[0]
    numero2=lista[1]
    for i in range(2, len(lista)):
        if numero1<numero2:
            numero1=numero2
            numero2=lista[i]
        else:
            ordenada=False 
    return ordenada
print(estaOrdenada(lista))