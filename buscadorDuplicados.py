#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, hashlib, sqlite3
#inicializamos la db
conn = sqlite3.connect('ficheros.sqlite3')
conn.text_factory = str
cur = conn.cursor()
#eliminamos la tabla si existe
cur.execute('DROP TABLE IF EXISTS ficheros')
cur.execute("CREATE TABLE ficheros (id	INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT, hash	TEXT)")
conn.commit()
#funcion que calcula el hash
def hashArchivo(archivo):
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open(archivo, 'rb')as fichero:
		buf = fichero.read(BLOCKSIZE)
		while len(buf) > 0:
			hasher.update(buf)
			buf = fichero.read(BLOCKSIZE)
	return hasher.hexdigest()
#inicio del script
print "Buscador de archivos duplicados"
#Obtencion de archivos en el directorio
cont = 1
for (nombredir, dirs, ficheros) in os.walk('.'):
	for nombrefichero in ficheros:
		print nombredir
		print "Calculando Hash para ", nombrefichero
		cur.execute("INSERT INTO ficheros (nombre, hash) VALUES(? , ?)", 
			(nombredir+'/'+nombrefichero, hashArchivo(nombredir+'/'+nombrefichero)))
		conn.commit()
		print "Agregado archivo Nro: ", cont, " - ", nombrefichero
		cont = cont + 1
#Realizando consulta para ir eliminando archivos duplicados y dejar solo el original
print "Eliminando repetidos, y solo dejando el original"
cur.execute('''
	WITH repetidos AS (SELECT min(id) as id, hash FROM ficheros GROUP BY hash having COUNT(*)>1)
SELECT * FROM ficheros WHERE id NOT IN(SELECT id FROM repetidos) AND hash IN (SELECT hash FROM repetidos)''')
conn.commit()
for i in cur:
	print "Borrando archivo ", i[1]
	os.delete(i[2])
print "Archivos duplicados realizado exitosamente"