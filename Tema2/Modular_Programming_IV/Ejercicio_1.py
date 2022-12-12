'''
Created on 8 dic 2022

@author: rafam
'''


print("######## GMAIL #########")
print("1. Iniciar sesion")
print("2. Crear usuario")
print("3. Visualizar usuarios guardados")
print("4. Salir de Gmail")
print("########################")

usuarios=[]
contrasenas=[]

contador=0
bloqueo=False
opcion=int(input("\nIntroduzca una opcion: "))
while 0>opcion>5:
    opcion=int(input("\nIntroduzca una opcion valida: "))

while opcion!=4 and bloqueo==False:
    if opcion==1:   
        usua=input("\nIntroduce tu usuario: ")
        if usua not in usuarios:
            print("No estas en la BBDD. Escoge la opcion 2")
        else:
            contra=input("Introduzca tu contrasena: ")
            if contra not in contrasenas:
                cont=0
                while cont<3:
                    contra=input("Introduzca tu contrasena: ")
                    cont+=1
                    if cont==3:
                        bloqueo=True
        opcion=int(input("Introduzca una opcion: "))
    elif opcion==2:
        if len(usuarios)<10:
            print("Bienvenido a Gmail, registrese")
            usua=input("Introduce tu nuevo usuario: ") 
            while usua in usuarios:
                cont=0
                while cont<3:
                    usua=input("Introduce de nuevo tu usuario")
                    cont+=1
                    if cont==3:
                        print("Demasiados intentos, vuelva al menu.") 
                        print("######## GMAIL #########")
                        print("1. Iniciar sesion")
                        print("2. Crear usuario")
                        print("3. Visualizar usuarios guardados")
                        print("4. Salir de Gmail")
                        print("########################")
                        opcion=int(input("\nIntroduzca una opcion: "))
            contra=input("Introduce tu contrasena")
            contra2=input("Intoduce otra vez su contrasena")
            if contra!=contra2:
                cont=0
                print("Las contrasenas no coinciden")
                cont+=1
                contra2=input("Intoduce otra vez su contrasena")   
                if cont==3:
                    print("Demasiados intentos, vuelva al menu.") 
                    print("######## GMAIL #########")
                    print("1. Iniciar sesion")
                    print("2. Crear usuario")
                    print("3. Visualizar usuarios guardados")
                    print("4. Salir de Gmail")
                    print("########################")
                    opcion=int(input("\nIntroduzca una opcion: "))
            
            else:
                usuarios.append(usua)
                contrasenas.append(contra)
                opcion=int(input("\nIntroduzca una opcion"))
        else:
            print("Ocupacion maxima de usuarios, vuelva en otro momento.")
            opcion=4
 
    elif opcion==3:
        print(usuarios)
        opcion =int(input("Elija opcion: "))
 
if bloqueo==True:
        print("Estas bloqueado maquinote")
    
if opcion==4:
    print("Has salido de Gmail.")    

    