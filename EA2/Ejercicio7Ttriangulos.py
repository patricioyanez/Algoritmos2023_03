print("==== Evaluar 3 números menores a cero====")
lado1 = int(input("Ingrese el 1er lado: "))
lado2 = int(input("Ingrese el 2do lado: "))
lado3 = int(input("Ingrese el 3er lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilátero")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("El triángulo es escaleno")
else:
    print("El triangulo es isósceles")