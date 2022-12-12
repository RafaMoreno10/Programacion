'''
Created on 9 dic 2022

@author: rafam

Design a function called numberInString that receives a string of characters as
parameter and returns how many of them are numbers
'''
numeros="1234567890"
def numberCaseInString(cadena):
    cantidad=0
    for i in range(len(cadena)) :
        if cadena[i] in numeros:
            cantidad+=1
    return cantidad

assert(numberCaseInString("SaNdra tieNe 2 perros y 5 gatos"))
assert(numberCaseInString("JUAN ESTA EN SEVILLA y hace 47 grados, fresquito"))
