Algoritmo Factorial
	Definir numero1 Como Entero
	Definir total Como Entero
	Escribir "Ingrese n�mero:"
	Leer numero1
	
	si numero1 < 1 Entonces
		Escribir "Debe ingresar un n�mero positivo"
	SiNo
		total = 1
		para contador <- 1 Hasta numero1 Hacer
			total = total * contador // acumulador y contador
		FinPara
		Escribir "El factorial es:", total
	FinSi
	
FinAlgoritmo
