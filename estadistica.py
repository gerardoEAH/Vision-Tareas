
def average(lista):
	suma = 0
	for value in lista:
		suma += value
	return suma / len(lista)

def varianza(lista):
	avera = average(lista)
	suma = 0
	for value in lista:
		suma += (value - avera)**2
	return suma / len(lista)
