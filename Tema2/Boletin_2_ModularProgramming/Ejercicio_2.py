'''
Created on 28 Nov 2022

@author: estudiante
'''
def isLeapYear(year):
    return (year%4==0) or (year%100!=0 and year%400==0)

year=int(input("Introduce un anho"))
while year>0:
    
    if isLeapYear(year)==True:
        print(year,"es un anho bisiesto")
    elif isLeapYear(year)==False:
        print(year,"no es un anho bisiesto")

    num=int(input("Introduce un numero"))
        