'''
Created on 28 Nov 2022

@author: estudiante
'''
def isFriendNumber(numero, number2):
    divisors=0
    amigo=False
    for i in range(1, numero):
        if numero%i==0:
            divisors+=i
    
    if divisors==number2:
        amigo=True 
        
    return amigo 
numero=int(input("Introduce un numero: "))
number2=int(input("Introduce otro numero: "))

print(isFriendNumber(numero, number2))