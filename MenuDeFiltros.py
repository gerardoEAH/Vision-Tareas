from Tkinter import *
import Image,ImageTk
import ImageDraw
from sys import argv
from time import * 
import numpy
#Import de programas
from FiltroModa import escalaGrisesModa #Importar funcion de libreria
from FiltroMediana import filtroMediana

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

    #Funciones de cada boton.    
    def boton_FiltroModa(self):
	print "Generando imagen..."        
	escalaGrisesModa()

    def boton_FiltroMedia(self):
	print "Generando imagen..."        
	filtroMediana()
	
        
def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()
    
main()

