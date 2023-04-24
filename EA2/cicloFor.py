rango = range(5) # del 0 (por defecto) al 4
for numero in rango:
    print("Número: ", numero)

print("\n**** inicia desde el 4 ****")
rango = range(4, 10) # del 4... al 9
for numero in rango:
    print("Número: ", numero)

print("\n**** Aumento de más de 1 ****")
rango = range(0, 10, 2) # aumenta de 2
for numero in rango:
    print("Número: ", numero)

palabra = "Alejandro"
for letra in palabra:
    print(letra)