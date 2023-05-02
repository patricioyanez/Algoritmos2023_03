contador = 0

while contador < 10:
    print("El número es:", contador)
    contador += 1

print("****** pares *******")
contador = 0
while contador < 10:
    print("El número es:", contador)
    contador += 2


print("****** Break *******")
contador = 0
while contador < 100:
    print("El número es:", contador)
    contador += 1
    if contador == 20:
        break

print("****** fin Break *******")