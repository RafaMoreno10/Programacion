'''
Created on 9 dic 2022

@author: rafam

Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters.
'''

letras="abcdefghijklmnopqrstuvxyz"
mayus=letras.upper()
minus=letras.lower()
def upperCaseInString(cadena):
    cantidad=0
    for i in cadena :
        if i in mayus:
            cantidad+=1
    return cantidad

assert(upperCaseInString("SaNdra tieNe LA CABeza Mal"))
assert(upperCaseInString("JUAN ESTA EN SEVILLA"))