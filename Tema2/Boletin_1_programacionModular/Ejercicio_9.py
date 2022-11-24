'''
Created on Nov 22, 2022

@author: estudiante
'''
def es_mayor(lista):
    mayores=[]
    juan=3
    for i in range(len(lista)+2):
        if i>juan:
            mayores.append(i)
    return mayores

def es_menor(lista):
    menores=[]
    juan=3
    for i in range(len(lista)+2):
        if i<juan:
            menores.append(i)
    return menores

def es_multiplo(lista):
    multiplos=[]
    juan=3
    for i in range(len(lista)+2):
        if i%juan==0:
            multiplos.append(i)
    return multiplos

manolo=[1, 2, 4, 5, 6, 7, 8, 9]
print(es_mayor(manolo))
print(es_menor(manolo))
print(es_multiplo(manolo))