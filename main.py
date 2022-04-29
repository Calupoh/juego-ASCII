from msilib.schema import Class
from tkinter import *
from tkinter import ttk

from requests import options

size_x = 15
size_y = 15


def ajustar_cuadricula(col=30, row=30):
    size_x = view['width']/col
    size_y = view['height']/row


class personaje():
    def __init__(self, padre=None, npc=False, posicion=(0,0), size=(15,15)):
        self.sizex = size[0]
        self.sizey = size[1]
        self.posx = posicion[0]
        self.posy = posicion[1]
        self.camara = padre
        self.dibujar()
        
    

    def movimiento(self, direccion):
        match direccion:
            case 'Right':
                self.posx = self.posx + self.sizex
            case 'Left':
                self.posx = self.posx - self.sizex
            case 'Up':
                self.posy = self.posy - self.sizey
            case 'Down':
                self.posy = self.posy + self.sizey
        self.dibujar()
    

    def dibujar(self):
        self.camara.create_rectangle(
                    self.posx,
                    self.posy,
                    self.posx + self.sizex,
                    self.posy + self.sizey,
                    fill='green'
                )


root = Tk()
root.title('Rogue-Like')
root.option_add('*tearOff', FALSE)
# root.minsize(300, 200)

view = Canvas(root, width=450, height=450, background='black')
view.grid(column=0, row=0)

jugador = personaje(view)
root.bind('<Right>', lambda e:[jugador.movimiento(e.keysym)])
root.bind('<Left>', lambda e:[jugador.movimiento(e.keysym)])
root.bind('<Up>', lambda e:[jugador.movimiento(e.keysym)])
root.bind('<Down>', lambda e:[jugador.movimiento(e.keysym)])

root.mainloop()