# Ejercicios:

# 1.- mostrar los valores y sus indices de los
# números pares que están almacenados en una matriz de 4x4 
# (crear con numeros aleatorios)
import numpy as np

matriz = np.array([
                    [3 , 0, 5, 4],
                    [10,60,70, 5],
                    [20,64,90,55],
                    [30,50,80,51]
                  ])

print(matriz)

for fila in matriz:
    for indice in range(len(fila)):
        if fila[indice] % 2 == 0:
            print(fila[indice])
        

from random import *
fila = 4
columna = 4
matriz2 = [[randint(1,100) for j in range(fila)] for i in range(columna)]
print(matriz2)
for fila in matriz2:
    for indice in range(len(fila)):
        if fila[indice] % 2 == 0:
            print(fila[indice])


# 2.- Crear un arreglo de dos dimensiones de 3 x 3 
# con números ceros, excepto la diagonal 
# principal que debe contener en el mismo 
# orden los siguientes elementos 1, 2 y 3.
