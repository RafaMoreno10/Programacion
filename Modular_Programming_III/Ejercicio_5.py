'''
Created on 9 dic 2022

@author: rafam

Design a function called palindrome that has a string of characters as input parameter,
and returns True if it is a palindrome or False in other cases. A word is a palindrome if it
can be read the same from left to right or right to left, ignoring whites. For example:
"anilina" or "Dabale arroz a la zorra el abad" To simplify the problem, you can assume
that simple characters are used, that is, without tildes or diresis.
'''
#Esta funcion se utiliza para quitar los espacios entre palabra y palabra para que sea leida correctamente

def quitarEspacios(cadena):
    noSpaces=""
    
    for i in range(len(cadena)):
        if cadena[i]!=" ":
            noSpaces+=cadena[i]
    return noSpaces

#Esta funcion se utiliza para darle la vuelta a cadena y poder compararlas

def reverse(cadena):
    stringRever=""
    
    for i in cadena:
        stringRever=i+stringRever
    return stringRever

def palindrome(cadena):
    resul=False 
    
    if " " in cadena:
        cadena=quitarEspacios(cadena)
    
    
    cadenaAlReves=reverse(cadena)
    if cadena.upper()==cadenaAlReves.upper():
        resul=True 
    return resul

assert(palindrome("Dabale arroz a la zorra el abad"))
assert(palindrome("Ana"))
assert(palindrome("Anilina"))
assert(palindrome("Juan"))