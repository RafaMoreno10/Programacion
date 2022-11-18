'''
Created on Oct 18, 2022

@author: estudiante
'''
fecha= input ("Introduzca una fecha en formato dd-mm-yyyy")
hemisferio= input("Introduzca el hemisferio (Norte/Sur)").upper()

day = int(fecha[0:2])
month = int(fecha[3:5])
year = int(fecha[6:10])

if (month==10 or month==11) or (23<=day<=31 and month==9) or (month==12 and 1<=day<=21):
    if hemisferio =="NORTE":
        print("Es otono")
    elif hemisferio == "SUR":
        print("Es primavera")
        
elif (month==4 or month==5) or (21<=day<=31 and month==3) or (month==6 and 1<=day<=21):
    if hemisferio =="NORTE":
        print("Es primavera")
    elif hemisferio == "SUR":
        print("Es Otono")
        
elif (month==1 or month==2) or (21<=day<=31 and month==12) or (month==3 and 1<=day<=21):
    if hemisferio =="NORTE":
        print("Es invierno")
    elif hemisferio == "SUR":
        print("Es verano")
        
elif (month==7 or month==8) or (21<=day<=31 and month==6) or (month==9 and 1<=day<=21):
    if hemisferio =="NORTE":
        print("Es verano")
    elif hemisferio == "SUR":
        print("Es invierno")
        