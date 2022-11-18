'''
Created on Nov 17, 2022

@author: estudiante
'''
listaPiezas1=[5,3]
listaPiezas2=[2,4]

def encajan(listaPiezas1, listaPiezas2):
    encajan=True 
    if listaPiezas1[0]== listaPiezas2[0] or listaPiezas1[1]==listaPiezas2[0] or listaPiezas1[0] == listaPiezas2[1] or listaPiezas1[1]==listaPiezas2[1]:
        encajan= encajan 
    else:
        encajan=False 
    return encajan 
print(encajan(listaPiezas1, listaPiezas2))