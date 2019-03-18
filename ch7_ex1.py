fichero = raw_input("Introduzca nombre del fichero: ")
try:
	manf = open(fichero)
except:
	print "No se pudo abrir " , fichero
	exit()
for indice in manf:
	print indice.upper()