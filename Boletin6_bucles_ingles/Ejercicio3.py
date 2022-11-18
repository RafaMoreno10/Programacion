'''
Created on 17 oct 2022

@author: rafam
'''
#Design a program that asks how many numbers the user wants to introduce. Then,
#the user would have to introduce the numbers one by one and the program should
#say if each one of the numbers is odd or even. If the user inputs 0 or a negative
#number, it is not valid, and the system should ask for another number.

cantidad=int(input("How many numbers do you want input?: "))
for numero in range(cantidad):
    numero=int(input("“Enter one number greater than 0: "))
    if numero<=0:
        print("The number is not valid, it should be greater than 0 ")
    else:
        if numero%2==0:
            print("The number ,numero, is even")
        if not numero%2==0:
            print("The number ,numero, is odd")