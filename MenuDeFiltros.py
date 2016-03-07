from Tkinter import *
import Image,ImageTk
import ImageDraw
from sys import argv
from time import * 
import numpy
#Import de programas
from FiltroModa import escalaGrisesModa #Importar funcion de libreria
from FiltroMediana import filtroMediana
from AclararImagen import aclararImagen
from Brillo import brillo
from Contraste import contrasteClaro
from ContrasteAlternativo import contrasteObscuro
from Copiar import copiar
from Negativo import negativo
from salYpimienta import escalaGrisesRuido
from Umbral import umbral
from umbralAd import umbralAda
from UmbralMaxProbabilidad import umbMaxProb


class Aplicacion(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self,parent) 
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Actividad Fundamental 1')
        self.pack(fill=BOTH, expand=1)
        #Area de botones
        self.moda = Button(text='Filtro Modal', command = self.boton_FiltroModa).pack(side=LEFT)
        self.mediana = Button(text='Filtro Mediana', command = self.boton_FiltroMedia).pack(side=LEFT)
        self.aclarar = Button(text="Aclarar Imagen", command= self.boton_AclararImagen).pack(side=LEFT)
        self.brillo = Button(text ="Brillo", command= self.boton_Brillo).pack(side=LEFT)
        self.contrasteC = Button(text="Contraste claro", command = self.boton_ContrasteClaro).pack(side=LEFT)
        self.contraseOb= Button(text="Contraste Obscuro", command = self.boton_contrasteAlternativo).pack(side=LEFT)
        self.copiar = Button(text="Copiar imagen", command= self.boton_copiar).pack(side=LEFT)
        self.negativo = Button(text="Negativo imagen", command= self.boton_negativo).pack(side=LEFT)
        self.ruido= Button(text="Sal y Pimienta", command=self.boton_salYpimienta).pack(side=LEFT)
        self.umbral = Button(text="Umbral", command=self.boton_umbral).pack(side=LEFT)
        self.umbralAd= Button(text="Umbral Adaptativo", command= self.boton_umbralAd).pack(side=LEFT)
        self.umbralMax= Button(text="Umbral Maxima Probabilidad", command = self.boton_umbralMax).pack(side=LEFT)

    #Funciones de cada boton.    
    def boton_FiltroModa(self):
        print "Generando imagen..."        
        escalaGrisesModa()

    def boton_FiltroMedia(self):
	    print "Generando imagen..."        
	    filtroMediana()
    def boton_AclararImagen(self):
        print "Generando imagen..."
        aclararImagen()
    def boton_Brillo(self):
        print "Generando imagen..."
        brillo()
    def boton_ContrasteClaro(self):
        print "Generando imagen..."
        contrasteClaro()
    def boton_contrasteAlternativo(self):
        print "Generando imagen..."
        contrasteObscuro()
    def boton_copiar(self):
        print "Generando imagen..."
        copiar()
    def boton_negativo(self):
        print "Generando imagen..."
        negativo()
    def boton_salYpimienta(self):
        print "Generando imagen..."
        escalaGrisesRuido()
    def boton_umbral(self):
        print "Generando imagen..."
        umbral()
    def boton_umbralAd(self):
        print "Generando imagen..."
        umbralAda()
    def boton_umbralMax(self):
        print "Generando imagen..."
        umbMaxProb()

        


	
        
def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()
    
main()

