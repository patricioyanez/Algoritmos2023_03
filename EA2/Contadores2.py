print("*** Cuenta de números pares ***")
contador = 0

num1 = int(input("Ingrese 1er número: "))
if num1 % 2 == 0: # obtiene el resto donde 0 es par y 1 es impar
    contador = contador + 1
    
num1 = int(input("Ingrese 2do número: "))
if num1 % 2 == 0:
    contador = contador + 1
    
num1 = int(input("Ingrese 3er número: "))
if num1 % 2 == 0:
    contador = contador + 1
print("Cantidad de números pares ingresados: ", contador)