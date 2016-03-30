import numpy as np
from sys import argv
import cv2


#obtiene nombre de imagen como parametro
nombreImagen = argv[1]

#Umbral de diferencia entre zonas
thresh = 256
while thresh < 1 or thresh > 254:
	thresh = input("Ingresa la diferencia entre vecindades (1 - 254): ")

thresh = thresh**2

#Lee la imagen en escala de grises
img = cv2.imread(nombreImagen,0)

#La imagen de escala de grise se vuelve de 16 tonos de gris.
ancho, alto = img.shape
for i in range(ancho):
	    for j in range(alto):
		#Formula mas efectiva que condiciones para dividir en los 16 tonos
		#Ej. 248 se vuelve 255 entonces... 248 / 16 = 15.5 ... 15 * 17 = 255
		newpx = (int(img.item(i,j) / 16)) * 17
		img.itemset((i,j), newpx)

#Guarda la imagen
cv2.imwrite(nombreImagen + 'TONOS.jpg', img)
print "Guardando imagen de tonos"

###### Zonas de Vecindad ######
#Crear array de Zonas donde el valor de todo es 0
zones = np.zeros(img.shape, dtype=np.int)
np.savetxt('zonas1.txt', zones, delimiter='-') 

###


##
###
#FUNCIONES

def vecinos(i, j):

	global value
	global n
	global total

	if i - 1 >= 0:
		if zones[i - 1, j] == 0:
			if (value - img.item(i,j))**2 < thresh:
				zones[i - 1,j] = n
				total -= 1

	if j - 1 >= 0:
		if zones[i, j - 1] == 0:
			if (value - img.item(i,j))**2 < thresh:
				zones[i,j - 1] = n
				total -= 1

	if i + 1 < ancho:
		if zones[i + 1, j] == 0:
			if (value - img.item(i,j))**2 < thresh:
				zones[i + 1,j] = n
				total -= 1

	if j + 1 < alto:
		if zones[i, j + 1] == 0:
			if (value - img.item(i,j))**2 < thresh:
				zones[i,j + 1] = n
				total -= 1

def isVecino(i, j):
	global n

	if i - 1 >= 0:
		if zones[i - 1, j] == n:
			return True

	if j - 1 >= 0:
		if zones[i, j - 1] == n:
			return True

	if i + 1 < ancho:
		if zones[i + 1, j] == n:
			return True

	if j + 1 < alto:
		if zones[i, j + 1] == n:
			return True

	return False

##3
#Itera por la imagen

#La zona. Se inicia en 1 y cuando termine de encontrar una zona se incrementa para la siguiente zona
n = 1

#Declarar variables y seleccionar el pixel (0,0)

px = 0
py = 0
i = px
j = py
value = img.item(px,py)
zones[px,py] = n
selected = True
i += 1
total = ancho * alto

while total > 10:

	while j <= alto:
		if i + 1 <= ancho and j + 1 <= alto:
			if zones[i,j] == 0 and not(selected):
				n += 1
				value = img.item(i,j)
				zones[i,j] = n
				total -= 1
				selected = True
				print "Total: " + str(total)
				print "Zona: " + str(n)
				np.savetxt('zonas.txt', zones, fmt='%1s', delimiter='-') 

			elif zones[i,j] == 0 and selected:
				###
				if isVecino(i,j):
					if (value - img.item(i,j))**2 < thresh:
						zones[i,j] = n
						total -= 1
						vecinos(i,j)
			
				
			elif zones[i,j] == n:
				vecinos(i,j)

		if i + 1 < ancho:
			i += 1
		else:
			i = 0
			j += 1
	selected = False
	i = 0
	j = 0

"""
	if zones(i,j) == 0 and not(selected):
		px = i
		py = j
		value = img.item(i,j)
		zones(i, j) = n
		selected = true
		if i + 1 < ancho:
		i += 1
		else:
		j += 1

	elif zones(i,j) == 0 and selected:
		if (value - img.item(i,j))**2 < thresh:
			zones(i,j) = n
			
	
		if i + 1 <= ancho:
			i += 1
		else:
			i = px
			j += 1

	else:
		selected = false
		i = 0
		j = 0

"""


#########INTENTOS
"""
#Declarar variables y seleccionar el pixel (0,0)
px = 0
py = 0
i = px
j = py
value = img.item(px,py)
zones(px,py) = n
selected = true
i += 1
"""

###


"""
#Itera por la imagen
while j <= alto:
	if zones(i,j) == 0 and not(selected):
		px = i
		py = j
		value = img.item(i,j)
		zones(i, j) = n
		selected = true
		if i + 1 < ancho:
		i += 1
		else:
		j += 1

	elif zones(i,j) == 0 and selected:
		if (value - img.item(i,j))**2 < thresh:
			zones(i,j) = n
			
	
		if i + 1 <= ancho:
			i += 1
		else:
			i = px
			j += 1

	else:
		selected = false
		i = 0
		j = 0
"""
###

"""
n = 1
value = img.item(0,0)

def vecinos(i, j):

	global value
	global n

	if i - 1 >= 0 and zones[i - 1, j] == 0:
		if (value - img.item(i,j))**2 < thresh:
			zones[i - 1,j] = n
			vecinos(i - 1, j)

	if j - 1 >= 0 and zones[i,j - 1] == 0:
		if (value - img.item(i,j))**2 < thresh:
			zones[i,j - 1] = n
			vecinos(i, j - 1)

	if i + 1 <= ancho and zones[i + 1,j] == 0:
		if (value - img.item(i,j))**2 < thresh:
			zones[i + 1,j] = n
			vecinos(i + 1, j)

	if j + 1 <= alto and zones[i,j + 1] == 0:
		if (value - img.item(i,j))**2 < thresh:
			zones[i,j + 1] = n
			vecinos(i, j + 1)


	if i + 1 <= ancho and j + 1 <= alto:
		next = True
		while next:
			if i + 1 < ancho:
				i += 1
			else:
				i = 0
				j += 1
			
			if j > alto:
				next = False
				print "FIN"

			if zones[i,j] == 0:
				next = False
				value = img.item(i,j)
				n += 1
				vecinos(i, j)




vecinos(0,0)
"""


np.savetxt('zonas.txt', zones, fmt='%1s', delimiter='-') 
print "Text File saved."


