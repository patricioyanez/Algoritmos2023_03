# Funciones
# definición de una funcion
def saludar():
    # cuerpo de una funcion
    print("Hola mundo")


# llamar o invocar una función
saludar()


def sumar():
    numero1=10
    numero2=20
    return numero1+numero2


total = sumar()
print("El total de la suma es:", total)


def sumar2(num1, num2):
    res = num1+num2
    return res
    
total = sumar2(5, 10)
print("Total:", total)
