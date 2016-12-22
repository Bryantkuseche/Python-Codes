import os, re, sqlite3
print "Buscador de trackers vivos"
nombre_archivo = raw_input("Introduzca nombre de archivo: ")
if len(nombre_archivo) < 1:
	print "no se selecciono ningun archivo, saliendo"
	quit()
else:
	print "Buscando trackers y comprobando, puede llevar algunos minutos"

print "Creando base de datos"
conn = sqlite3.connect('trackersdb.sqlite')
puntero = conn.cursor()

#Dando formato a una db

puntero.executescript('''

DROP TABLE IF EXISTS Trackers;

CREATE TABLE Trackers(
	Tracker	TEXT NOT NULL UNIQUE)
''')

#Abriendo archivo de texto y procesando

archivo = open(nombre_archivo).read()
http_lista = list()
udp_lista = list()
for link in archivo:
	link.rstrip()
	if re.search('http://.*', link):
		http_lista.append(link)
	elif re.search('udp://.*', link):
		udp_lista.append(link)

print "Hay " , (len(http_lista) + len(udp_lista)), "Trackers en el archivo"
print "Se estan verificando, espere por favor, esto puede tardar varios minutos"

for link_vivo in http_lista:
	hostname = link_vivo
	response = os.system('ping -c 1' + hostname)
	if response == 0:
		puntero.execute('''INSERT OR IGNORE INTO Trackers (hostname)
		VALUES ( ? )''', (hostname, ))
	else:
		print hostname , "Esta caido!"
	conn.commit() 

