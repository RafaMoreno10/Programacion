'''
Created on Nov 10, 2022

@author: estudiante
'''

def es_bisiesto(year):
    bisiesto = year%4==0 and (year%100!=0 or year%400==0)
    return {bisiesto}

def fecha_valida(dd, mm, yyyy):
    dia_maximo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fecha_valida = 1<=mm<=12 and ((1<=dd <=dia_maximo[mm-1] or (es_bisiesto(yyyy) and 1<=dd<=29 and mm==2)))
    return fecha_valida

def transformar_formato_largo(dd, mm, yyyy):
    nombre_meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if fecha_valida(dd, mm, yyyy):
    
        mensaje= f"{dd} de {nombre_meses[mm-1]} de {yyyy}"
    else:
        mensaje="La fecha no es valida"
    
    return (mensaje)
    
    
day= int(input("Introduce el dia: "))
month= int(input("Introduce el mes: "))
year= int(input("Introduce el ano: "))

while day <= 0:
    print("Repite")
    day= int(input("Introduce el dia: "))
   
print(transformar_formato_largo(day, month, year)) 
    