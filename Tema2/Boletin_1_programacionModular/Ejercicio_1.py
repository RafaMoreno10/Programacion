
from random import randint

lista1=[]
numeros=int(input("Con cuantos numeros quieres trabajar?: "))
for i in range(numeros+1):
    num=randint(0, 1000)
    lista1.append(num)

def obtenerElementoMayor(lista):
    mayor=lista[0]
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

def obtenerElementoMenor(lista):
    menor=lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor

def sumaNumeros(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

def mediaNumeros(lista):
    return sumaNumeros(lista)/numeros
        
def sustituirElemento(lista, numeroSustituir, valorCambio):
    for i in range(len(lista)):
        if numeroSustituir==lista[i]:
            lista[i]=valorCambio
    return valorCambio

def mostrarNumeros(lista):
    listaNum=[]
    for i in range(len(lista)):
        listaNum.append(lista1[i])
    return listaNum


print("a.",obtenerElementoMayor(lista1))
print("b",obtenerElementoMenor(lista1))
print("c",sumaNumeros(lista1))
print("d",mediaNumeros(lista1))
print("e",sustituirElemento(lista1, 6, 18))
print("f",mostrarNumeros(lista1))
