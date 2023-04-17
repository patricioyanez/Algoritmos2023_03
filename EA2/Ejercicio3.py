# Ingrese 3 notas por teclado (valide que sean entre 1 y 7) 
# y calcule su promedio. Si la nota resultante es mayor o igual a 4.0 
# entonces indique que está aprobado, 
# en caso contrario notifique que está reprobado.

print("**** Promedio de notas ****")
nota1 = float(input("Ingrese nota 1:"))
nota2 = float(input("Ingrese nota 2:"))
nota3 = float(input("Ingrese nota 3:"))

if nota1 < 1 or nota1 > 7: # si no está en el rango
    print("La primera nota ingresada no es válida.")
elif nota2 < 1 or nota2 > 7:
    print("La segunda nota ingresada no es válida.")
elif nota3 < 1 or nota3 > 7:
    print("La tercera nota ingresada no es válida.")
else:
    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 4:
        print("Ud está aprobado :)")
    else:
        print("Ud. reprobó :(, lo espero en Enero.")

print("Fin app")