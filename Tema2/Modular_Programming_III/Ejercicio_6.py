'''
Created on 11 dic 2022

@author: rafam
'''

def busca_palabra(cadena, palabra):
    palabra_final=""
    cadena=cadena.lower()
    palabra=palabra.lower()
    
    for i in range(len(cadena)):
        if palabra[i] in cadena:
            palabra_final+=palabra[i]
    return palabra_final
        
    


assert(busca_palabra("Me gustan los coches", "coCHes"))
assert(busca_palabra("shybaoxlna", "hola"))
assert(busca_palabra("soybaoxlna", "hola"))