from PIL import Image
from sys import argv

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]
img = Image.open(nombreImagen)
#obtiene dimensiones de imagen
ancho,alto = img.size
pixeles = img.load()
for i in range(ancho):
    for j in range(alto):
    	a = pixeles[i,j]
    	s = int(a[0]*0.299)+int(a[1]*0.587)+int(a[2]*0.114)    	
    	pixeles[i,j] = (s,s,s)

new = 'grises.jpg'
img.save(new)
