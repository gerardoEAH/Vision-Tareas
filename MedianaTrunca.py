import BasicOperations as bo
import estadistica as est
import FiltroMediana as mediana
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
averaI = est.average(est.doList(pixeles, ancho, alto))

####
veces = ((ancho * alto)**0.25) + 8
print str(veces)
z = 0
while z < veces:
	for i in range(ancho):
		for j in range(alto):
			p = []
			avera = 10
			moda = 0
			contador = 0
			while ((avera - moda)**2 > 24):
				#1
				if i - 1 < 0 or j - 1 < 0:
				 	p1 = pixeles[i,j][0]
				else:
					p.append(pixeles[i-1,j-1][0])

				#2
				if i - 1 < 0:
					p2 = pixeles[i,j][0]
				else:
					p.append(pixeles[i-1,j][0])

				#3
				if i - 1 < 0 or j + 1 > alto - 1:
					p3 = pixeles[i,j][0]
				else:
					p.append(pixeles[i-1,j+1][0])

				#4
				if j - 1 < 0:
					p4 = pixeles[i,j][0]
				else:
					p.append(pixeles[i,j-1][0])

				#5
				if j + 1 > alto - 1:
					p5 = pixeles[i,j][0]
				else:
					p.append(pixeles[i,j+1][0])

				#6
				if i + 1 > ancho - 1 or j - 1 < 0:
					p6 = pixeles[i,j][0]
				else:
					p.append(pixeles[i+1,j-1][0])

				#7
				if i + 1 > ancho - 1:
				 	p7 = pixeles[i,j][0]
				else:
					p.append(pixeles[i+1,j][0])

				#8
				if i + 1 > ancho - 1 or j + 1 > alto - 1:
					p8 = pixeles[i,j][0]
				else:
					p.append(pixeles[i+1,j+1][0])

				#Obtener mayor y menor de los pixeles cercanos		
				minp = min(p)
				maxp = max(p)

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

				avera = est.average(p)
				moda = est.moda(p)
				contador += 1
				if contador > 1:
					avera = 0
					moda = 0
	z += 1
###

#Guarda Imagen
new = "medianaTrunca.jpg"
img.save(new)
