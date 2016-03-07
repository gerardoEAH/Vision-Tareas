import BasicOperations as bo
from PIL import Image
from sys import argv


def filtroMediana(nombreImagen = argv[1]):
	#obtiene nombre de imagen como parametro
	#Abre la imagen, obtiene su ancho, alto y sus pixeles
	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles = img.load()
	#La transforma a escala de grises
	bo.toGrayScale(pixeles, ancho, alto)
	fMediana(pixeles, ancho, alto, img)

#[i-1, j-1]		[i, j-1]	[i+1, j-1]			[1][4][6]	
#[i-1, j]		[i,j]		[i+1, j]	----->	[2][0][7]
#[i-1, j+1]		[i, j+1]	[i+1, j+1]			[3][5][8]
def fMediana(pixeles, ancho, alto,img):
	for i in range(ancho):
		    for j in range(alto):
		    	#1
		    	if i - 1 < 0 or j - 1 < 0:
		    		p1 = pixeles[i,j][0]
		    	else:
		    		p1 = pixeles[i-1,j-1][0]

				#2
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

		    	#Obtener mayor y menor de los pixeles cercanos
		    	minp = min(p1, p2, p3, p4, p5, p6, p7, p8)
		    	maxp = max(p1, p2, p3, p4, p5, p6, p7, p8)

		    	#Selecciona el nuevo pixel en base a los minimos y maximos cercanos
		    	pixel = pixeles[i,j][0]
		    	if pixel < minp:
		    		newpx = minp
		    	elif pixel > maxp:
		    		newpx = maxp
		    	else:
		    		newpx = pixel

		    	#Coloca el nuevo valor
		    	pixeles[i,j] = (newpx, newpx, newpx)


	#fMediana(pixeles, ancho, alto,img)
	new = "filtroMediana.jpg"
	img.save(new)
	print "Imagen generada con exito 'filtroMediana.jpg'"

