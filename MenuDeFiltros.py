from Tkinter import *
import Image,ImageTk
import ImageDraw
from sys import argv
from time import * 
import numpy
from FiltroModa import escalaGrisesModa #Importar función de librería.

class Aplicacion(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self,parent) 
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Ventana')
        self.pack(fill=BOTH, expand=1)
        #Área de botones
        self.moda = Button(text='Filtro Mooooda', command = self.boton_FiltroModa).pack(side=LEFT)

    #Funciones de cada boton.    
    def boton_FiltroModa(self):
        escalaGrisesModa()
        
def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()
    
main()

