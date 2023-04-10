#Ejercicio "3"
print("Cálculo de formula")
numero = input("Ingrese un número entero:") # input devuelve String (str)
numero = int(numero)  # convertir el str en int (texto a entero)

resultado = (numero ** 2 + 3 * numero + 1) / 4

print(f"El resultado de la operación es: {resultado}")