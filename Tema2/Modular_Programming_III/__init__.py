VOCALES="aeiou"
CONSONANTES="qwrtypsdfghjklzxcvbnm"
ESPACIO=" "
def desordena_palabra(cadena):
    cadena_final=""
    cadena=cadena.lower()
    for i in range(len(cadena)):
        if cadena[i] in VOCALES:
            cadena_final+="e"
        elif cadena [i] in CONSONANTES:
            cadena_final+=cadena[i]
        elif cadena [i] in ESPACIO:
            cadena_final+=cadena[i]
            
            
    return cadena_final 

assert(desordena_palabra("Me mata el pino de repente"))