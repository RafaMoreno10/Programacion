'''
Created on 28 Nov 2022

@author: estudiante
'''

nameMonth=["Enero", "Febrero", "Mar<o", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Deciembre"]
def isLeapYear(yyyy):
    return yyyy%4==0 and (yyyy%100!=0 or yyyy%400==0)


def computeDaysInMonth(mm, yyyy):
    maxDaysMonth=31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    if mm==2 and isLeapYear(yyyy):
        maxDaysMonth=29
            
    else:
        maxDaysMonth=maxDaysMonth[mm-1]
        
    return maxDaysMonth

month=1
while month>0:
    month=int(input("Introduce un mes(mm): "))
    
    year=int(input("Introduce un año(yyyy): "))

    if month<=0 or year<=0:
        mensaje=-1
    else:
        mensaje=f"El mes de {nameMonth[month-1]} del {year}, tiene {computeDaysInMonth(month,year)} dias"
        
    print(mensaje)