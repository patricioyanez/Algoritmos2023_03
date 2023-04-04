Algoritmo Ejercicio2
	Definir numero1 Como Entero
	Definir numero2 Como Entero
	
	Escribir "Ingrese número 1:"
	Leer numero1
	Escribir "Ingrese número 2:"
	Leer numero2
	si numero1 < 1 o numero2 < 1 Entonces
		Escribir "Debe ingresar solo números positivos"
	SiNo
		si numero1 > numero2 Entonces
			Escribir "El número 1 es mayor (", numero1, ")"
		SiNo			
			Escribir "El número 2 es mayor o igual al número 1 (", numero2, ")"
		FinSi
	FinSi
FinAlgoritmo
