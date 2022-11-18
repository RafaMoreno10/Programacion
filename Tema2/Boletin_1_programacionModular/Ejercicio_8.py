'''
Created on Nov 17, 2022

@author: estudiante
'''

def es_primos(num):
    esPrimo = True 
    
    if num > 2:
        for i in range(2,num):
            if num%i==0:
                esPrimo=False 
    return esPrimo


def listar_Primos(lista):
    listaPrimos=[]
    for i in range(len(lista)):
        if es_primos(lista[i])==True:
            listaPrimos.append(lista[i])
    return listaPrimos

def sumatorio(lista):
    varuable=0
    for i in range(len(lista)):
        varuable+=lista[i]
    return varuable

def media_total(lista):
    media=0
    for i in range(len(lista)):
        media=(sumatorio(lista))/(len(lista))
    return media




manolo=[1,2,3,4,5,6,7,8]  
print(listar_Primos(manolo))
print(sumatorio(manolo))
print(media_total(manolo))
