
numeros="1234567890"
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
LONGITUD_MINIMA = 8
LONGITUD_MAXIMA = 9

def dni_valido(dni):
    
    son_numeros=True
    for num in dni[:-1]:
        if num not in numeros:
            son_numeros=False 
    
    longitud_valida=LONGITUD_MINIMA<=len(dni)<=LONGITUD_MAXIMA
    ultima_letra=dni[-1].upper() in LETRAS
    letra_valida= son_numeros and LETRAS[int(dni[:-1])%int(len(23))]==dni[-1].upper()
    return son_numeros and longitud_valida and ultima_letra and letra_valida

assert(dni_valido("11111111H"))
            
        