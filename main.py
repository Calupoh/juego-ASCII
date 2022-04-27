from tkinter import *

from requests import options

pixel_size = (15, 15)

def ajustar_cuadricula(col=30, row=30):
    sizex = view['width']
    sizey = view['height']
    pixel_size = (sizex/col, sizey/row)


root = Tk()
root.title('Rogue-Like')
root.option_add('*tearOff', FALSE)
# root.minsize(300, 200)

view = Canvas(root, width=450, height=450, background='black')
view.grid(column=0, row=0)
print(view['width'])
view.create_rectangle(0,0,15,15, fill='grey', outline='grey')
view.create_rectangle(15,0,30,15, fill='green', outline='green')

root.mainloop()