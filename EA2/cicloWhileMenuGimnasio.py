# En un Gimnasio se está realizando una encuesta para determinar la cantidad de 
# personas según el rango etario que asisten a él. Existen tres rangos o categorías:

# -	Entre 10 y 17 años niño.
# -	Entre 18 y 29 años joven.
# -	Entre 30 y 50 años adulto.
# 
# Las personas que asisten al gimnasio deben estar entre estos rangos de edad.
# Desarrolle un programa que permita determinar:
# 
# -	El promedio de edad de las personas que asisten al gimnasio.
# -	La cantidad de mujeres y hombres que asisten al gimnasio.
# -	La cantidad final por categoría (rango etarios)
# 
# El programa debe solicitar por pantalla el sexo (F ó M) y la edad de la 
# persona (validar datos de entrada).
# 
import os
opcion = ""
nino = 0
joven= 0
adulto=0
f = 0
m = 0
while opcion != "5":
    os.system ("cls")
    print("******* Maquina de bebidas *******")
    print("1.- Ingrese de datos")
    print("2.- Promedio de edades")
    print("3.- Cantidad de hombres y mujeres")
    print("4.- Reporte rango etario")
    print("5.- Salir")
    opcion = input("Ingrese opción:")

    if opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no es válida")
    elif opcion == "5":
        print("Aplicación cerrada")
    elif opcion == "1":
        print("================ Ingreso de datos ================ ")
        edad = int(input("Ingrese edad: ")) # except 
        genero= input("Ingrese F para femenino y M para Masculino: ")

        if edad < 10 or edad > 50:
            print("La edad esta fuera del rango")
        elif genero not in ("F", "M", "f", "m"):
            print("La opción esta mala")
        else:
            if edad <= 17:
                nino+=1
            elif edad <= 29:
                joven+=1
            else:
                adulto+=1
            
            if genero.upper()=="F":
                f+=1
            else:
                m+=1

    input("presione enter para continuar")


