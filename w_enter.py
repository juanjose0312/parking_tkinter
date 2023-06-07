from tkinter    import *
from datetime   import datetime

from window import Window
from database_manager     import DatabaseManager

class W_enter(Window):
    def __init__(self, window, title, geometry):
        super().__init__(window, title, geometry)

        # crea un frame para el formulario

        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40)

        # texto y barra desplegable para el tipo de vehiculo

        Label(frame, text= 'tipo de vehicle : ').grid(row=0, column=0)
        self.type=StringVar(frame)
        self.type.set('carro')
        options=['carro','moto']
        OptionMenu(frame,self.type,*options).grid(row=0, column=1)

        # texto y espacion para agregar la placa del vehiculo

        Label(frame, text= 'placa : ').grid(row=1, column=0)
        self.plate = Entry(frame)
        self.plate.focus()
        self.plate.grid(row=1, column=1)

        # texto de hora de entrada con la fecha actual tomada del sistema

        Label(frame, text= "tiempo de entrada").grid(row=2,column=0)
        self.time_entry = datetime.now()
        Label(frame, text= self.time_entry.strftime("%I:%M %p")).grid(row=2,column=1)

        def send_db():

            # inserta los datos en la base de datos no se debe de ingresar ningun parametro el lo consulta automaticamente del formulario

            db = DatabaseManager()
            car_data = {
                'fecha_ingreso':self.time_entry.timestamp(),
                'fecha_salida': 0,
                'tipo_vehiculo':self.type.get(),
                'placa':        self.plate.get(),
                'mensualidad':  0,
                'valor':        0,
            }

            # se trabaja con dos base de datos para los carros activos y para el historial

            db.insert_data('historial',car_data)
            db.insert_data('carros_activos',car_data)
            db.close_connection()
            window.destroy()

        # boton de confirmacion y subir a la base de datos

        Button(frame,text='confirmar',command= send_db).grid(row=3, column=0)