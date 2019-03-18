lista = []
salida = True
while salida != False:
	entrada = raw_input("Introduce un numero: ")
	try:
		if entrada == "fin" or entrada == "Fin" or entrada == "FIN":
			break
		else:
			lista.append(int(entrada));
			continue
	except:
		print "Entrada Erronea"
		continue

lista.sort()
print max(lista), " " , min(lista)