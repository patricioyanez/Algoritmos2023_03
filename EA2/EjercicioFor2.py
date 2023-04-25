# Ingrese por teclado 10 letras, 
# indique cuantas de ellas son vocales y cuántas son consonantes.
#

rango = range(10)
vocales = 0
consonantes = 0
for x in rango:
    letra = input("ingrese una letra: ")
#    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#        vocales += 1
#    elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
#        vocales += 1
#    else:
#       consonantes += 1

    if letra.lower() in ("a","e","i","o","u"):
        vocales += 1
    else:
        consonantes += 1
print("Vocales      : ", vocales)
print("Consonantes  : ", consonantes)  