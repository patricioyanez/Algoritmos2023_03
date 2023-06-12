# Crear una aplicación que permita registrar los arriendos de
# casilleros que tiene una empresa de turismo.
# Las categorias de estos casilleros son:
# 1.- Super Grande= $2000
# 2.- Grande      = $1000
# 3.- Pequeño     = $500
# 
# Los casilleros tienen una capacidad de 3 filas 
# (una para cada capacidad) y de 5 unidades para cada una
# Al arrendar uno, se debe registrar el rut
# 
# Las opciones a realizar son:

# 1.-Registro de arriendo
# 2.-Listar casilleros (ocupados y los que no)
# 3.-Totalizar la venta hasta el momento.
# 4.-Desocupar un casillero


# Usar funciones para cada una de las opciones
# validar que no esten vacios los datos a ingresar

import numpy as np
import os # para limpiar pantalla
casillero = np.array([["","","","",""],
                      ["","","","",""],
                      ["","","","",""]], dtype=object)

totalDeVentas   = 0  # acumulador, suma todos los arriendos realizados
filaCasillero   = -1 # almacenará el tipo de casillero
columnaCasillero= -1 # almacenará el nro de casillero
opcion = ""

def registroArriendo(casillero):
    pass

def listarCasilleros(casillero):
    pass

def totalVenta(casillero):
    pass

def desocuparCasillero(casillero):
    pass


listaDeOpciones = ["0", "1", "2", "3", "4"]

while opcion != "0":
    os.system("cls")
    print("====== Administración de Casilleros ======")
    print("1.- Registrar Arriendo")
    print("2.- Listar Casilleros")
    print("3.- Total de ventas")
    print("4.- Desocupar Casilleros")
    print("0.- Salir")
    opcion = input("Ingrese una opción: ")

    #validar si es una opción válida
    if opcion not in listaDeOpciones:
        print("****** La opción no es válida ******")
        input("Presione enter para continuar...")
    elif opcion == "1":
        registroArriendo(casillero)
    elif opcion == "2":
        listarCasilleros(casillero)
    elif opcion == "3":
        totalVenta(casillero)
    elif opcion == "4":
        desocuparCasillero(casillero)

