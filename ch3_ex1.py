horas = raw_input("Introduce el numero de horas: ")
horas = float(horas)
tarifa = raw_input("Introduce la tarifa por hora: ")
tarifa = float(tarifa)
if horas > 40:
	salario = (horas * 1.5) * tarifa
	print "Salario: ", tarifa
else:
	salario = horas * tarifa