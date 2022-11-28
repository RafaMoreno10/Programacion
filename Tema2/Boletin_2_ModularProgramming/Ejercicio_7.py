'''
Created on 28 Nov 2022

@author: estudiante
'''
def isPrime(number):
    is_prime=True
    if number>0:
        for i in range(2, number):
            if number%i==0:
                is_prime=False
    else:
        is_prime=None
        
    return f"{number} es primo? {is_prime}"

number=int(input("Introduce un numero: "))
while number>0:
    print(isPrime(number))
    number=int(input("\nIntroduce un numero: "))
    

