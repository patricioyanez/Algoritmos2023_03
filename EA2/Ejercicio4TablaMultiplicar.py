# Ingrese por teclado un número positivo y 
# muestre su tabla de multiplicar 
# (considere que la tabla sea de 1 a 10).

print("Tabla de multiplicar")
numero = int(input("Ingrese valor(rango del 1 al 10): "))

if numero < 1 or numero > 10:
    print("El número no es válido")
else:
    print(numero,  " x  1 :", numero*1)
    print(numero,  " x  2 :", numero*2)
    print(numero,  " x  3 :", numero*3)
    print(numero,  " x  4 :", numero*4)
    print(numero,  " x  5 :", numero*5)
    print(numero,  " x  6 :", numero*6)
    print(numero,  " x  7 :", numero*7)
    print(numero,  " x  8 :", numero*8)
    print(numero,  " x  9 :", numero*9)
    print(numero,  " x 10 :", numero*10) # ctrl + c y v para copiar linea