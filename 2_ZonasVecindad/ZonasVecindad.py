#Este codigo es funcional. Pero en mi opinion le falta optimizarse mas.
#Fue lo que realice un poco a prisas y es la version inicial.

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

##Funciones que se usaran##

#Esta funcion mira los vecinos del pixel (i, j) y si estos estan dentro del rango los une a a la misma zona.
def vecinos(i, j):

	#Variables globales que se deben usar
	global value
	global n
	global total

	#Se verifica que el pixel adyacente se encuentre en los rangos de la imagen.
	#Despues se checa que no tengo zona, es decir su zona sea 0
	#Por ultimo se checa si la diferencia de intensidades este dentro del rango.
	#Y si es asi, lo coloca dentro de la zona 'n'. Y disminuimos en uno el total de pixeles que faltan de unir a una zona	

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

#Esta funcion nos regresa verdadero si alguno de los vecinos del pixel (i,j) pertecen a la zona 'n' que estamos trabajando
#De lo contrario nos regresa falso
def isVecino(i, j):
	
	#Variable global de la zona
	global n

	#Se verifica que el pixel que queremos ver exista dentro de los limites de la imagen
	#Despues se checa si pertenecen a la zona y si es asi nos regresa verdadero

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

	#Si no regresa verdadero porque no tiene vecinos de la zona nos regresa falso.
	return False


#Comienza a correr el algoritmo

#Declarar variables y seleccionar el pixel inicial como el  (0,0)
n = 1 #La zona. Se inicia en 1 y cuando termine de encontrar una zona se incrementa para la siguiente zona
i = 0
j = 0
value = img.item(i,j) 	#Valor del pixel con el cual comparar los demas
zones[i,j] = n		#Pixel inicial esta en la primera zona
selected = True		#Ya se selecciono un pixel y zona asi que es verdadero
i += 1			#Nos movemos al pixel adyacente
total = ancho * alto 	#Total de pixeles


#Iterara hasta que no haya pixeles sin zona
while total > 1:
	#Detiene este ciclo cuando recorra toda la imagen
	while j <= alto: 
		#Que no se pase del limite de la imagen
		if i + 1 <= ancho and j + 1 <= alto:
			#Si el pixel no tiene zona y no hay seleccion de nueva zona.
			if zones[i,j] == 0 and not(selected):
				n += 1			#Incrementa n para empezar con la siguiente zona
				value = img.item(i,j)	#Guarda el valor del pixel actual para las comparaciones
				zones[i,j] = n		#Vuelve el pixel actual en la nueva zona
				total -= 1		#Al tener un pixel nuevo en zona, disminuimos total para saber cuantos pixeles faltan
				selected = True		#Como seleccionamos una nueva zona volvemos selected verdadero

			#Si no tiene zona, pero si se ha seleccionado una nueva zona
			elif zones[i,j] == 0 and selected:
				#Si tiene vecinos con zona actual
				if isVecino(i,j):
					#Si entra en el rango para pertenecer a la zona
					if (value - img.item(i,j))**2 < thresh:
						zones[i,j] = n	#Vuelve el pixel actual en la zona 
						total -= 1	#Al tener un pixel nuevo en zona, disminuimos total para saber cuantos pixeles faltan
						vecinos(i,j)	#Checa si sus vecinos pertenecen a la zona.
			
			#Si la zona del pixel actual pertenece ya a la zona, checa sus vecinos para ver si tambien pertenecen
			elif zones[i,j] == n:
				vecinos(i,j)

		#Nos movemos en la imagen
		if i + 1 < ancho:
			i += 1
		else:
			i = 0
			j += 1

	#Al teminar de ver toda la imagen y llenamos la zona, proseguimos a repetir el proceso con una nueva zona.
	selected = False	#No tenemos pixel seleccionado asi que toma el valor de falso
	i = 0			#Volvemos a movernos por la imagen desde el inicio
	j = 0


#OPCIONAL
#Guargamos el archivo de la matrix en un archivo de texto, donde cada pixel es el numero de zona y estan divididos por '-'
np.savetxt('zonas.txt', zones, fmt='%1s', delimiter='-') 
print "Text File saved."


