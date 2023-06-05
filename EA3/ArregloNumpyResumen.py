# arreglo usando numpy
# importar librería
import numpy as np

#crear arreglo 
arreglo = np.array([1, 2, 3, 4, 5])
#imprimir arreglo
print(arreglo)
# crear arreglo con 5 elementos
arreglo2 = [i for i in range(0,5)]  # 0 al 4
#imprimir arreglo
print(arreglo2)
# crea un arreglo de 10 elementos y valores desde el cero
arreglo3 = np.arange(10)
#imprimir arreglo
print(arreglo3)

print("===== Obtener valores según index")
# imprimir valor del indice 0 y 1
print("Valor 0: ",arreglo[0])
print("Valor 1: ",arreglo[1])


print(arreglo[-1]) # último indice
print(arreglo[-2]) # penúntimo indice

print("****** Recorrer arreglo")
# recorrer un arreglo
for i in range(len(arreglo)): 
    print(arreglo[i])

for valor in arreglo2:
    print("Valor: ", valor)


print("\n Modificar valor")
# modificar un valor según indice
arreglo[2] = 200
# recorrer un arreglo
for i in range(len(arreglo)): 
    print(arreglo[i])


#Cantidad de elementos y dimensiones de la matriz
print("Cantidad de elementos: ", len(arreglo))
print("Cantidad de dimensiones: ", arreglo.ndim)


#crear una matriz  ( 3 x 5)
matriz = np.array([[21, 22, 23, 24, 25],
                    [16, 17, 18, 19, 10],
                    [11, 21, 31, 41, 51]])

# otras formas de crear matriz
matriz1 = np.zeros((4,3))
print(matriz1)

matriz2 = np.ones((5,6))
print(matriz2)

matriz3 = np.diag([1,3,5,1])
print(matriz3)

#imprimir valor usando coordinadas
print("Valor coordenadas 0,4:",matriz[0,4])
print("Valor coordenadas 2,2:",matriz[2,2])

#información de la matriz
print("Cantidad de elementos fila 0: ", len(matriz[0]))
print("Cantidad de filas y columnas : ", matriz.shape)
print("Cantidad de filas : ", matriz.shape[0])
print("Cantidad de columnas : ", matriz.shape[1])
print("Cantidad de dimensiones: ", matriz.ndim)


# recorrer la matriz usando indices
for fila in range(3):
    for columna in range(5):
        print("coordenadas:",fila,columna,":", matriz[fila,columna])

# recorrer la matriz obteniendo los valores almacenados
print("\n======== Obtener valores:")
for fila in matriz:
    for indice in fila:
        print("valor:",indice)


# Ejercicio: mostrar los valores y sus indices de los
# números pares que están almacenados en una matriz
print("\n======== Solución:")
for fila in range(3):
    for columna in range(5):
        if matriz[fila,columna] % 2 == 0:
            print("valor:", matriz[fila,columna], "indice:", fila, columna)
            