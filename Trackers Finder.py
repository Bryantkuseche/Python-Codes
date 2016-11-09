from bs4 import BeautifulSoup
import urllib
import re

while True:
	enlace = raw_input("Introduzca una direccion de busqueda: ")
	if len(enlace) < 1:
		print "Saliendo..."
		quit()
	else:
		print "Obteniendo enlaces..."
		data = urllib.urlopen(enlace).read()
		sopa = BeautifulSoup(data)
		for tracker in sopa.find_all('pre'):
			print (tracker.get_text())
		
		
			
	

	
