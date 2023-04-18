# flag o bandera

flag = False # esMayorDeEdad

edad = int(input("Ingrese su edad:"))

if edad >= 18: 
    flag = True # se cumple la condición y se cambia el estado
else:
    flag = False

if flag:
    print("Es mayor de edad")
else:
    print("Es menor de edad")