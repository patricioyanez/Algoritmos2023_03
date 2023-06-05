# manejo de listas

#crear una lista
lista = [1,2,3,4,5]

#mostrar un valor
print(lista[0]) # valor indice 0
print(lista[1]) # valor indice 1

print(lista) # muestra todo la lista

print(lista[-1]) # indice negativo, 
# muestra el ultimo valor
print(lista[-2]) 

#recorrer una lista
for i in range(len(lista)):
    print("valor:", lista[i])

print("\n Modificar valor")
# modificar un valor según indice
lista[2] = 200

#recorrer una lista
for i in range(len(lista)):
    print("valor:", lista[i])


# agregar un valor
lista.append(1000)


#recorrer una lista
for i in range(len(lista)):
    print("indice:",i, "valor:", lista[i])

# eliminar un valor
print("****** ELIMINAR")
lista.pop()
#recorrer una lista
for i in range(len(lista)):
    print("indice:",i, "valor:", lista[i])

#CANTIDAD DE ELEMENTOS
print("La cantidad de elementos: ", len(lista))

#crear una matriz con una lista ( 2 x 4)
nuevaLista = [[1,2,3,4], [5,6,7,8]]
print(nuevaLista)

print("Cantidad de elementos:",len(nuevaLista))
# recorrer una lista con listas (matriz)
for i in range(len(nuevaLista)):
    for j in range(len(nuevaLista[i])):
        print("coordenadas:",i,j, "valor:", nuevaLista[i][j])


# ejercicios: multiplicar por 10 cada elemento dentro de la
#lista creada anteriormente
for i in range(len(nuevaLista)):
    for j in range(len(nuevaLista[i])):
        nuevaLista[i][j] = nuevaLista[i][j] * 10

print(nuevaLista)