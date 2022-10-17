'''
Created on Sep 28, 2022

@author: estudiante
'''

#Realizar un programa que lea un nÃºmero entero por teclado e informe de si
#el nÃºmero es par o impar (el cero se considera par).

numero=int(input("Introduce un numero: "))

if numero==0 or numero%2==0:
    print("El numero seleccionado es par")
else:
    print("El numero seleccionado es impar")
    
print("-----")

#Realizar un programa que solicite dos nÃºmeros por teclado e imprima en
#pantalla si son iguales, el primero mayor que el segundo o el primero mÃ¡s
#pequeÃ±o que el segundo.

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce otro numero: "))

if numero1==numero2:
    print("Los numeros son iguales")
elif numero1>numero2:
    print("El numero %s es mayor que el numero %s" %(numero1, numero2))
elif numero < numero2:
    print("El numero %s es menor que el numero %s" %(numero1, numero2))

print("-----")
    
#Realizar un programa que lea un nÃºmero por teclado. El programa debe
#imprimir en pantalla un mensaje con â€œEl nÃºmero xx es mÃºltiplo de 2â€� o un
#mensaje con â€œEl nÃºmero xx es mÃºltiplo de 3â€�. Si es mÃºltiplo de 2 y de 3
#deben aparecer los dos mensajes. Si no es mÃºltiplo de ninguno de los dos
#el programa finaliza sin mostrar ningÃºn mensaje.   

numero=int(input("Introduce un numero: "))

if numero%3==0 and numero%2==0:
    print("El numero %s es multiplo de 2 y 3" %(numero))
    
elif numero%3==0 :
    print("El numero %s es multiplo de 3" %(numero))
    
elif numero%2==0 :
    print("El numero %s es multiplo de 2" %(numero))
else:
    print("Datos erroneos")
    
print("-----")
    
#Realizar un programa que lea la edad de una persona menor a 100 aÃ±os e
#informe de si es un nino (0-12 aÃ±os), un adolescente (13-17), un joven (18-
#29) o un adulto.

edad=int(input("Introduce tu edad: "))
   
if edad>=0 and edad<=12 and edad<100:
    print("Eres un nino")

elif edad>=13 and edad<=17 and edad<100:
    print("Eres un adolescente")

elif edad>=18 and edad<=29 and edad<100:
    print("Eres un joven")
    
elif edad>=30 and edad<100:
    print("Eres un adulto")
    
print("-----")
    
#Realizar un programa que solicite 4 nÃºmeros e imprima la media de los
#nÃºmeros. TambiÃ©n debe imprimir aquellos nÃºmeros que son superiores a la
#media.

print("Vamos a hacer la media de 4 numeros")
print()
numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero: "))
numero3=int(input("Introduce un numero: "))
numero4=int(input("Introduce un numero: "))


media=(numero1 + numero2 + numero3 + numero4)/4
print(media)

if numero1>media:
    print("El numero %s es mayor que la media" %(numero1))

if numero2>media:
    print("El numero %s es mayor que la media" %(numero2))

if numero3>media:
    print("El numero %s es mayor que la media" %(numero3))

if numero4>media:
    print("El numero %s es mayor que la media" %(numero4))
    
print("-----")
    

#Realizar un programa que solicite un carÃ¡cter por teclado e informe por
#pantalla si el carÃ¡cter es una vocal o no lo es. Si es una vocal mostrarÃ¡ el
#mensaje â€œEs la primera vocal (A)â€� o â€œEs la segunda vocal (E)â€�, etc.


print("Dime una letra y te dire si es vocal o consonante (En mayuscula)")
print()
letra=input("Introduce una letra: ")

    
if letra==("A"):
    print("Es la primera vocal A")

elif letra==("E"):
    print("Es la segunda vocal E")

elif letra==("I"):
    print("Es la tercera vocal I")

elif letra==("O"):
    print("Es la cuarta vocal O")

elif letra==("U"):
    print("Es la quinta vocal U")
    
else:
    print("La letra %s es una consonante" %(letra))

print("-----")


#Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
#Casado, V-Viudo y D-Divorciado) y su edad. DespuÃ©s debe mostrar por
#pantalla el porcentaje de retenciÃ³n que debe aplicÃ¡rsele de acuerdo con las
#siguientes reglas:
#A los solteros o divorciados menores de 35 aÃ±os, un 12%
#Todas las personas mayores de 50 aÃ±os, un 8.5%
#A los viudos o casados menores de 35 aÃ±os, un 11.3%
#Al resto de casos se le aplica un 10.5%

estadoCivil=input("Â¿Que estado civil tienes? (S-Soltero, C-Casado, V-Viudo y D-Divorciado)  ")
edad=int(input("Cuantos anos tienes? "))

if (estadoCivil==("S") or estadoCivil==("D")) and edad<35:
    print("Se le retiene un 12%")
elif edad>50:
    print("Se le retiene un 8'5%")
elif estadoCivil==("C") or estadoCivil==("V"):
    print("Se le retiene un 11'3%")
else:
    print("Se le retiene un 10'5%")

print("-----")
    

  

#Realizar un programa que lea por teclado dos marcaciones de un reloj
#digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
#23:59:59 e informe cual de ellas es mayor.

print("Te voy a decir que hora es mayor")

hora1=int(input("Hora1? "))
minutos1=int(input("Minutos1? "))
segundos1=int(input("Segundos1? "))
print("")
print("Ahora introduce la segunda hora")
hora2=int(input("Hora2? "))
minutos2=int(input("Minutos2? "))
segundos2=int(input("Segundos2? "))

if 0<=hora1<=23 and 0<=hora2<=23 and 0<minutos1<=59 and 0<minutos2<=59 and 0<segundos1<=59 and 0<segundos2<=59:
    if hora1<hora2:
            print("La hora 2 es mayor")
    elif hora2<hora1:
            print("La hora 1 es mayor")
    else:
        if minutos1<minutos2:
            print("La hora 2 es mayor")
        elif minutos1>minutos2:
            print("La hora 1 es mayor")
        else:
        
            if segundos1<segundos2:
                print("La hora 2 es mayor")
            elif segundos1>segundos2:
                print("La hora 1 es mayor")
            else:
                print("Las horas son iguales")
                
else:
    print("Los valores introducidos son erroneos")
    
print("-----")
    
   

#En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
#porcentaje de rebaja que se aplicará sobre el precio original del producto se
#calcula de la siguiente forma:
#Si el producto es de tipo A, independientemente de su precio se
#aplica un 7% de descuento.
#Si el producto es de tipo C o bien el precio es inferior a 500€ se
#aplicará un porcentaje del 12% de descuento.
#En el resto de casos se aplica un 9% de descuento.
#Realizar un programa que solicite los datos necesarios (tipo de producto y
#precio original) y calcule el precio rebajado. Debe comprobarse que los
#datos de entrada son correctos, y si no lo son mostrar un mensaje de error.


producto=input("Que tipo de producto quieres?(A, B o C): ")
precio_Original=int(input("Cual es el precio original del producto?: "))

if producto=="A" or producto=="B" or producto=="C":
    if producto=="A":
        print(precio_Original-(precio_Original*7/100))
    elif producto=="C" or precio_Original<500:
        print(precio_Original-(precio_Original*12/100))
    elif producto=="B" or precio_Original>=500:
        print(precio_Original-(precio_Original*9/100))
else:
    print("Los datos seleccionados no son correctos")
    
print("-----")
    
   
#Realizar un programa que lea un carácter y dos números enteros por
#teclado. Si el carácter leído es un operador aritmético, calcular la operación
#correspondiente, si es cualquier otro debe mostrar un error.
print("Esto es una calculadora que suma, resta, multiplica(*) o divide(/) dos numeros")
accion=input("Que accion quieres hacer?: ")
print()
print("Ahora introduciremos dos numeros")
numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce otro numero: "))

if accion=="+" or accion=="-" or accion=="*" or accion=="/" :
    if accion=="+":
        print("El resultado es",numero1+numero2)
    elif accion=="-":
        print("El resultado es",numero1-numero2)
    elif accion=="*":
        print("El resultado es",numero1*numero2)
    elif accion=="/":
        print("El resultado es",numero1/numero2)
else:
    print("Datos erroneos")
    
print("Fin del boletin")

   
    
    
    
    