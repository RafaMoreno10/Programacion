'''
Creado en 22 de Septiembre
@author: Rafael Moreno Barea
'''

#Ejercicio1
print(7>=27 and not (7<=2))
print(24>5 and 10<=10 or 10==5)
print((10>=15 or 23==13) and not(8==8))
print(not (6/3>3) or 7>7)

#Ejercicio2

print(27%4 + 15/4)
print(37//4^2-2)
print(9*2/3*10*3)
print((7*3-4*4)^2//4*2)

#Ejercicio3A
resultado=True
precio=int(input("¿Que precio tiene el articulo?: "))

if precio>=60 and precio>=420:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Ejercicio3B
resultado=True
numero=int(input("Introduce un numero: "))

if precio%2!=0:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Ejercicio3C
resultado=True
saldo=int(input("¿Cuanto dinero tienes en la cuenta? "))
dineroSacar=int(input("¿Cuanto dinero quieres sacar? "))

if dineroSacar>=0 and dineroSacar<=saldo:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Ejercicio3D
resultado=True
hora=int(input("¿Que hora es? "))
minutos=int(input("¿Y cuantos minutos? "))

if hora>=0 and hora<=23 and minutos>=0 and minutos<=59:
    resultado
else:
    resultado=False
print(resultado)

print("----------")

#Ejercicio3E
resultado=False
estadoCivil=input("¿Que estado civil tienes? ")

if estadoCivil==("S") or estadoCivil==("C") or estadoCivil==("V") or estadoCivil==("D"):
    resultado
else:
    resultado=True
print(resultado)

print("----------")

#Ejercicio4A
resultado=False
cantidad=int(input("¿Que cantidad de dinero quires sacar?"))

if cantidad>=300 or cantidad<0:
    resultado
else:
    resultado=True
print(resultado)

print("----------")

#Ejercicio4B
resultado=False
edad=int(input("¿Que edad tienes?"))

if edad>=16 or edad<=22:
    resultado
else:
    resultado=True
print(resultado)

print("----------")

#Ejercicio4C
resultado=False
respuesta=input("¿Eres hombre?: ")

if respuesta==("S") or respuesta==("N"):
    resultado
else:
    resultado=True
print(resultado)

print("----------")

#Ejercicio4D
resultado=False
numero=int(input("Introduce un numero"))

if numero%7==0 or numero%3==0:
    resultado
else:
    resultado=True
print(resultado)

print("----------")



#Ejercicio5#
A=True
B=True

print("Para A=", A, " y B=", B)
print("(A or B) and not (A) =", (A or B) and not (A))
print("not (A or B) and B =", not (A or B) and B)
print("A or not (B) =", A or not (B))
print("not((A and B) and (B or A)) =", not((A and B) and (B or A)))

A=True
B=False

print("Para A=", A, " y B=", B)
print("(A or B) and not (A) =", (A or B) and not (A))
print("not (A or B) and B =", not (A or B) and B)
print("A or not (B) =", A or not (B))
print("not((A and B) and (B or A)) =", not((A and B) and (B or A)))

A=False
B=False

print("Para A=", A, " y B=", B)
print("(A or B) and not (A) =", (A or B) and not (A))
print("not (A or B) and B =", not (A or B) and B)
print("A or not (B) =", A or not (B))
print("not((A and B) and (B or A)) =", not((A and B) and (B or A)))

A=False
B=True

print("Para A=", A, " y B=", B)
print("(A or B) and not (A) =", (A or B) and not (A))
print("not (A or B) and B =", not (A or B) and B)
print("A or not (B) =", A or not (B))
print("not((A and B) and (B or A)) =", not((A and B) and (B or A)))

