#I.- Caso: Máquina de Bebidas

# En su lugar de trabajo existe una máquina donde puede adquirir bebidas. Existen tres 
# opciones de bebida: Coca-Cola, Fanta y Sprite. El valor de cualquiera de ellas es: $400.
# Desarrolle un programa que permita vender una bebida y entregar vuelto si así se determina. 
# El programa debe solicitar por pantalla el tipo de bebida que va a comprar: 
# 1) Coca-Cola, 2) Fanta o 3) Sprite (validar opción). 
# Además, se debe pedir el dinero a pagar por la bebida.
# -	Si el dinero es igual a $400 no tiene vuelto.
# -	Si el dinero es mayor a $400 debe calcular y entregar vuelto.
# -	Si el dinero es menor a $400 debe mandar un mensaje de alerta y no entregar la bebida.
# Finalizado el proceso, esperar una nueva orden.


import os

opcion = ""
cocacola = 0
fanta = 0
sprite = 0
fueVendida = False
totalVentas = 0
while opcion != "6":
    os.system ("cls")
    print("******* Maquina de bebidas *******")
    print("1.- CocaCola")
    print("2.- Fanta")
    print("3.- Sprite")
    print("4.- Cantidad de ventas")
    print("5.- Total de ventas registradas")
    print("6.- Salir")
    opcion = input("El valor de la bebida es $400. Ingrese opción:")

    if opcion not in ("1", "2", "3", "4", "5", "6"):
        print("Opción no es válida")
    elif opcion == "6":
        print("Aplicación cerrada")
    elif opcion == "4":
        print("******* Listado de ventas *******")
        print("CocaCola: ", cocacola)
        print("Fanta: ", fanta)
        print("Sprite: ", sprite)
    elif opcion == "5":
        print("Total de las ventas registradas es:", totalVentas)
    else:
        monto = int(input("Ingrese cantidad de dinero:"))
        total = monto - 400
        if total == 0:
            print("Vuelto: $0. Gracias por la compra")
            fueVendida = True
        elif total > 0:
            print("Vuelto: ", total, ". Gracias por su compra")
            fueVendida = True
        else:
            print("Falta dinero. Vuelva a intentar")
            fueVendida = False
        
        if fueVendida:
            totalVentas += 400
            if opcion == "1":
                cocacola += 1
            elif opcion == "2":
                fanta += 1
            else:
                sprite += 1
    input("Presione enter para continuar")
## agregar contadores para saber cuantas bebidas se vendieron de cada una. 
# Crear otra opcion en el menú

# Agregar opción total de ventas: Suma todas las ventas realizadas