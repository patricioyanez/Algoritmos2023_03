Algoritmo TablaDeMultiplicar
	//Ingrese un numero > 0 y multiplicarlo
	// del 1 al 10
	Definir numero1 Como Entero
	Definir resultado Como Entero
	Escribir "Ingrese número a multiplicar:"
	Leer numero1
	
	Si numero1>0 Entonces
		Para contador <- 1 Hasta 10 Hacer
			resultado = numero1 * contador
			Escribir numero1, " x ", contador, " = ", resultado
		FinPara
	FinSi
	
FinAlgoritmo
