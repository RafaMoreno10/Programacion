#Debe ser Verdadera si el contenido de las variables enteras 
#sueldo_bruto y sueldo_neto es
#el adecuado para una retención del 22%.



sueldo_Bruto=int(input("Introduce su sueldo bruto: "))
sueldo_Neto=int(input("Introduce su sueldo neto: "))
retencion=int(sueldo_Bruto*22/100)
resultado=True

if sueldo_Neto>=retencion:
    resultado

if sueldo_Neto<retencion:
    resultado=False
print(resultado)


print("--------------")

#Debe ser Verdadera si el contenido de 
#la variable entera día es un valor válido para el mes
#de mayo.

resultado=True
dia=int(input("Introduce un dia de Mayo: "))

if dia>=1 and dia<=31 : 
    resultado
else:
    resultado=False
print(resultado)

print("------------")

#Debe ser Verdadera si el número contenido en 
#las variables enteras num1 y num2 son
#múltiplos de tres.
resultado=True
num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero numero: "))

if num1%3==0 and num2%3==0:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Debe ser Verdadera si la calificación 
#contenida en la variable real nota es un aprobado.

resultado=True
nota=int(input("¿Que nota ha sacado el alumno?: "))

if nota>=5:
    resultado
else:
    resultado=False
print(resultado)

print("----------")
#Debe ser Verdadera si la media de la 
#calificación contenida en las variables reales nota1,
#nota2 y nota3 es un aproblado.

resultado=True
nota1=int(input("Introduce la primera nota: "))
nota2=int(input("Introduce la segunda nota: "))
nota3=int(input("Introduce la tercera nota: "))

if ((nota1+nota2+nota3)//3)>=5:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Debe ser Falsa si alguna de las calificaciones 
#contenidas en las variables reales nota1, nota2
#y nota3 es un suspenso.

resultado=True
nota1=int(input("Introduce la primera nota: "))
nota2=int(input("Introduce la segunda nota: "))
nota3=int(input("Introduce la tercera nota: "))

if nota1<5 or nota2<5 or nota3<5:
    resultado
else:
    resultado=False
print(resultado)

print("----------")




    