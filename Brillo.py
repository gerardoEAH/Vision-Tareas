import BasicOperations as bo;
from PIL import Image
from sys import argv

def brillo():

	#obtiene nombre de imagen como parametro
	nombreImagen = argv[1]

	#Selecciona el brillo a agregar
	brillo = 256;
	while brillo < -255 or brillo > 255:
		brillo = input("Ingresa el brillo (-255 a 255) : ")

	#Obtiene la imagen,el tamano, y los pixeles
	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles = img.load()

	#Los pixeles a color los cambia a Escala de Grises
	bo.toGrayScale(pixeles, ancho, alto)
	max = 0

	#Aumenta el brillo a la imagen
	for i in range(ancho):
		    for j in range(alto):
		    	pixel = pixeles[i,j]
		    	newpx = pixel[0] + brillo    	
		    	pixeles[i,j] = (newpx, newpx, newpx)
		    	if newpx > max :
		    		max = newpx

	#Normaliza la imagen para que un pixel no sobrepase los 255
	#if max > 255:
	#	bo.normalize(pixeles, max, ancho, alto)

	new = "brillo.jpg"
	img.save(new)
	print "Imagen generada con exito 'brillo.jpg'"
