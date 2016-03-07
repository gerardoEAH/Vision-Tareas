import BasicOperations as bo
import estadistica as est
import math
from PIL import Image
from sys import argv

def umbMaxProb():

	#obtiene nombre de imagen como parametro
	nombreImagen = argv[1]

	#Abre la imagen, obtiene su ancho, alto y sus pixeles
	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles = img.load()

	#La transforma a escala de grises
	bo.toGrayScale(pixeles, ancho, alto)

	#Obtener promedio y varianza
	promedio = est.average(pixeles, ancho, alto)
	varianza = est.varianza(pixeles, ancho, alto, promedio)

	#Formula Umbral de Maxima Probabilidad
	for i in range(ancho):
			    for j in range(alto):
			    	pixel = pixeles[i,j][0]
			    	newpx =  int((1 / ((2 * math.pi * varianza))**0.5)**(-(((promedio - pixel)**2) / (varianza * 2))))
			    	pixeles[i,j] = (newpx, newpx, newpx)

	new = "UmbralMaxProbabilidad.jpg"
	img.save(new)
	print "Imagen generada con exito 'UmbralMaxProbabilidad.jpg'"
