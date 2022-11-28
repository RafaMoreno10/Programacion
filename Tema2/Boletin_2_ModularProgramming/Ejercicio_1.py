'''
Created on Nov 24, 2022

@author: estudiante
'''

def computeFactorial(num):
    manolo=1
    if num<0:
        manolo=None
    else:
        for i in range(num):
            manolo*=i+1
    return manolo

num=int(input("Introduce un numero"))
while num>0:
    print("El factorial de",num,"es",computeFactorial(num))
    num=int(input("Introduce un numero"))



