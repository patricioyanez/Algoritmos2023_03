import numpy as np

# crear una matriz 
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("valor de la coordenada 1,1: ", matriz[1,1])
print("valor de la coordenada 2,0: ", matriz[2,0])

# recorrer la matriz
for fila in range(3):
    for columna in range(3):
        print("valor : ", matriz[fila,columna])

print(matriz)

print("Valores y coordenada")
for fila in range(3):
    for columna in range(3):
        print("Fila: ", fila,"Columna: ", columna, "Valor : ", matriz[fila,columna])


matriz1 = np.zeros((4,3))
print(matriz1)

matriz1 = np.ones((5,6))
print(matriz1)

matriz1 = np.diag([1,3,5,1])
print(matriz1)

print("Suma de valores:", matriz.sum())
print("cant. elemento  matriz:", matriz.size)
print("tamaño  matriz:", matriz.shape)