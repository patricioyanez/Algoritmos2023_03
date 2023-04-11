# Solicitar edad y clasifiquelo según rango etario
# niño, adolescente, adulto, adulto mayor
print("Clasificación por rango etario")
edad = input("Ingrese su edad:")
edad = int(edad)

if edad <= 12:
    print("Ud. es un niño")
elif edad < 19:
    print("Ud. es Adolescente")
elif edad < 65:
    print("Ud. es Adulto")
else:
    print("Ud. está en la 3ra edad")