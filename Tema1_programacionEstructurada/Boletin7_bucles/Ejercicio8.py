'''
Created on Nov 4, 2022

@author: estudiante
'''
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
