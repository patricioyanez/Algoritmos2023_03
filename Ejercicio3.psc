Algoritmo Ejercicio3
	// Realice un programa en pseudocódigo que determine el pago a 
	// realizar en una fotocopiadora, 
	// donde el precio por cada fotocopia es de $20 en negro y $100 color. Al imprimir más 
	// de 30 fotocopias se realiza un descuento al total del pago del x%.( del 20% al 40%)
	// Notas: 
	//  -	Asuma que el cálculo del pago para x clientes. 
	// 	-	Valide que la cantidad de fotocopias sea mayor a 0.
	//  -  El usuario debe seleccionar si la fotocopia es color o negro
	
	Definir precioNegro Como Entero
	Definir precioColor Como Entero
	Definir cantidad Como Entero
	Definir porcentaje Como Entero
	Definir total Como Real
	Definir opcion Como Entero
	opcion = 0
	precioColor = 100
	precioNegro = 20
	Mientras opcion <> 3 Hacer
		Escribir "**** Menú ****"
		Escribir "[1] Color"
		Escribir "[2] Negro"
		Escribir "[3] Salir"
		Escribir "Seleccione una opción:"
		Leer opcion
		
		si opcion = 1 o opcion = 2 Entonces
			Escribir "Ingrese cantidad de fotocopias: "
			Leer cantidad
			
			si opcion = 1 Entonces
				total = cantidad * precioColor
			SiNo
				total = cantidad * precioNegro
			FinSi
			
			si cantidad >= 30 Entonces
				Escribir "Ingrese % de descuento:"
				Leer porcentaje
				
				si porcentaje >= 20 y porcentaje <= 40 Entonces
					total = total - (porcentaje * total / 100)
				FinSi
				
				Escribir "El total a pagar es: " , total
			FinSi	
			
		FinSi
		
	FinMientras
	
	
FinAlgoritmo
