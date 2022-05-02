from msilib.schema import Class
from tkinter import *
from tkinter import ttk


class Personaje():
    def __init__(
        self, 
        npc=False, 
        pos=(0,0),
        size=15,
        icono='green',
    ):
        self.size = size
        self.icono = icono
        self.destino = [pos[0], pos[1]]
        self.origen = (None, None)
        

    def movimiento(self, direccion):
        self.origen = (self.destino[0], self.destino[1])
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


class Terreno():
    ''' self.area tiene la siguiente configuracion:
    [
        [(pos[0], pos[1], size[0], size[1], icono), ...],
        [(pos[0], pos[1], size[0], size[1], icono), ...],
        ...,
    ]
    '''
    def __init__(self, posicion=(0,0), size=15, icono='black'):
        self.cols = 30
        self.rows = 30
        self.size = size
        self.pos = posicion
        self.icono = icono
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
    for filas in terreno.area:
        for col in filas:
            if (col[0], col[1]) == jugador.origen:
                view.create_rectangle(
                    col[0],
                    col[1],
                    col[2],
                    col[3],
                    fill=col[4]
                )
    view.create_rectangle(
                jugador.destino[0],
                jugador.destino[1],
                jugador.destino[0] + jugador.size,
                jugador.destino[1] + jugador.size,
                fill=jugador.icono
            )


root = Tk()
root.title('Rogue-Like')
root.option_add('*tearOff', FALSE)
# root.minsize(300, 200)

view = Canvas(root, width=450, height=450, background='black')
view.grid(column=0, row=0)

jugador = Personaje()
terreno = Terreno(icono='grey')
dibujar()

root.bind('<Right>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Left>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Up>', lambda e:[jugador.movimiento(e.keysym), dibujar()])
root.bind('<Down>', lambda e:[jugador.movimiento(e.keysym), dibujar()])

root.mainloop()