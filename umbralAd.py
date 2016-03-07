#TODO Refactorizar el codigo, poner los metodos de umbral en un solo archivo
import BasicOperations as bo
from PIL import Image
from sys import argv

def umbralAdaptativo(hist, total):

	sum = 0.0
	sumB = 0.0
	wB = 0.0
	wB = 0.0
	mB = 0.0
	mF = 0.0
	max = 0.0
	between = 0.0
	tresh1 = 0.0
	thresh2 = 0.0

	for x in range(1, 255):
		sum += x * hist[x]

	for x in range(1, 255):
		wB += hist[x]
		if wB == 0:
			continue
		wF = total - wB
		if wF == 0:
			break
		sumB += x * hist[x]
		mB = sumB / wB
		mF = (sum - sumB) / wF
		between = wB * wF * (mB - mF) * (mB - mF)
		if (between >= max):
			tresh1 = x
			if between > max:
				thresh2 = x
			max = between

	return (tresh1 + thresh2) / 2

def umbral():
	nombreImagen = argv[1]

	#Obtiene la imagen,el tamano, y los pixeles
	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles = img.load()

	#Los pixeles a color los cambia a Escala de Grises
	bo.toGrayScale(pixeles, ancho, alto)

	#Histograma y el numero total de pixeles
	total = ancho * alto
	hist = img.histogram()

	#Obtiene el umbral 
	thresh = umbralAdaptativo(hist, total)

	#Redibuja la imagen con el umbral obtenido
	for i in range(ancho):
		    for j in range(alto):
		    	pixel = pixeles[i,j]
		    	if pixel[0] > thresh:
		    		newpx = 255
		    	else:
		    		newpx = 0  	
		    	pixeles[i,j] = (newpx, newpx, newpx)

	new = "umbralAdaptativo.jpg"
	img.save(new)
	print "Imagen generada con exito 'umbralAdaptativo.jpg'"

if __name__ == '__main__':
	umbral()
