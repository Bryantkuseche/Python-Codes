print "Calificador"
calificacion = raw_input("Introduce una calificacion valida: ")
try:
	calificacion = float(calificacion)
	if calificacion >= 0.0 and calificacion <= 0.9:
		if calificacion >= 0.9:
			print "Sobresaliente"
		elif calificacion >= 0.8:
			print "Notable"
		elif calificacion >= 0.7:
			print "Bien"
		elif calificacion >= 0.6:
			print "Suficiente"
		elif calificacion < 0.6:
			print "Insuficiente"
	else:
		print "Puntuacion incorrecta"
except:
	print "Puntuacion incorrecta"