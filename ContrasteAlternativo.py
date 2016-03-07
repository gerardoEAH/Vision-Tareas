#Es un contraste con colores mas obscuros

import BasicOperations as bo;
from PIL import Image
from sys import argv

def contrasteObscuro():

	#obtiene nombre de imagen como parametro
	nombreImagen = argv[1]

	#Pide la gamma y beta que se usara
	gamma = input("Gamma: ")
	beta = input("Beta: ")


	#Abre la imagen, obtiene su ancho, alto y sus pixeles
	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles = img.load()

	#La transforma a escala de grises
	bo.toGrayScale(pixeles, ancho, alto)

	#Anade contraste a la imagen
	for i in range(ancho):
		    for j in range(alto):
		    	pixel = pixeles[i,j]
		    	newpx = pixel[0] / gamma - beta
		    	#Valida los valores
		    	if newpx < 0:
		    		newpx = 0
		    	elif newpx > 255:
		    		newpx = 255
		    	else:
		    		newpx = pixel[0]
		    	#Coloca el nuevo valor
		    	pixeles[i,j] = (newpx, newpx, newpx)

	new = "contrasteObscuro.jpg"
	img.save(new)
	print "Imagen generada con exito 'contrasteObscuro.jpg'"
