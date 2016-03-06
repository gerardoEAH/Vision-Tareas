#Devuelve el promedio de una imagen
def average(pixeles, ancho, alto):
	suma = 0
	for i in range(ancho):
		    for j in range(alto):
		    	suma += pixeles[i,j][0]
	return suma / (ancho * alto)

#Devuelve el promedio de una lista
def average(lista):
	suma = 0
	for i in lista:
		suma += i
	return suma / len(lista)

#Devuelve la varianza de una imagen
def varianza(pixeles, ancho, alto, avera):
	suma = 0
	for i in range(ancho):
		    for j in range(alto):
		    	suma += (pixeles[i,j][0] - avera)**2
	return suma / (ancho * alto)

#Devuelve una lista con todos los pixeles
def doList(pixeles, ancho, alto):
	pxList = []
	for i in range(ancho):
		    for j in range(alto):
		    	pxList.append(pixeles[i,j][0])
	return pxList

#Devuelve la moda de una lista
def moda(listaModa):
	repeticiones = 0
	for k in listaModa:
		apariciones = listaModa.count(k)
		if apariciones > repeticiones:
	    		repeticiones =	apariciones
	    	modas =[]
	for k in listaModa:
		apariciones = listaModa.count(k)
		if apariciones == repeticiones and k not in modas:
	    		modas.append(k)
	return k


