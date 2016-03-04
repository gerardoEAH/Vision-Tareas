import BasicOperations as bo;
from PIL import Image
from sys import argv
import random


def escalaGrises(nombreImagen=argv[1]):
	
	img = Image.open(nombreImagen)
	ancho,alto  =img.size
	pixeles = img.load()
	bo.toGrayScale(pixeles,ancho,alto)
	
	salYpimienta(img,ancho,alto,pixeles)


def salYpimienta(img,ancho,alto,pixeles):
    prob = 0
    prob = input("Dame la probabilidad entre 0-1: ")
    for i in range(ancho):
        for j in range(alto):
            r,g,b = img.getpixel((i,j))
            if random.random() < prob:
                sal_p = pixeles[i,j][0]
                if sal_p < 128:
                    sal_p = 255
                    img.putpixel((i,j),(sal_p, sal_p, sal_p))             
                else:
                    sal_p = 0
                    img.putpixel((i,j),(sal_p, sal_p, sal_p))   
            else:
                img.putpixel((i,j),(r, g, b))            
    print "se guardo" 
    new = "ruido.jpg"
    img.save(new)	           
    return img 
    

escalaGrises()




