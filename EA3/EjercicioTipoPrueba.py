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
casillero = np.array([["","","","",""],
                      ["","","","",""],
                      ["","","","",""]], dtype=object)

totalDeVentas   = 0  # acumulador, suma todos los arriendos realizados
filaCasillero   = -1 # almacenará el tipo de casillero
columnaCasillero= -1 # almacenará el nro de casillero

def registroArriendo(casillero):
    pass

def listarCasilleros(casillero):
    pass

def totalVenta(casillero):
    pass

def desocuparCasillero(casillero):
    pass


