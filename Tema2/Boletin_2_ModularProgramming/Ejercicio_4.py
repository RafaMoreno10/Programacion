'''
Created on 28 Nov 2022

@author: estudiante
'''
def getDayOfWeek(dia, mes, anho):
    a=(14-mes)//12
    
    y=anho-a
    
    m=mes+12*a-2
    
    return(int(dia+y+y//4-y//100+y//400+(31*m)//12)%7)

nameOfDays=["Sabado", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
dia=1
while dia>0:
    dia=int(input("Introduce el numero de un dia: "))
    if dia>31:
        dia=int(input("Introduce el numero de un dia: "))

    month=int(input("Introduce el numero del mes: "))
    year=int(input("Introduce el numero del año: "))
    if dia>0:
        mensaje=nameOfDays[getDayOfWeek(dia, month, year)]
        
    else:
        mensaje:"No es posible introducir estos valores"
        
    if [getDayOfWeek(dia, month, year)]>[getDayOfWeek(28, 11, 2022)]:
        print("Ese dia será",mensaje)
    else:
        print("Ese dia era",mensaje)