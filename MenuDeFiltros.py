from Tkinter import *
import Image,ImageTk
import ImageDraw
from sys import argv
from time import * 
import numpy
from FiltroModa import escalaGrisesModa

class Aplicacion(Frame):
    
    def __init__(self,parent):
        Frame.__init__(self,parent) 
        self.parent = parent
        self.initUI()
         
    def initUI(self):
        self.parent.title('Ventana')
        self.pack(fill=BOTH, expand=1)
        self.moda = Button(text='Filtro Mooooda', command = self.boton_FiltroModa).pack(side=LEFT)
    def boton_FiltroModa(self):
        escalaGrisesModa()

        #FiltroModa.escalaGrises()
def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()
    
main()

