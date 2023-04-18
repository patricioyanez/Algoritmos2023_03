print("*** Acumulador de suma de números ***")
acumulador = 0

num1 = int(input("Ingrese 1er valor: "))
acumulador = acumulador + num1

num1 = int(input("Ingrese 2do valor: "))
acumulador += num1 # otra forma de sumar

num1 = int(input("Ingrese 3er valor: "))
acumulador = acumulador + num1

print("El total de la suma es: ", acumulador)