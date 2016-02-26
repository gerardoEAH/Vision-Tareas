import BasicOperations as bo;
from PIL import Image
from sys import argv

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]

#Abre la imagen, obtiene su ancho, alto y sus pixeles
img = Image.open(nombreImagen)
ancho,alto = img.size
pixeles = img.load()

#La transforma a escala de grises
bo.toGrayScale(pixeles, ancho, alto)

#Vuelve Negativa la imagen
for i in range(ancho):
	    for j in range(alto):
	    	pixel = pixeles[i,j]
	    	newpx = 255 - pixel[0] 
	    	pixeles[i,j] = (newpx, newpx, newpx)


new = "negativo.jpg"
img.save(new)
