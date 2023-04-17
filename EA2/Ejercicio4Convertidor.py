# Genere un convertidor de: 
# Ingrese un monto en $ para convertirlo a:
# Dólar a pesos chilenos 
# Peso Argentino a peso chileno 
# Yen a pesos chilenos 
# 
# Buscar los valores de hoy

print("**** Convertidor de monedas a $CL ****")
arg = 3.7
dolar = 800.0
yen = 5.97
valorMoneda = 0.0
monto = input("Ingrese monto de la moneda a convertir: ")
moneda= input("Seleccione moneda origen [1] Argentina [2] USD [3] Yen:")

if moneda == "1": # comparar el mismo tipo de dato
    valorMoneda = arg
elif moneda == "2":
    valorMoneda = dolar
else:
    valorMoneda = yen

total = float(monto) * valorMoneda

print(f"El valor en pesos es: {total}")