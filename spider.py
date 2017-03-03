import httplib, urllib, re
from bs4 import BeautifulSoup

serie = raw_input("Introduzca el nombre de la serie: ")
sitio = raw_input("BUscar en Rarbg o Argenteam?: ")


parametros = urllib.urlencode({'search': serie })
cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
abrir_conexion = httplib.HTTPConnection(sitio +":80")
abrir_conexion.request("POST", "/search", parametros, cabeceras)
respuesta = abrir_conexion.getresponse()
ver_source = respuesta.read()
abrir_conexion.close()
soup = BeautifulSoup(ver_source , 'html.parser')
url = soup('a')
for link in url:
	print link
	






