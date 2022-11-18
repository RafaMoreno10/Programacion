'''
Created on Nov 8, 2022

@author: estudiante
'''
'''
lista = [7, 1, 3, 5]
lista.insert(0, lista[-1])
lista.pop(-1)
print(lista)
"DE ESTA FORMA SERIA MUCHO MAS RAPIDO"
'''
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17]

a_escribir = lista[0]
a_guardar = 0

for i in range(len(lista)):
    
    a_guardar = lista[(i+1)%len(lista)]
    lista[(i+1)%len(lista)]=a_escribir
    a_escribir = a_guardar
    print(lista)