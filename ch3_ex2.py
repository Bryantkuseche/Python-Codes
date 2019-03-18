horas = raw_input("Introduce el numero de horas: ")
tarifa = raw_input("Introduce la tarifa por hora: ")
try:
	horas = float(horas)
	tarifa = float(tarifa)
	if horas > 40:
		horasExtra = (horas - 40)
		salario = ((horas - horasExtra)  * tarifa) + (horasExtra * tarifa * 1.5)
		print "Salario: ", salario 
	else:
		salario = horas * tarifa
		print "Salario: ", salario
except:
	print "Error, por favor introduce un numero"