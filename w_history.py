from tkinter import *
from tkinter import ttk
from datetime import datetime
from window import Window
from database_manager import DatabaseManager


class W_history(Window):
    def __init__(self, window, title, geometry):
        super().__init__(window, title, geometry)

        

        def busqueda_placa():

            # esta funcion se encarga de buscar el registro de la pacas en el historial

            db =DatabaseManager()
            resultado = db.select_data('historial')

            return resultado

        # tabal de historial
        self.tree = ttk.Treeview(
            window ,height=12, columns=[f"#{n}" for n in range(1, 6)]
        )
        self.tree.grid(row= 1, column= 1)
        self.tree.heading('#0', text='fecha de ingreso  ')          
        self.tree.column('#0', width=140)
        self.tree.heading('#1', text='fecha de salida   ')
        self.tree.column('#1', width=140)
        self.tree.heading('#2', text='tipo de vehiculo  ')
        self.tree.column('#2', width=140)
        self.tree.heading('#3', text='placa             ')
        self.tree.column('#3', width=100)
        self.tree.heading('#4', text='mensualidad       ')
        self.tree.column('#4', width=120)
        self.tree.heading('#5', text='valor             ')
        self.tree.column('#5', width=120)

        tabla=busqueda_placa()
        longitud_tabla = len(tabla)

        for i in range(len(tabla)):

            # se cambia el formato de la fecha de ingreso y salida de numero a formato de fecha "YYYY-MM-DD HH:MM"

            registro = list(tabla[i])

            registro[1] = datetime.fromtimestamp(registro[1]).strftime("%Y-%m-%d %H:%M")

            if registro[2] == 0:
                registro[2] = 'no a salido' 
            else: 
                registro[2] = datetime.fromtimestamp(registro[2]).strftime("%Y-%m-%d %H:%M")

            tabla[i] = tuple(registro)


        

        for i in range(longitud_tabla-1,-1,-1):

            # se insertan los datos en la tabla
            # se insertan de forma inversa para que el ultimo registro sea el primero en la tabla

            self.tree.insert(
                "",
                0, 
                text=   tabla[i][1],
                values=(tabla[i][2], 
                        tabla[i][3],
                        tabla[i][4],
                        tabla[i][5],
                        tabla[i][6]
                        )
            )