'''
Created on Sep 19, 2022

@author: Rafa Moreno
'''
'''
from Tema1_programacionEstructurada.Boletin1_operacionesBasicas import numero

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
print("Buenas, vamos a calcular la hipotenusa")
cateto1=int(input("Dime la longitud del primer cateto "))
cateto2=int(input("Dime la longitud del segundo cateto "))
hipotenusa=(cateto1*2)+(cateto2*2)
print("La longitud de la hipotenusa es",hipotenusa)

print("------")

#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print("Vamos a pasar de grados Celsius a grados Fahrenheit")
grados=int(input("Introduce los grados celsius: "))
grados_F=(grados*9/5)+32
print("%s grados Celsius son %s grados Fahrenheit" %(grados, grados_F))
print("--------")

#Calcular la media de tres números pedidos por teclado

print("Vamos a hacer la media de 3 numeros")
print()
numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce un numero: "))
numero3=int(input("Introduce un numero: "))

media=(numero1 + numero2 + numero3)/3
print(media)

print("------")
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
#cuanto deberá pagar finalmente por su compra.

compra=int(input("Cuanto cuesta el producto comprado?: "))
descuento=compra*15/100
precio_final=compra-descuento
print("El precio final es de %s euros"%(precio_final))

print("------")
#Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).
print("Vamos a calcular la distancia entre dos puntos")
numero1=int(input("Introduce el primer punto: "))
numero2=int(input("Introduce el segundo punto: "))
resultado=abs(numero1-numero2)
print("La distancia entre los puntos es de %s"%(resultado))
print("------")
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.

x1=int(input("Introduce el valor del primer punto en X: "))
y1=int(input("Introduce el valor del primer punto en Y: "))
print("El primer punto es %s,%s"%(x1,y1))
print()
x2=int(input("Introduce el valor del segundo punto en X: "))
y2=int(input("Introduce el valor del segundo punto en Y: "))
print("El segundo punto es %s,%s"%(x2,y2))
resultado=((x2-x1)**2+(y2-y2)**2)**(1/2)
print("La distancia entre los puntos es de %s"%(resultado))
print("------")
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?

numero=int(input("Introduce un numero: "))
raiz_cua=(numero)**(1/2)
raiz_cubi=(numero)**(1/3)
print("La raiz cuadrada de %s es %s y la raiz cubica es %s"%(numero, raiz_cua, raiz_cubi))
print("------")
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
#pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

print("Que cantidad de dinero tienes? Veamoslo")

monedas2=int(input("Cuantas monedas de dos euros tienes?: "))
monedas1=int(input("Cuantas monedas de un euros tienes?: "))
moneda50cent=int(input("Cuantas monedas de 50 centimos tienes?:"))
moneda20cent=int(input("Cuantas monedas de 20 centimos tienes?: "))
moneda10cent=int(input("Cuantas monedas de 10 centimos tienes?: "))

if monedas2<0 or monedas1<0 or moneda50cent<0 or moneda20cent<0 or moneda10cent<0:
    print("No puede haber monedas negativas")
else:

    euros=(2*monedas2)+(1*monedas1)
    centimos=(moneda50cent*50)+(moneda20cent*20)+(moneda10cent*10)
    
    if centimos<100:
        print("Tienes %s euros y %s centimos"%(euros, centimos))
    else:
        cents=centimos%100
        eur=euros+(centimos//100)
        print("Tienes %s euros y %s centimos"%(eur, cents))

print("------")
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
#exponente. Pueden ocurrir tres cosas:
#◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
#◦ El exponente sea 0, el resultado es 1.
#◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo

print("Vamos a calcular la potencia de un numero")
base=int(input("Cual es la base de su operacion?: "))
expon=int(input("Cual es el exponente de su operacion?: "))

if expon>0:
    print("El resultado es",base**expon)
elif expon==0:
    print("El resultado es 1")
else:
    print("El resultado es",1/(base**expon))
print("------")  
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
#lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
#cuenta los siguiente:
#◦ Si se cumple Pitágoras entonces es triángulo rectángulo
#◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
#◦ Si los 3 lados son iguales entonces es equilátero.
#◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.  

lado1=int(input("Cual es la dimension de su primer lado?: "))
lado2=int(input("Cual es la dimension de su segundo lado?: "))
lado3=int(input("Cual es la dimension de su tercer lado?: "))

if lado3==(lado1**2 + lado2**2)**1/2 or lado1==(lado2**2 - lado3**2)**1/2 or lado2==(lado3**2 - lado2**2)**1/2:
    print("Es un triangulo rectangulo")
elif lado1==lado2 or lado2==lado3 or lado2==lado3: 
    print("Es un triangulo equilatero")
elif lado1!=lado2 or lado2!=lado3 or lado2!=lado3:
    print("Es un triangulo escaleno")
else:
    print("Isoceles")
    
print("----------")

#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
#número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
#por 400.

ano=int(input("Que años quieres verificar si es/fue bisiesto?: "))

if ano%400 == 0:
    print("Es un año bisiesto")
elif ano%100 == 0:
    print("No es un año bisiesto")
elif ano%4 == 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
    
print("----------")

#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
#se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
#producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
#tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia


tipoUva=input("Que tipo de uva tienes (A o B)?: ").upper()
kilos=float(input("Introduce los kg de uvas entregada "))
precioInicial=int(input("Introduce los kg inicial "))
tamanoUva=int(input("Introduce en tipo de uva (1 o 2): "))

if tipoUva=="A" or tipoUva=="B" and tamanoUva==1 or tamanoUva==2:
    
    if tipoUva=="A" and tamanoUva==1:
        print("La ganancia final es de: ",(kilos*precioInicial)+(kilos*0.2))
    elif tipoUva=="A"and tamanoUva==2:
        print("La ganancia final es de: ",(kilos*precioInicial)+(kilos*0.3))
    elif tipoUva=="B"and tamanoUva==1:
        print("La ganancia final es de: ",(kilos*precioInicial)-(kilos*0.3))
    else:
        print("La ganancia final es de: ",(kilos*precioInicial)-(kilos*0.5))
else:
    print("Los datos son erroneos")
print("------")   
#. El director de una escuela está organizando un viaje de estudios, y requiere determinar
#cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
#servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada 
#alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
#número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
#autobuses y lo que debe pagar cada alumno por el viaje.

numeroAlu=int(input("Cuantos alumnos viajaran?: "))
        
if numeroAlu >=100:
    print("Se pagara",numeroAlu*65,"euros a la agencia y cada alumno paga 65€")
elif numeroAlu<100 and numeroAlu>=50:
    print("Se pagara",numeroAlu*65,"euros a la agencia y cada alumno paga 65€")
elif numeroAlu<50 and numeroAlu>=30:
    print("Se pagara",numeroAlu*65,"euros a la agencia y cada alumno paga 65€")
else:
    print("El autobus cuesta 4000 euros y cada alumno paga",(4000/numeroAlu),"€")
print("------")  
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
#es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
#los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
#décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
#es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
#determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

duracion=int(input("Introduce la duracion de la llamada(en minutos): "))
dia=str(input("Que dia de la semana es?: ").upper())
    
if duracion>10:
    precio=3
elif duracion>8:
    precio=2.5
elif duracion>5:
    precio=1.8
else:
    precio=1
    
if dia!="DOMINGO":
    horario=str(input("Se realizo la llamada por la mañana o por la tarde?: ").upper())
    if horario=="MAÑANA":
        impuesto=precio*0.15
    elif horario=="TARDE":
        impuesto=precio*0.1
    else:
        impuesto=0
else:
    impuesto=precio*0.03
    
if impuesto==0:
    print("El horario es incorrecto")
else:
    print("EL precio total es de",precio+impuesto,"€")
    
print("------")
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error.


dia=int(input("Introduce el dia de la semana con numero (1-7): "))

if dia>=1 and dia<=7:
    if dia==1:
        print("Es lunes")
    elif dia==2:
        print("Es martes")
    elif dia==3:
        print("Es miercoles")
    elif dia==4:
        print("Es jueves")
    elif dia==5:
        print("Es viernes")
    elif dia==6:
        print("Es sabado")
    else:
        print("Es domingo")
else:
    print("Los datos introducidos son erroneos")
print("------")   
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de
#días que tiene el mes correspondiente

print("Te dire los dias que tiene el mes que introduzcas")
mes=int(input("Introduzca el numero del mes: "))


if 0<mes<=12:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        print("El mes",mes,"tiene 31 dias.")
    elif mes==4 or mes==6 or mes==9 or mes==11:
        print("El mes",mes,"tiene 30 dias.")
    else:
        print("El mes de Febrero tiene 28 dias")
else:
    print("Los datos introducidos son incorrectos")

'''
print("------")


#EJERCICIO17



#EJERCICIO18
#Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
#inferior es mayor que el superior lo tiene que volver a pedir.
#A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
#el programa dará las siguientes informaciones:
#◦ La suma de los números que están dentro del intervalo (intervalo abierto).
#◦ Cuantos números están fuera del intervalo.
#◦ Informa si hemos introducido algún número igual a los límites del intervalo

inferior=int(input("Introduce el valor del limite inferior: "))
superior=int(input("Introduce el valor del limite superior: "))

numero=0
suma=0
fuera=0
igual=0

while inferior>=superior:
    inferior=int(input("No puede ser mayor que el limite superior, introduzca otro numero: "))

numero = int(input("Introduzca un numero entre %s y %s : "%(inferior, superior)))
while numero!=0:
   
    if numero!=0:
        if inferior < numero < superior:
            suma+=numero
        elif numero < inferior or numero >superior:
            fuera+=1
        else:
            igual+=1

        numero = int(input("Introduzca un numero entre %s y %s : "%(inferior, superior)))

print("La suma de los numero del intervalo es %s, fuera del intervalo hay %s numeros"%(suma, fuera))
if igual:
    print("Existe %s numeros que coinciden cin los limites del intervalo"%(fuera))


#EJERCICIO20
#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
#segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
#cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.

meses=20
pago=10
apagar=0
mes=0
while meses!=0:
    apagar+=pago
    pago=pago*2
    mes+=1
    print("El mes",mes, "pagaras %s euros." %(pago))
    meses-=1  
    
#EJERCICIO21
# Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
#números primos que queremos mostrar              





'''
print("Fin del boletin.")
'''