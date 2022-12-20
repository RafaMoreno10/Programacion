'''
Created on 20 dic 2022

@author: rafam
'''

primos=[2,3,5,7,11,13,17]
def divisores(numero):
    divsion=[]
    contador=0
    
    while numero!=1:
        resto=numero%primos[contador]
        if resto==0:
            numero=numero//primos[contador]
            divsion.append(primos[contador])
        else:
            contador+=1
    return divsion
    
print(divisores(104)) 