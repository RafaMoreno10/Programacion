'''
Created on 9 dic 2022

@author: rafam
'''
'''
Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters.
'''

def charactersInString(palabra, letra):
    cantidad=0
    for i in range(len(palabra)):
        if palabra[i]==letra:
            cantidad+=1
    return cantidad
assert(charactersInString("Arruabarrena era un gran portero del Fuenlabrada", "a"))
assert(charactersInString("de Kukutxumutxu es mi camiseta ", "u"))