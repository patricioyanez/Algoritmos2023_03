#Ejercicios:

# 1.1 Crear un arreglo unidimensional de tamaño 10, 
# con elementos aleatorios de números enteros del 0 al 100, 
# para ello deberá investigar la función que 
# permita crear números aleatorios.
# 
# 1.2. Crear una copia del arreglo y muestre:
# Elemento mayor
# Elemento menor
# Suma de los elementos
# Promedio de los elementos
# Mostrar todos los elementos

# pip list
# pip install numpy

from numpy import random

numero = random.randint(100)
print(numero)

arreglo = random.randint(100, size=(10))
print(arreglo)

arreglo2 = arreglo
arreglo2[0] = 1000
print(arreglo)

print("Copia del arreglo")
arreglo3 = arreglo.copy()
arreglo3[0] = 4000
print(arreglo)
print(arreglo3)