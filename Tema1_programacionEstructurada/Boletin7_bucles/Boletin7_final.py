'''
Created on 3 nov 2022

@author: rafam
'''
ano = int(input(" Introduce un a�o al que calcular:"))
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
        
print(f" {ano} a�os => {totalPuzzles} puzzles y {totalDinero}�")


print("---")
#Ejercicio7
numero = int(input(" Numero: "))
a = []
for i in range (numero):
    a.append(numero)
    print(*a)     
    
#Ejercicio8

numero = int(input(" Tamano: "))
tipo = input(" Que figura quires? (Cuadrado, triangulo, rombo): ").upper().strip()

if tipo==("CUADRADO" or "TRIANGULO" or "ROMBO"):
    if "CUADRADO":
        for i in range(numero):
            print("*"*numero)
        
    elif "TRIANGULO":
        for i in range (numero):
            print((" " * ((numero - i) - 1)) + ("*" * (1 + i * 2)))
            
    elif "ROMBO":
        k = 0
        for i in range (numero):
            print((" " * ((numero - i) - 1)) + ("*" * (1 + i * 2)))
            
            k = (i * 2) - 1
            
        for i in range(numero):
            print ((" " * (1 + i)) + ("*" * (k - i * 2)))
            
    else:
        print(" Figura incorrecta")
 
 
 
#Ejercicio9       
tipo = input(" Que figura sin interior quieres? (Cuadrado, triangulo, rombo): ").upper().strip()
numero = int(input(" De que tamano quieres la figura?: "))

if tipo==("CUADRADO" or "TRIANGULO" or "ROMBO"):
    if "CUADRADO":
        for i in range(numero):
            if i==0 or i==numero-1:
                print("*"*numero)
            else:
                print("*"+" "*(numero - 2)+"*")
               
    elif "TRIANGULO":
        
        k=0
        for i in range (numero):
            
            if i==numero-1:
                print("*"*(k + 2))
            elif i==0:
                print((" " *((numero - i) - 1))+("*"))
            else: 
                print((" "*((numero - i)-1)) + ("*") + (" " * (-1 + i * 2)) + ("*"))
                k=(1 + i * 2)
            
    elif "ROMBO":
        
        k=0 
        for i in range (numero):
            
            if i == 0:
                print((" " * ((numero - i) - 1)) + ("*"))
            else: 
                print((" " * ((numero - i) - 1)) + ("*") + (" " * (-1 + i * 2)) + ("*"))
                k = (i * 2 - 1)
            
        for i in range(numero - 1):
            
            if i == numero - 2:
                print((" " * (1 + i)) + ("*"))
            else:
                print((" " * (1 + i)) + ("*") + (" " * (k - i * 2 - 2)) + ("*"))
                
    else:
        print(" Figura incorrecta")
        
#Ejercicio10

tipo = input(" Que figura hueca quires hueca? (Cuadrado, triangulo, rombo): ").upper().strip()
numero = int(input(" De que dimension quiere la figura?: "))
simbolo = input(" Caracter con el que hacer la figura: ").strip()

if tipo==("CUADRADO" or "TRIANGULO" or "ROMBO"):
    if "CUADRADO":
        for i in range(numero):
            if i == 0 or i == numero - 1:
                print(simbolo * numero)
            else:
                print(simbolo + " "*(numero - 2) + simbolo)
               
    elif "TRIANGULO":
        
        k = 0
        for i in range (numero):
            
            if i == numero - 1:
                print(simbolo * (k + 2))
            elif i == 0:
                print((" " * ((numero - i) - 1)) + (simbolo) + (" " * ((numero - i) - 1)))
            else: 
                
                print((" " * ((numero - i) - 1)) + (simbolo) + (" " * (-1 + i * 2)) + (simbolo) + (" " * ((numero - i) - 1)))
                k = (1 + i * 2)
            
    elif "ROMBO": 
        
        k = 0 
        for i in range (numero):
            
            if i == 0:
                print((" " * ((numero - i) - 1)) + (simbolo) + (" " * ((numero - i) - 1)))
            else: 
                print((" " * ((numero - i) - 1)) + (simbolo) + (" " * (-1 + i * 2)) + (simbolo) + (" " * ((numero - i) - 1)))
                k = (i * 2 - 1)
            
        for i in range(numero - 1):
            
            if i == numero - 2:
                print((" " * (1 + i)) + (simbolo) + (" " * (1 + i)))
            else:
                print((" " * (1 + i)) + (simbolo) + (" " * (k - i * 2 - 2)) + (simbolo) + (" " * (1 + i)))
                
    else:
        print(" Figura incorrecta")
        
