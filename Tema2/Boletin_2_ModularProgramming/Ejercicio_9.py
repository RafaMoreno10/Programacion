'''
Created on 28 Nov 2022

@author: estudiante
'''
def isPrime(numero):
    is_prime=True
    
    for i in range(2, numero):
        if numero%i==0:
            is_prime=False
   
        
    return is_prime

def getPrimeDivisors(numero):
    divisors=[]
    contador=0
    alberto=1
    if numero<0:
        divisors=None
    else:
        if isPrime(numero):
            divisors=[1, numero]
        else:
            while contador<=2:
                if isPrime(alberto) and numero%alberto==0:
                    divisors.append(alberto)
                    contador+=1
                alberto+=1
        
    return divisors

numero=int(input("Introduce un numero: "))
print(getPrimeDivisors(numero))