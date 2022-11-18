#Crea un programa que tras preguntar por dos números realice la división del mayor
#de ellos por el menor y muestre el resultado de la división, es decir, el cociente y el
#resto. Solo puedes utilizar la suma o la resta, pero no otras operaciones.

numA=int(input("Introduce un numero: "))
numB=int(input("Introduce otro numero: "))



if numA<numB:
    dividendo=numB
    divisor=numA
else:
    dividendo=numA
    divisor=numB
    
if dividendo==divisor:
    print("El cociente es 1 y el resto 0")
elif divisor==1:
    print("El cociente es %s y el resto 0"%(dividendo))

else:
    cociente=1
    while dividendo>divisor:
        dividendo=dividendo-divisor
        cociente+=1
        if divisor==dividendo:
            resto=0
            print("El cociente es %s y el resto es %s"%(cociente, resto))
        elif dividendo<divisor:
            cociente-=1
            print("El cociente es %s y el resto es %s"%(cociente, dividendo))