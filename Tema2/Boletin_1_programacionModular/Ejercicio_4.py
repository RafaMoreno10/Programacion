'''
Created on Nov 15, 2022

@author: Rafa Moreno
'''




def mostrar_mayor(lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor+=lista[i]
  
    return mayor

def numeros_pares(lista):
    listaPar=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            listaPar.append(lista[i])
    return listaPar

lista=[]
num=int(input("Introduce un numero"))
while num>0:
    lista.append(num)
    num=int(input("Introduce un numero"))
print(lista)
print(numeros_pares(lista))
print(mostrar_mayor(lista))   