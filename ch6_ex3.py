def contador(palabra, letra):
	cont = 0 
	for indice in palabra:
		if indice == letra:
			cont = cont + 1


	return cont

palabra = raw_input("Introduza una palabra: ").lower()
letra = raw_input("Introduzca la letra que desea contar: ").lower()
cont = contador(palabra, letra)
print cont