from tkinter import *

from w_enter    import W_enter
from w_exit     import W_exit
from w_monthly  import W_monthly
from w_tariff   import W_tariff
from w_history  import W_history

class W_index:
    def __init__(self, window, title, geometry):
        self.wind = window
        self.wind.title(title)
        self.wind.geometry(geometry)

        # crea un frame container para los botones

        frame = LabelFrame(self.wind, text='menu')
        frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40) 

        # Crea un boton de ingreso de carros

        def open_enter():
            w_enter = Tk()
            W_enter(w_enter,"ingreso","350x250")

        Button(frame,text='ingreso',command= open_enter).grid(row=0, column=0)

        # Crea un boton de salida de carros

        def open_exit():
            w_exit = Tk()
            W_exit(w_exit,"salida","350x250")

        Button(frame,text='salida',command= open_exit).grid(row=1, column=0)

        # Crea un boton de para hacer una mensualidad

        def open_monthly():
            w_monthly = Tk()
            W_monthly(w_monthly,"mensualidad","350x250")

        Button(frame,text='mensualidad',command= open_monthly).grid(row=2, column=0)

        # Crear un boton para modificar las tarifas

        def open_tariff():
            w_tariff = Tk()
            W_tariff(w_tariff,"tarifas","450x250")

        Button(frame,text='tarrifas',command= open_tariff).grid(row=3, column=0)

        # Crear un boton de historial de carros que han pasado por el parqueadero

        def open_history():
            w_history = Tk()
            W_history(w_history,"historial","900x250")

        Button(frame,text='historial',command= open_history).grid(row=4, column=0)