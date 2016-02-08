import cv2
from PIL import Image
from sys import argv

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]
img = Image.open(nombreImagen)

ancho,alto = img.size
pixeles = img.load()
umbral = input("Ingresa el umbral \n")
for i in range(ancho):
    for j in range(alto):

    	a = pixeles[i,j]
    	s = int(a[0]*0.299)+int(a[1]*0.587)+int(a[2]*0.114)    	
    	pixeles[i,j] = (s,s,s)
    	

    	b = pixeles[i,j]
    	if( b[0] > umbral):
    		s = 255
        else:
            s = 0
        pixeles[i,j] = (s,s,s)    

new = 'blancoNegro.png'
img.save(new)
new2 = cv2.imread('blancoNegro.png',-1)
cv2.imshow("Imagen",new2)
print "Oprima una tecla para cerrar"
cv2.waitKey(0)
cv2.destroyAllWindows();