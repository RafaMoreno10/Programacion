'''
Created on 22 nov 2022

@author: rafam
'''
def unionListas(lista1, lista2):
    lista=[]
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista.append(lista1[i])
    
    for i in range(len(lista2)):
        if lista2[i] not in lista1:
            lista.append(lista2[i])
   
    return quitarRepeticiones(lista)


print([1,2,3])
print([2,3,4,5])
print("La union de las dos listas:",unionListas([1,2,3], [2,3,4,5]))