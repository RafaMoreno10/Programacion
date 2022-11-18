'''
Created on 17 oct 2022

@author: rafam
'''
#ejercicio7
cantidad=int(input("How many numbers do u want input?: "))

while cantidad<=0:
    print("The number is not valid, it should be greater than 0")
    cantidad= int(input("How many numbers do u want input?: "))
    
total, contador= 0, 0
while contador<cantidad:
    numero=int(input("Enter one number greater than 0: "))
    while numero<=0:
        numero=int(input("The number is not valid. Enter one number greater than 0: "))
    contador+=1
    total+=numero
            
print(f"The medium is {total/cantidad}")