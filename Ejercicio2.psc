Algoritmo Ejercicio2
	Definir numero1 Como Entero
	Definir numero2 Como Entero
	
	Escribir "Ingrese n�mero 1:"
	Leer numero1
	Escribir "Ingrese n�mero 2:"
	Leer numero2
	si numero1 < 1 o numero2 < 1 Entonces
		Escribir "Debe ingresar solo n�meros positivos"
	SiNo
		si numero1 > numero2 Entonces
			Escribir "El n�mero 1 es mayor (", numero1, ")"
		SiNo			
			Escribir "El n�mero 2 es mayor o igual al n�mero 1 (", numero2, ")"
		FinSi
	FinSi
FinAlgoritmo
