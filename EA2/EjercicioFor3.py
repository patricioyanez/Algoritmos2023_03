# Ingrese un número entero mayor a cero por teclado 
# e indique si es o no “Primo”.

print("=== BUSQUEDA DE NUMEROR PRIMOS ===")
numero = int(input("Ingrese número: "))
flag = True
for n in range(2, numero):
    if numero % n == 0:
        flag = False
        break
if flag:
    print("El número es primo")
else:
    print("El numero no es primo")

