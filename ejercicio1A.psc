Algoritmo ejercicio1A
	// Solicitar x cantidad de notas al usuario
	// promediarlas y entregar resultado (aprobado o no)
	// las notas deben estar en el rango de 10 a 70
	Definir cantidadNotas Como Entero
	Definir nota Como Entero
	Definir resultado Como Real
	Escribir "Ingrese cantidad de notas:"
	Leer cantidadNotas
	
	Para i <- 1 Hasta cantidadNotas Hacer
		Escribir "Ingrese nota nro ", i, ": "
		Leer nota
		resultado = resultado + nota
	FinPara
	
	resultado = resultado / cantidadNotas
	Escribir "El promedio es: ", resultado
	
	si resultado >= 40 Entonces
		Escribir "Ud aprobó :) "
	SiNo
		Escribir "Ud. reprobó, Vuelva en verano :)"
	FinSi
FinAlgoritmo
