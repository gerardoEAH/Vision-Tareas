import BasicOperations as bo
from PIL import Image
from sys import argv
import os


def escalaGrisesModa(nombreImagen= argv[1]):
	imagen = Image.open(nombreImagen)
	ancho,alto= imagen.size
	pixeles = imagen.load()
	bo.toGrayScale(pixeles,ancho,alto)
	imgModa(imagen, ancho, alto, pixeles)

def imgModa(imagen, ancho, alto,pixeles):
	for i in range(ancho):
		for j in range(alto):
			if i - 1 < 0 or j - 1 < 0:
				p1 = pixeles[i,j][0]
			else:
				p1 = pixeles[i-1,j-1][0]
			if i - 1 < 0:
				p2 = pixeles[i,j][0]
			else:
				p2 = pixeles[i-1,j][0]

	    	#3
	    	if i - 1 < 0 or j + 1 > alto - 1:
	    		p3 = pixeles[i,j][0]
	    	else:
	    		p3 = pixeles[i-1,j+1][0]

	    	#4
	    	if j - 1 < 0:
	    		p4 = pixeles[i,j][0]
	    	else:
	    		p4 = pixeles[i,j-1][0]

	    	#5
	    	if j + 1 > alto - 1:
	    		p5 = pixeles[i,j][0]
	    	else:
	    		p5 = pixeles[i,j+1][0]

	    	#6
	    	if i + 1 > ancho - 1 or j - 1 < 0:
	    		p6 = pixeles[i,j][0]
	    	else:
	    		p6 = pixeles[i+1,j-1][0]

	    	#7
	    	if i + 1 > ancho - 1:
	    		p7 = pixeles[i,j][0]
	    	else:
	    		p7 = pixeles[i+1,j][0]

	    	#8
	    	if i + 1 > ancho - 1 or j + 1 > alto - 1:
	    		p8 = pixeles[i,j][0]
	    	else:
	    		p8 = pixeles[i+1,j+1][0]

	    	listaModa=[p1,p2,p3,p4,p5,p6,p7,p8]
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
	    	newpx = k
	    	pixeles[i,j] = (newpx, newpx, newpx)

	new ="filtroModa.jpg"
	print "Filtro Moda terminado."
	imagen.save(new)

