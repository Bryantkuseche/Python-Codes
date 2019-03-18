fichero = raw_input("Introduzca nombre del fichero: ")
probabilidad = 0.0
contador = 0

try:
	manf = open(fichero)
except:
	print "No se pudo abrir " , fichero

for i in manf:
	if i.startswith('X-DSPAM-Confidence'):
		probabilidad = probabilidad + float(i[i.find('0.'):].rstrip())
		contador = contador + 1

print (probabilidad/contador)