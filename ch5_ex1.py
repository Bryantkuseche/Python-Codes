contador = 0
media = 0.0
salida = True
while salida != False:
	entrada = raw_input("Introduce un numero: ")
	try:
		if entrada == "fin" or entrada == "Fin" or entrada == "FIN":
			break
		else:
			media = media + float(entrada)
			contador = contador + 1
			continue
	except:
		print "Entrada Invalida"
		continue
print media ," " , contador , " ",  (media / contador)