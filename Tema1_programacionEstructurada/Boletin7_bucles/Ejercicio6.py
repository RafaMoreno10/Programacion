'''
Created on Nov 4, 2022

@author: estudiante
'''
ano = int(input(" Introduce un ano al que calcular:"))
incremento = float(input(" Incremento de dinero en: "))
eurosInicial = float(input(" Primera paga: "))

totalDinero=0
totalPuzzles=0

a=0
b=0
for n in range (1, ano + 1):
    
    if n % 2 != 0:
        totalPuzzles = totalPuzzles + (2 ** a)
        a += 1
    else:
        totalDinero = totalDinero + (eurosInicial + incremento * b)
        b += 1
        
print(f" {ano} anos => {totalPuzzles} puzzles y {totalDinero}€")