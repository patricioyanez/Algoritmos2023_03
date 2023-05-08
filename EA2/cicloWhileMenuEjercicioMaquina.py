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


opcion = ""

while opcion != "4":
    print("******* Calculadora *******")
    print("1.- CocaCola")
    print("2.- Fanta")
    print("3.- Sprinte")
    print("4.- Salir")
    opcion = input("Ingrese opción:")

    if opcion not in ("1", "2", "3", "4"):
        print("Opción no es válida")
    elif opcion == "4":
        print("Aplicación cerrada")
    else:
        monto = int(input("Ingrese cantidad de dinero:"))
        total = monto - 400
        if total == 0:
            print("Vuelto: $0. Gracias por la compra")
        elif total > 0:
            print("Vuelto: ", total, ". Gracias por su compra")
        else:
            print("Falta dinero. Vuelva a intentar")
## agregar contadores para saber cuantas bebidas se vendieron de cada una. Crear otra opcion en el 
# menú