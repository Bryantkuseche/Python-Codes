fichero = raw_input("Introduzca nombre del fichero: ")
manf = ''
try:
	if fichero == 'na na boo boo':
		print "NA NA BOO BOO PARA TI - Has sido un nino malo!"
	else:
		manf = open(fichero)
except:
	print "No se pudo abrir " , fichero
	exit()
for indice in manf:
	print indice