# crear una calculadora usando funciones
# para las operaciones + - * / usando menu funciones

def sumar(n1, n2):
    return n1+n2
def restar(n1, n2):
    return n1-n2
def multiplicar(n1, n2):
    return n1*n2
def dividir(n1, n2):
    if n2 == 0:
        return "No se puede dividir por cero"
    return n1/n2
#
# Ejercicio 2: Agregar sumatoria y factorial de un número
#
import os
opcion = ""
while opcion != "0":
    os.system ("cls")
    print("=== Super Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Sumatoria")
    print("6. Factorial")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")

    # validar
    if opcion not in ("0","1","2","3","4","5","6"):
        print("Opción no válida")
        input("Presione enter para continuar...")
    elif opcion == "5":
        print("Ingrese un numero para obtener la sumatoria: ")
        num1 = int(input("Ingrese un número: "))
 #       sumatoria(num1)
    else:
        print("Ingrese dos numeros: ")
        num1 = int(input("Ingrese el primer numero: ")) # try except
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = 0
        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)


        print("\nEl resultado es:", resultado) 
        input("Presione enter para continuar...")
        
