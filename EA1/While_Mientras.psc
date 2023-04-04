Algoritmo While_Mientras
	
	Definir numero Como Entero
	Mientras numero < 10
		numero = numero + 1
		Escribir "Numero: ", numero
	FinMientras
	
	Definir respuesta Como Caracter
	Mientras respuesta <> "5" Hacer // !=
		Escribir "**** Menú ****"
		Escribir "[1] Sumar"
		Escribir "[2] Restar"
		Escribir "[3] Multiplicar"
		Escribir "[4] Dividir"
		Escribir "[5] Salir"
		Escribir "Seleccione una opción:"
		Leer respuesta
		
		si respuesta = "1" Entonces
			Escribir "Ingrese primer número:"
			Leer numero1
			Escribir "Ingrese segundo número:"
			Leer numero2
			Escribir "El resultado es: ", numero1+numero2
			Escribir "Presione enter para continuar"
			Esperar Tecla
		FinSi
		
		si respuesta = "2" Entonces
			Escribir "Ingrese primer número:"
			Leer numero1
			Escribir "Ingrese segundo número:"
			Leer numero2
			Escribir "El resultado es: ", numero1-numero2
			Escribir "Presione enter para continuar"
			Esperar Tecla
		FinSi
		
		si respuesta = "3" Entonces
			Escribir "Ingrese primer número:"
			Leer numero1
			Escribir "Ingrese segundo número:"
			Leer numero2
			Escribir "El resultado es: ", numero1*numero2
			Escribir "Presione enter para continuar"
			Esperar Tecla
		FinSi
		
		si respuesta = "4" Entonces
			Escribir "Ingrese primer número:"
			Leer numero1
			Escribir "Ingrese segundo número:"
			Leer numero2
			
			si numero2 = 0 Entonces
				Escribir "|====== No se puede dividir por cero =======|"
			sino
				Escribir "El resultado es: ", numero1/numero2			
			FinSi
			
			Escribir "Presione enter para continuar"
			Esperar Tecla
		FinSi
	FinMientras
	
FinAlgoritmo
