'''
Created on 12 dic 2022

@author: rafam
'''
LETRAS="qwertyuiopasdfghjklzxcvbnm"


def contar_palabras(cadena):
    contador=0
    cadena=cadena.lower()
    if cadena[0] in LETRAS:
            contador+=1
    for i in range(len(cadena)):
        if cadena[i]==" " and cadena[i-1] in LETRAS:
                contador+=1
    return contador

assert(contar_palabras(" Hola   buenas tardes "))
assert(contar_palabras("He comido mucho"))
assert(contar_palabras("He comido   mucho"))
assert(contar_palabras(" AYer Gano  Espana"))