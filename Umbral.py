import BasicOperations as bo;
from PIL import Image
from sys import argv

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]

#Selecciona el umbral
thresh = 0;
while thresh < 1 or thresh > 255:
	thresh = input("Ingresa el umbral (1-255) : ")

#Obtiene la imagen,el tamano, y los pixeles
img = Image.open(nombreImagen)
ancho,alto = img.size
pixeles = img.load()

#Los pixeles a color los cambia a Escala de Grises
bo.toGrayScale(pixeles, ancho, alto)

#Umbral Blanco-Negro
for i in range(ancho):
	    for j in range(alto):
	    	pixel = pixeles[i,j]
	    	if pixel[0] > thresh:
	    		newpx = 255
	    	else:
	    		newpx = 0  	
	    	pixeles[i,j] = (newpx, newpx, newpx)

new = "umbral.jpg"
img.save(new)
