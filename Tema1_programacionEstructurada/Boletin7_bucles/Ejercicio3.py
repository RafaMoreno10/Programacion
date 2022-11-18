'''
Created on Oct 21, 2022

@author: estudiante
'''
num=int(input("Introduce un numero: "))

tipo=()
PosNeg=()

while num!=0:
    if num%2==0:
        tipo="Par"
    else:
        tipo="Impar"
    if num>0:
        PosNeg="Positivo"
    else:
        PosNeg="Negativo"
    print("El numero %s, es %s, %s y su cuadrado es %s" %(num, tipo, PosNeg, num**2))
    num=int(input("\nIntroduce un numero: "))
print("Programa terminado.")
        