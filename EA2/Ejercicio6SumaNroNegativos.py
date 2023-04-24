print("==== Evaluar 3 números menores a cero====")
n1 = int(input("Ingrese el 1er número: "))
n2 = int(input("Ingrese el 2do número: "))
n3 = int(input("Ingrese el 3er número: "))

contador = 0
if n1 < 0:
    contador += 1

if n2 < 0:
    contador += 1

if n3 < 0:
    contador += 1

print("Los números menores a ceros son: ", contador)