import BasicOperations as bo;
from PIL import Image
from sys import argv


def aclararImagen():

	#obtiene nombre de imagen como parametro
	nombreImagen = argv[1]

	#Selecciona el brillo a agregar
	x = -1;
	while x < 0:
		x = input("Ingresa la cantidad a aclarar (mayor a 0.0) : ")

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
		    	newpx = int(pixel[0] * x)    	
		    	pixeles[i,j] = (newpx, newpx, newpx)
		    	if newpx > max :
		    		max = newpx

	new = "aclaradoDeImagen.jpg"
	img.save(new)
	print "Imagen generada con exito 'aclaradoDeImagen.jpg'"
