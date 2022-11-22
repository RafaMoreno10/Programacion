'''
Created on 22 nov 2022

@author: rafam
'''
def quitarRepeticiones(lista):
    listaSin=[]
    for i in range(len(lista)):
        if lista[i] not in listaSin:
            listaSin.append(lista[i])
    return listaSin

def intersect(lista1, lista2):
    lista=[]
    a=0
    for i in range(len(lista1)):
        a=lista1[i]
        cont=0
        while cont<len(lista2):
            if lista2[cont]==a:
                lista.append(lista2[cont])
                cont+=1
            else:
                cont+=1
   
    return quitarRepeticiones(lista)


print("[1,2,2,3,4,3,5]") 
print("[1,9,2,3,3,7,4,4,1,5]") 
print("La interseccon entre las dos listas esta en:",intersect([1,2,2,3,4,3,5], [1,9,2,3,3,7,4,4,1,5]))