opcion = ""

while opcion != "3":
    print("******* Calculadora *******")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Salir")

    opcion = input("Ingrese opción:")

    # si NO ESTA en los caracteres: 1,2 o 3 (como string) no es válido
    if opcion not in ("1", "2", "3"):
        print("Opción no es válida")
    elif opcion == "1":
        n1 = int(input("Ingrese 1er número:"))
        n2 = int(input("Ingrese 2do número:"))
        print("La suma de los números es:", (n1+n2))
    
    