def calculo_salario(horas,tarifa):
	if(horas > 40):
		horasExtra = horas - 40
		salario = ((horas - horasExtra) * tarifa) + (horasExtra * tarifa * 1.5)
		return salario
	else:
		salario = (horas * tarifa)
		return salario
try:
	horas = float(raw_input("Introduza el numero de horas: "))
	tarifa = float(raw_input("Introduzca la tarifa por hora: "))
	salario = calculo_salario(horas,tarifa)
	print "Salario: ", salario
except:
	print "Error, por favor introduce un numero"