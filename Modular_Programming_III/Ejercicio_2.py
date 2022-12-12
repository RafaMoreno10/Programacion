'''
Created on 9 dic 2022

@author: rafam
'''
'''
 Design a function called lowCaseInString that has a string of characters as parameter,
the method should return how many of those characters are lowercase letters.
'''

letras="abcdefghijklmnopqrstuvxyz"
mayus=letras.upper()
minus=letras.lower()
def lowCaseInString(cadena):
    cantidad=0
    for i in cadena :
        if i in minus:
            cantidad+=1
    return cantidad

assert(lowCaseInString("SaNdra tieNe LA CABeza Mal"))
assert(lowCaseInString("JUAN ESTA EN SEVILLA"))