import os

contador = 1
nombredir = raw_input("Enter: ")
for (nombredir, dirs, ficheros) in os.walk('.'):
	for nombrefichero in ficheros:
		if nombrefichero.endswith('.mp3'):
			contador = contador + 1
print 'Ficheros:', contador


