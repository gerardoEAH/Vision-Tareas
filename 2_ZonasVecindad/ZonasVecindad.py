import numpy as np
from sys import argv
import cv2

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]
img = cv2.imread(nombreImagen,0)
ancho, alto = img.shape
total = ancho * alto 	#Total de pixeles

#Umbral de diferencia entre zonas
thresh = 256
while thresh < 1 or thresh > 254:
	thresh = input("Ingresa la diferencia entre vecindades (1 - 254): ")

thresh = thresh**2

#Blur el cual no afecta tanto los bordes de una imagen.
img = cv2.bilateralFilter(img,9,75,75)

cv2.imwrite(nombreImagen + 'BLUR.jpg', img)
print "Blur Generado"

#La imagen de escala de grise se vuelve de 16 tonos de gris.
for i in range(ancho):
	    for j in range(alto):
		#Formula mas efectiva que condiciones para dividir en los 16 tonos
		#Ej. 248 se vuelve 255 entonces... 248 / 16 = 15.5 ... 15 * 17 = 255
		newpx = (int(img.item(i,j) / 16)) * 17
		img.itemset((i,j), newpx)

#Guarda la imagen
cv2.imwrite(nombreImagen + 'TONOS.jpg', img)
print "Imagen de Tonos guardada"


###### Zonas de Vecindad ######
#Crear array de Zonas y vecinos donde el valor de todo es 0
zones = np.zeros(img.shape, dtype=np.int)
veci = np.zeros((total,2), dtype=np.int)

#Esta funcion mira los vecinos del pixel (i, j) y si estos estan dentro del rango los une a a la misma zona.
def vecinos(i, j):

	#Variables globales que se deben usar
	global value
	global n
	global total
	global aux
	global veci
	global zones

	#Se verifica que el pixel adyacente se encuentre en los rangos de la imagen.
	#Despues se checa que no tengo zona, es decir su zona sea 0
	#Por ultimo se checa si la diferencia de intensidades este dentro del rango.
	#Y si es asi, guarda su posicion en el arreglo de vecinos, lo vuelve dentro de la zona actual 'n' 
	#y disminuye en uno el total faltante

	if i - 1 >= 0:
		if zones[i - 1, j] == 0:
			if (value - img.item(i - 1,j))**2 <= thresh:
				veci[aux, 0] = i - 1
				veci[aux, 1] = j
				aux += 1
				zones[i - 1,j] = n
				total -= 1

	if j - 1 >= 0:
		if zones[i, j - 1] == 0:
			if (value - img.item(i,j - 1))**2 <= thresh:
				veci[aux, 0] = i
				veci[aux, 1] = j - 1
				aux += 1
				zones[i,j - 1] = n
				total -= 1

	if i + 1 < ancho:
		if zones[i + 1, j] == 0:
			if (value - img.item(i + 1,j))**2 <= thresh:
				veci[aux, 0] = i + 1
				veci[aux, 1] = j
				aux += 1
				zones[i + 1,j] = n
				total -= 1


	if j + 1 < alto:
		if zones[i, j + 1] == 0:
			if (value - img.item(i,j + 1))**2 <= thresh:
				veci[aux, 0] = i
				veci[aux, 1] = j + 1
				aux += 1
				zones[i,j + 1] = n
				total -= 1


#Comienza a correr el algoritmo

#Declarar variables y seleccionar el pixel inicial como el  (0,0)
n = 1 #La zona. Se inicia en 1 y cuando termine de encontrar una zona se incrementa para la siguiente zona
aux = 0 #Auxiliar. Contador del indice de donde se agregaran los nuevos pixeles de la zona
k = 0 #Auxiliar. Contador dentro de los ciclos para entrar en el arreglo de vecinos
value = img.item(i,j) 	#Valor del pixel con el cual comparar los demas
zones[0,0] = n		#Pixel inicial esta en la primera zona
selected = True #Ya se selecciono un nuevo pixel y zona nueva
total -= 1 #Al haber seleccionado un pixen en una zona se disminuye en uno.
vecinos(0,0) #Checa los vecinos de nuestro pixel inicial

#Mientras aun haya pixeles sin zona...
while total > 1:
	#Mientras estemos en una posicion del arreglo donde sea diferente de (0,0), es decir hay pixeles donde no hemos visto sus vecinos
	while veci[k, 0] > 0 or veci[k, 1] > 0:
		#Checamos sus vecinos y aumentamos k en uno
		vecinos(veci[k,0], veci[k,1])
		k += 1

	#Al ya no haber mas pixeles posibles reiniciamos el arreglo de vecinos. Y ahora no hemos selecionado un nuevo pixel para continuar
	veci = np.zeros((total,2))
	selected = False

	#Recorremos la imagen hasta encontrar un pixel en sin zona.
	for p in range(ancho):
		for q in range (alto):
			if zones[p,q] == 0:
				#Mismo proceso inicial.
				n += 1 		#Aumentamos la zona en 1
				zones[p,q] = n 	#Pixel actual en la nueva zona 'n'
				total -= 1 		#Encontramos nuevo pixel asi que disminuimos en 1
				aux = 0			#Reiniciamos variables
				k = 0			#Reiniciamos variables
				value = img.item(p,q)	#Nuevo valor a comparar, el de nuestro nuevo pixel
				vecinos(p,q)	#Checamos sus vecinos
				selected = True	#Encontramos nuevo pixel
				break #Ya encontramos uno asi que terminamos de ver en la imagen.
		if selected:
			break #Ya encontramos uno asi que terminamos de ver en la imagen.


#OPCIONAL
#Guardamos el archivo de la matrix en un archivo de texto, donde cada pixel es el numero de zona y estan divididos por '-'
np.savetxt('zonas.txt', zones, fmt='%1s', delimiter='-') 
print "Archivo de texto de las Zonas de Vecindad Guardado"


#Colorear la imagen en 9 tonos diferentes
for i in range(ancho):
	    for j in range(alto):
	    	newpx = zones[i,j] * 32
	    	while newpx > 255:
	    		newpx = newpx - 256
	    	img.itemset((i,j), newpx)
	
#Guarda la imagen final
cv2.imwrite(nombreImagen + 'ZONAS.jpg', img)
print "Guardada imagen de Zonas de Vecindad"

