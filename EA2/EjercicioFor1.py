# Ingresar por teclado 5 números enteros, luego debe indicar:
# Cuántos números son mayores a cero
# Cuántos números son menores a cero
# Cuántos números son iguales a cero
mayoresACero = 0
menoresACero = 0
igualesACero = 0
rango = range(5)
for indice in rango:
    numero = int(input(f"Ingrese número {(indice+1)} : "))

    if numero > 0:
        mayoresACero += 1 # contador
    elif numero < 0:
        menoresACero += 1
    else:
        igualesACero += 1
    
    
print("Cantidad de mayores a cero: ", mayoresACero)
print("Cantidad de menores a cero: ", menoresACero)
print("Cantidad de iguales a cero: ", igualesACero)

      