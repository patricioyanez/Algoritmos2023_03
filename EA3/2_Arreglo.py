# instalar numpy:
# ir a consola o terminal
# pip install numpy
# ver si esta instalado:
# pip list
import numpy

arreglo = numpy.array([1,5,6,7,9,110,50,40,3,55])
print(arreglo)

print("Cantidad de dimensiones:", arreglo.ndim)
print("Cantidad de elementos  :", len(arreglo))
print("Valor elemento 2 :", arreglo[2]) # indice de inicio: 0
print("Cortar arreglo: ", arreglo[2:5]) # devuelve el indice 2, 3 y 4
print("Cortar arreglo: ", arreglo[0:8:3]) # aumenta en 3 el contador para el indice
print("Valor último elemento:", arreglo[-1])
print("Valor antepenúltimo  :", arreglo[-3])
            # cambiar valor de inicio. Por defecto parte del cero
arreglo2 = [i+10 for i in range(0,5)] # crear arreglo con 5 elementos
print(arreglo2)

for i in range(len(arreglo2)): ## recorrer un arreglo
    print(arreglo2[i])

# crea un arreglo de 10 elementos y valores desde el cero
arreglo3 = numpy.arange(10)
print(arreglo3)


arreglo4 = arreglo3
print(arreglo4)
arreglo4[0] = 100 # modifica el valor del indice 0
print(arreglo3)

# OPERACIONES CON ARREGLO
arr1 = numpy.array([10,20,30,40,50])
arr2 = numpy.array([ 1, 2, 3, 4, 5])
res = arr1 + arr2 # ambos arreglos deben tener la misma cantidad de elementos
print("resultado: ", res )
res = arr1 * arr2
print("resultado: ", res )


arr1 = numpy.array([10,20,30,40, 5])
arr2 = numpy.array([ 1,20, 3,40,50])
print(arr1 == arr2) # devuelve un arreglo V/F según la comparación realizada
print(arr1 > arr2) # <, >= o <=
print("Sumar los elementos: ", arr1.sum()) # suma los valores
print("Promedio los elementos: ", arr1.mean()) # promedia los valores avg
print("Valor Menor : ", arr1.min()) # devuelve el valor menor
print("Valor Mayor : ", arr1.max()) # devuelve el valor mayor

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
