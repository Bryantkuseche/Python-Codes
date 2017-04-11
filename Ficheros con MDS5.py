#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, hashlib

duplicado = dict()
contador = 1 #Contador de inicio para saber el numero de archivos
for (nombredir, dirs, ficheros) in os.walk('.'):
	for nombrefichero in ficheros: 
		if nombrefichero.endswith('.mp3'): 
			contador = contador + 1 
			elfichero = os.path.join(nombredir,nombrefichero)
			manf = open(elfichero , 'r')
			datos = manf.read()
			manf.close()
			checksum = hashlib.md5(datos).hexdigest()
			print nombrearchivo , checksum
			duplicado[checksum] = nombredir
			if checksum in duplicado == True:
				print nombrearchivo , duplicado[checksum]
			else:
				continue
