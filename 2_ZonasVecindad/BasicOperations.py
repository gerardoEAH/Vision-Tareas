from PIL import Image

#Vuelve la imagen en escala de grises
def toGrayScale(pixeles, ancho, alto):
	for i in range(ancho):
	    for j in range(alto):
	    	pixel = pixeles[i,j]
	    	newpx = int(pixel[0]*0.299)+int(pixel[1]*0.587)+int(pixel[2]*0.114)   
	    	pixeles[i,j] = (newpx, newpx, newpx)
	return pixeles

