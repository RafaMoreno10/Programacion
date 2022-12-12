'''
Created on 11 dic 2022

@author: rafam
'''
VOCALES="aeiou"

def buscar_vocales(palabra):
    total=[]
    acumulador=0
    
    for i in range(len(palabra)):
        if (palabra[i].lower() in VOCALES) and (palabra[i].lower() not in total):
            total.append(palabra[i].lower())
            acumulador+=1
    return acumulador
    
assert(buscar_vocales("patata"))
print("Hay",buscar_vocales("total"),"vocales diferentes")
assert(buscar_vocales("alberto"))