opcion = ""

while opcion != "5":
    print("******* Calculadora *******") ## multiplicar y dividir
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")

    opcion = input("Ingrese opción:")

    # si NO ESTA en los caracteres: 1,2, 3, 4 o 5 (como string) no es válido
    if opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no es válida")
    elif opcion == "1":
        n1 = int(input("Ingrese 1er número:"))
        n2 = int(input("Ingrese 2do número:"))
        print("La suma de los números es:", (n1+n2))
    elif opcion == "2":
        n1 = int(input("Ingrese 1er número:"))
        n2 = int(input("Ingrese 2do número:"))
        print("La resta de los números es:", (n1-n2))
    elif opcion == "3":
        n1 = int(input("Ingrese 1er número:"))
        n2 = int(input("Ingrese 2do número:"))
        print("La mulitiplicación de los números es:", (n1*n2))
    elif opcion == "4":
        n1 = int(input("Ingrese 1er número:"))
        n2 = int(input("Ingrese 2do número:"))

        if n2 == 0:
            print("No se puede dividir por cero, vuelva a intentar")
        else:
            print("La división de los números es:", (n1/n2))
    
    