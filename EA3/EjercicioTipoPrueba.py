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

listaDeOpciones = ["0", "1", "2", "3", "4"]
listaDeOpcionesCasilleros = ["1", "2", "3"]
totalDeVentas   = 0  # acumulador, suma todos los arriendos realizados
filaCasillero   = -1 # almacenará el tipo de casillero
columnaCasillero= -1 # almacenará el nro de casillero
opcion = ""

def registroArriendo(casillero):
    print("****** Registrar Arriendo ******* ")
    print("1.- Super Grande")
    print("2.- Grande")
    print("3.- Pequeño")
    opcion2 = input("Seleccione casillero: ")

    if opcion2 not in listaDeOpcionesCasilleros:
        print("****** La opción no es válida ******")
        input("Presione enter para continuar...")
    else:
        fila = int(opcion2)
        mostrarCasillerosDisponibles(fila)

        nroCasillero = input("Seleccione número de casillero: ")
        try: # evitar que se "caiga" la aplicación
            columna = int(nroCasillero) - 1 # convertir a numero
            fila -= 1
            rut = input("Ingrese su rut: ")
            casillero[fila, columna]= rut # casillero[fila, columna]= ""
        except:
            print("****** La opción no es válida ******")
            input("Presione enter para continuar...")


def mostrarCasillerosDisponibles(fila):
    disponibles = ""
    nroCasillero = 1
    for columna in casillero[fila-1]:
        if columna == "":
            disponibles += str(nroCasillero) + " "
        else:
            disponibles += "X "

        nroCasillero+=1
    print("Lista de casilleros de la opción", fila)
    print(disponibles)

def listarCasilleros(casillero):
    pass

def totalVenta(casillero):
    pass

def desocuparCasillero(casillero):
    pass



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

