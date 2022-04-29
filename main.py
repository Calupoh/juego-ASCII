from msilib.schema import Class
from tkinter import *
from tkinter import ttk


class personaje():
    def __init__(
        self, 
        padre=None, 
        npc=False, 
        posicion=(0,0), 
        size=(15, 15)
    ):
        self.sizex = size[0]
        self.sizey = size[1]
        self.posx = posicion[0]
        self.posy = posicion[1]
        self.camara = padre
        

    def movimiento(self, direccion):
        match direccion:
            case 'Right':
                self.posx = self.posx + self.sizex
                # despues cambiar 30 por num_cols y 15 por casilla_sx
                if self.posx > 30 * 15: 
                    self.posx = (30 * 15) - 15
            case 'Left':
                self.posx = self.posx - self.sizex
                if self.posx < 0:
                    self.posx = 0
            case 'Up':
                self.posy = self.posy - self.sizey
                if self.posy < 0:
                    self.posy = 0
            case 'Down':
                self.posy = self.posy + self.sizey
                # despues cambiar 30 por num_rows y 15 por casilla_sy
                if self.posy > 30 * 15:
                    self.posy = (30 * 15) - 15
    

    def get_ubicacion(self):
         return (
                self.posx,
                self.posy,
                self.posx + self.sizex,
                self.posy + self.sizey,
                'green'
         )


class terreno():
    pass


def ajustar_cuadricula(col=30, row=30):
    global casilla_sx
    global casilla_sy
    global num_cols
    global num_rows
    num_cols = col
    num_rows = row
    casilla_sx = view['width']/col
    casilla_sy = view['height']/row


def dibujar():
    j = jugador.get_ubicacion()
    view.create_rectangle(
                j[0],
                j[1],
                j[2],
                j[3],
                fill=j[4]
            )


root = Tk()
root.title('Rogue-Like')
root.option_add('*tearOff', FALSE)
# root.minsize(300, 200)

view = Canvas(root, width=450, height=450, background='black')
view.grid(column=0, row=0)

jugador = personaje(view)
root.bind('<Right>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Left>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Up>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Down>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
dibujar()

root.mainloop()