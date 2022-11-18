'''
Created on Nov 4, 2022

@author: estudiante
'''
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
        