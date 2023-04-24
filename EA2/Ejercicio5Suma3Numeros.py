print("==== Suma de 3 números ====")
n1 = int(input("Ingrese el 1er número: "))
n2 = int(input("Ingrese el 2do número: "))
n3 = int(input("Ingrese el 3er número: "))

total = 0
contador = 0
if n1 > 0 and n1 % 2 == 0:
    total += n1 # total = total + n1
else:
    contador += 1

if n2 > 0 and n2 % 2 == 0:
    total += n2 # total = total + n1
else:
    contador += 1

if n3 > 0 and n3 % 2 == 0:
    total += n3 # total = total + n1
else:
    contador += 1

print("El total de la suma de números pares es: ", total)
print("Los números impares o ceros ingresados son: ", contador)

