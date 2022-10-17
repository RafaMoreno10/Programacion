#En el gimnasio Jacafitness tienen el siguiente horario: Los Lunes, Miércoles y Viernes imparten Spinning de 12 a 14, Yoga de 16 a 20 y Body combat de 20 a 22; Los Martes y Jueves La sesión de Spinning 
#y Yoga se intercambian.
#Elabora un programa que dé la bienvenida al gimnasio Jacafitness y tras preguntar por la hora y el día de la semana te indique la actividad que puedes realizar.

nombre=str(input("Cual es su nombre?: "))
print("Bienvenidos al gimnasio Jacafitness,",nombre)
dia=str(input("Que dia de la semana asistiras?: ").upper())
hora=int(input("A que hora asistiras al gimnasio?: "))

   
if (dia=="LUNES" or dia=="MIERCOLES" or dia=="VIERNES") and (12<=hora<=14):
    print("Puedes realizar Spinning")
elif (dia=="LUNES" or dia=="MIERCOLES" or dia=="VIERNES") and (16<=hora<=20):
    print("Puedes realizar Yoga")
elif (dia=="LUNES" or dia=="MIERCOLES" or dia=="VIERNES") and 20<=hora<=22:
    print("Puedes realizar Body Combat")
elif (dia=="MARTES" or dia=="JUEVES") and (12<=hora<=14):
    print("Puedes realizar Yoga")
elif (dia=="MARTES" or dia=="JUEVES") and 16<=hora<=20:
    print("Puedes realizar Spinning")
elif (dia=="MARTES" or dia=="JUEVES") and 20<=hora<=22:
    print("Puedes realizar Body Combat")
elif (dia=="SABADO" or dia=="DOMINGO"):
    print("Los fines de semana no abrimos el gimnasio, perdone las molestias.")
else:
    print("A esa hora no hay clases o se encuentra cerrado el gimnasio")  