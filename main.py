from msilib.schema import Class
from tkinter import *
from tkinter import ttk


class Personaje():
    def __init__(
        self, 
        npc=False, 
        pos=[0,0],
        size=15,
        icono='geen',
    ):
        self.size = size
        self.icono = icono
        self.destino = pos
        self.origen = []
        

    def movimiento(self, direccion):
        self.origen = self.destino.copy()
        match direccion:
            case 'Right':
                self.destino[0] = self.destino[0] + self.size
                # despues cambiar 30 por num_cols y 15 por casilla_sx
                if self.destino[0] > 30 * 15: 
                    self.destino[0] = (30 * 15) - 15
            case 'Left':
                self.destino[0] = self.destino[0] - self.size
                if self.destino[0] < 0:
                    self.destino[0] = 0
            case 'Up':
                self.destino[1] = self.destino[1] - self.size
                if self.destino[1] < 0:
                    self.destino[1] = 0
            case 'Down':
                self.destino[1] = self.destino[1] + self.size
                # despues cambiar 30 por num_rows y 15 por casilla_sy
                if self.destino[1] > 30 * 15:
                    self.destino[1] = (30 * 15) - 15
    

    def get_ubicacion(self):
         return (
                self.pos[0],
                self.pos[1],
                self.pos[0] + self.size[0],
                self.pos[1] + self.size[1],
                'green'
         )


class Terreno():
    ''' self.area tiene la siguiente configuracion:
    [
        [(pos[0], pos[1], size[0], size[1], icono), ...],
        [(pos[0], pos[1], size[0], size[1], icono), ...],
        ...,
    ]
    '''
    def __init__(self, posicion=(0,0), size=15):
        self.cols = 30
        self.rows = 30
        self.size = size
        self.pos = posicion
        self.icono = 'black'
        self.area = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append([
                    c * self.size,
                    r * self.size,
                    (c + 1) * self.size,
                    (r + 1) * self.size,
                    self.icono,
                ])
            self.area.append(row)
  

    def get_area(self):
        return self.area


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
    t = terreno.get_area()
    for filas in t:
        for columnas in filas:
            view.create_rectangle(
                columnas[0],
                columnas[1],
                columnas[2],
                columnas[3],
                fill=columnas[4]
            )
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

jugador = Personaje()
terreno = Terreno()

root.bind('<Right>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Left>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Up>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Down>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
dibujar()

root.mainloop()