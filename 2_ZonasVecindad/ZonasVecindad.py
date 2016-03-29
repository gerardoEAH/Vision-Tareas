import numpy as np
from sys import argv
import cv2


#obtiene nombre de imagen como parametro
nombreImagen = argv[1]

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
