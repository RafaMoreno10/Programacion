'''
Created on 28 Nov 2022

@author: estudiante
'''
def powerIt(base, exponent=0):
    return base**exponent

base=int(input("Introduce la base de la operacion: "))
exponent=int(input("Introduce el exponente de la operacion: "))
print("La solucion es",powerIt(base, exponent))