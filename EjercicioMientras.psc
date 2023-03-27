Algoritmo sin_titulo
	// La dueña del almacén, Donde Margarita, desea tener un programa que le permita  
	// calcular las ganancias (20%) de cada producto, uno por uno, y de 
	// manera continua. Esto significa que, si un producto tiene precio de venta 
	// de 500 pesos, es necesario calcular el 20% y obtener el resultado.
	// Por otro lado, el programa debe seguir preguntando el valor del siguiente  
	// producto y dando su resultado correspondiente a menos que ella coloque 0 
	// o presione enter.
	
	Definir precio Como Entero
	Definir resultado Como Entero
	Definir opcion Como Entero
	opcion = 1
	
	Mientras opcion <> 0 Hacer
		Escribir "Ingrese precio del producto"
		leer precio
		resultado = precio * 20 / 100
		Escribir "La ganancia de ", precio, " es: ", resultado
		Escribir "[1] para Continuar"
		leer opcion
	FinMientras
	
	
FinAlgoritmo
