'''
Created on Oct 21, 2022

@author: estudiante
'''
peso=float(input("Cuanto pesas?: "))

while peso>0:
    edad=int(input("Cuantos anos tienes?: "))
    vida=input("Que estilo de vida llevas? (Sedentaria, Activa or muy activa): ").upper()
    while (vida!="SEDENTARIA" and vida!="ACTIVA" and vida!="MUY ACTIVA") or (peso<10 or peso>180) or (edad<0 or edad>110):
        if vida!="SEDENTARIA" and vida!="ACTIVA" and vida!="MUY ACTIVA":
            print("Datos Erroneos")
            vida=input("Que estilo de vida llevas? (Sedentaria, Activa or muy activa): ").upper()   
        if peso<10 or peso>180:
            print("Datos Erroneos")
            peso=float(input("Cuanto pesas?: "))
        if edad<0 or edad>110:
            print("Datos Erroneos")
            edad=int(input("Cuantos anos tienes?: "))
            
    if (edad>70 and vida=="SEDENTARIA") or (peso>100) or (peso>74.4 and edad)>50:
            print("Le recomendamos ir al medico")
    else:
        print("No es urgente que acuda al médico si no tiene problemas de salud")
        peso=float(input("Cuanto pesas?: "))
            
print("El programa ha terminado.")
                
            
    
    