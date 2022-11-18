'''
Created on 17 oct 2022

@author: rafam
'''
numero=int(input("Dame un numero entre el 0 y el 10: "))
if numero<=0 or numero>10:
    print("NO PUEDES INTRODUCIR UN NUMERO MAYOR A 10 O MENOR QUE 0")
else:
    for x in range (1,11):
        print (numero,"x",x,"=",numero *x)