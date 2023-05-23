lista = [1,2,3,4] # indice inicia del cero

print(lista)

print("valor del indice 1 (parte del cero): ", lista[1])
print("valor del indice 3 (parte del cero): ", lista[3])

# indice  : 0       1       2    3    4 
lista2 = ["hola", "CHAO", True, 1.5, 100]

print("Valor del índice 1: ", lista2[1])
print("Valor del índice 4: ", lista2[4])
print("Valor del índice 4: ", lista2[-1])
print("Valor del índice 3: ", lista2[-2])

print("cantidad de elementos:", len(lista))

lista.append(100) # black box
print(lista)
print("cantidad de elementos:", len(lista))


lista.reverse()
print(lista)

lista.insert(2, 500)
print(lista)

lista3 = [1000, 2000]
# agrega una lista previa a otra
lista.extend(lista3)
print(lista)

#eliminar un elemento
lista.pop(-2)
print(lista)