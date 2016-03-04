
def average(pixeles, ancho, alto):
	suma = 0
	for i in range(ancho):
		    for j in range(alto):
		    	suma += pixeles[i,j][0]
	return suma / (ancho * alto)

def varianza(pixeles, ancho, alto, avera):
	#avera = average(pixeles, ancho, alto)
	suma = 0
	for i in range(ancho):
		    for j in range(alto):
		    	suma += (pixeles[i,j][0] - avera)**2
	return suma / (ancho * alto)