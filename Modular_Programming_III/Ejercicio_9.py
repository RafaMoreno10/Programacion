'''
Created on 12 dic 2022

@author: rafam
'''
VOCALES="aeiou"
CONSONANTES="qwrtypsdfghjklzxcvbnm"

def desordena_palabra(cadena):
    cadena_final=""
    cadena=cadena.lower()
    for i in range(len(cadena)):
        if cadena[i] in CONSONANTES:
            cadena_final+=cadena[i]
    for i in range(len(cadena)):
        if cadena[i] in VOCALES:
            cadena_final+=cadena[i]
    return cadena_final 

assert(desordena_palabra("Vaya sorpresa Marruecos"))
assert(desordena_palabra("Me mata el pino de repente"))