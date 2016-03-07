import BasicOperations as bo
from PIL import Image
from sys import argv


def escalaGrises(nombreImagen=argv[1]):

	img = Image.open(nombreImagen)
	ancho,alto = img.size
	pixeles= img.load()
	bo.toGrayScale(pixeles,ancho,alto)

	ValleGlobal(ancho,alto,pixeles)


def ValleGlobal(img,ancho,alto,pixeles):

