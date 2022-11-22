'''
Created on 22 nov 2022

@author: rafam
'''
def convertirBinario(cadena):
    b=0
    invertida=cadena[::-1]
    for i in range(len(invertida)):
        b+=(2 ** i) * (int(invertida[i]))
    return b

def convertirDecimal(numero):
    result=""
    divisor=2
    dividendo=numero
    while dividendo>=1:
        resto=dividendo%divisor
        dividendo=dividendo//divisor
        result=str(resto)+result
    return result

numeroBin=input("Introduce numero binario: ")
for i in range(len(numeroBin)):
    while str(numeroBin[i]) != "0" and str(numeroBin[i]) != "1":
        numeroBin=input("El numero introducido no es valido, introduce un numero binario: ")
        
print(f"El numero {numeroBin} en decimal es {convertirBinario(numeroBin)}")

numDec=int(input("Introduzca un numero decimal:"))
while numDec<0:
    numDec=int(input("No valido, Introduzca un numero decimal:"))
    
print(f"El numero {numDec} en decimal es {convertirDecimal(numDec)}")