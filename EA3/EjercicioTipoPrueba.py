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
import os

# declarar variables
casilleros = np.array([ ["","","","",""],
                        ["","","","",""],
                        ["","","","",""],
                       ], dtype=object)

totalVentas = 0 # acumulador. Para sumar todas las ventas realizadas
filaCasillero = -1 # almacenará el tipo de casillero
columnaCasillero = -1 # almacenará el nro del casillero

listaDeOpcionesValidas = ["0","1","2","3","4"]
listaDeTiposCasilleros = ["1","2","3"]
opcion = ""
# declara las funciones para cada opción:
def registroDeArriendo(casilleros):
    print("***** Registro de arriendo *****")
    print("1.- Casillero Super Grande $2.000")
    print("2.- Casillero Grande $1.000")
    print("3.- Casillero Pequeño $500")
    print("0.- Salir")
    casillero = input("Ingrese tipo de casillero: ")
    if casillero not in listaDeTiposCasilleros:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    else:
        fila = int(casillero) # convertir de str a int. es la fila
        # mostrar casilleros disponibles ???
        casillerosDisponibles(casilleros, fila)

        # try / except
        # evita la "caida" de la aplicación si la conversión no se lleva a cabo
        try:
            nroCasillero = int(input("Ingrese nro del casillero: "))
            columna = nroCasillero -1 # matriz empieza con indice 0
            fila -= 1 # matriz empieza con indice 0
            rut = input("Ingrese su rut:")

            # almacena el rut en el casillero seleccionado
            casilleros[fila, columna] = rut

            print("Datos guardados")
            input("Presione enter para continuar...")
        except: # si ingreso un casillero que no se puede convertir en número o no existe
            print("Error en la elección del casillero")
            input("Presione enter para continuar...")

def listarCasilleros(casilleros):
    print("***** Lista de casilleros *****")
    listado = ""
    valor = ""

    for fila in casilleros:
        nroCasillero = 1
        for columna in fila:
            if columna != "":
                valor = "X"
            else:
                valor = str(nroCasillero)
            listado += valor + " "
            nroCasillero+=1
        listado += "\n"
    print(listado)
    input("Presione enter para continuar...")
    
def totalDeVentas(casilleros):    
    print("***** Total de recaudación *****")
    total = 0
    filita = 0
    for fila in casilleros:
        for columna in fila:
            if columna != "":
                if filita == 0:
                    total += 2000
                elif filita == 1:
                    total += 1000
                elif filita == 3:
                    total += 500
        filita += 1 # permite saber cuanto cobrar según la fila
    print("Total de recaudación:", total)
    input("Presione enter para continuar...")


def desocuparCasillero(casilleros):
    print("***** Desocupar Casillero *****")
    print("1.- Casillero Super Grande")
    print("2.- Casillero Grande")
    print("3.- Casillero Pequeño")
    print("0.- Salir")
    casillero = input("Ingrese tipo de casillero: ")
    if casillero not in listaDeTiposCasilleros:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    else:
        fila = int(casillero) # convertir de str a int. es la fila
        # validar que la conversión sea exitosa
        try:
            nroCasillero = int(input("Ingrese nro del casillero: "))
            columna = nroCasillero -1 # matriz empieza con indice 0
            fila -= 1 # matriz empieza con indice 0
            # limpiar casillero
            casilleros[fila, columna] = ""

            print("Casillero liberado...\n")
            listarCasilleros(casilleros)
        except: # si ingreso un casillero que no se puede convertir en número o no existe
            print("Error en la elección del casillero")
            input("Presione enter para continuar...")

def casillerosDisponibles(casilleros, fila):
    listado = ""
    nroCasillero = 1
    for columna in casilleros[fila-1]:
        if columna == "":
            listado += str(nroCasillero) + "\n"
        else:
            listado += "X" + "\n"
        nroCasillero+=1
    print(listado)


# definir el menú
while opcion != "0":
    os.system("cls")
    print("======= Administración de Casilleros ========")
    print("1.- Registro de arriendo")
    print("2.- Listar casilleros (ocupados y los que no)")
    print("3.- Total de ventas")
    print("4.- Desocupar casillero")
    print("0.- Salir")
    opcion = input("Seleccione una opción: ")

    #validar opción seleccionada
    if opcion not in listaDeOpcionesValidas:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    elif opcion == "1":
        registroDeArriendo(casilleros)
    elif opcion == "2":
        listarCasilleros(casilleros)
    elif opcion == "3":
        totalDeVentas(casilleros)
    elif opcion == "4":
        desocuparCasillero(casilleros)




