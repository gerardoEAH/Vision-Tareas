from PIL import Image
from sys import argv

#obtiene nombre de imagen como parametro
nombreImagen = argv[1]

#Abre la imagen, obtiene su ancho, alto y sus pixeles
img = Image.open(nombreImagen)
ancho,alto = img.size
pixeles = img.load()

new = "copia.jpg"
img.save(new)