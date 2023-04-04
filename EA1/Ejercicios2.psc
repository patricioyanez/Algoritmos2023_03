Algoritmo Ejercicios2
	// Realice un programa en pseudocódigo que determine el pago a 
	// realizar en una fotocopiadora, 
	// donde el precio por cada fotocopia es de $20. Al imprimir más 
	// de 30 fotocopias se realiza 
	// un descuento al total del pago del 10%.
	// Notas: 
	//  -	Asuma que el cálculo del pago es para un solo cliente. 
	// 	-	Valide que la cantidad de fotocopias sea mayor a 0.
	
	Definir total Como Entero
	Definir cantidad Como Entero
	Definir precio Como Entero
	precio = 20
	
	Escribir "Ingrese cantidad de fotocopias: "
	Leer cantidad
	
	si cantidad < 1 Entonces
		Escribir "Solo se permite números positivos"
	SiNo
		total = precio * cantidad
		
		si cantidad >= 30 Entonces
			total = total * .9
		FinSi
		
		Escribir "Total a pagar: ", total
	FinSi
	
	
	
FinAlgoritmo
