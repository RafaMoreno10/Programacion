numeros="1234567890"
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def dni_valido(dni):
    
    validez=True 
    for dig in dni[:8]:
        if dig in LETRAS:
            validez=False
            
    if dni[-1].upper() not in LETRAS and 8>(len(dni)>9):
        validez=False 
    
    if validez==True:
        numeros=len(dni[:8])
        division=int(numeros)%23
        letra=LETRAS[division]
        if letra==dni[-1]:
            validez=True 
            
assert(dni_valido("28847351S"))