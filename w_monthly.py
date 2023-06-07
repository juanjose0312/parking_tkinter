from tkinter    import *
from datetime   import datetime, timedelta

from window import Window
from database_manager     import DatabaseManager

class W_monthly(Window):
    def __init__(self, window, title, geometry):
        super().__init__(window, title, geometry)

        def tarifa(tipo_vehiculo):

            # consulta a la base de datos para obtener la tarifa
            # input debera de ser el tipo de vehiculo
            # output sera la tarifa en horas

            db =DatabaseManager()
            condicion = f"tiempo = '1'"
            resultado = db.select_data('tarifas', condicion)
            resultado = list(resultado[0])

            if tipo_vehiculo == 'carro' :
                tarifa = resultado[1]
            else:
                tarifa = resultado[2]

            return tarifa

        def send_db():

            # esta funcion se encarga de enviar los datos a la base de datos

            fecha_terminado = self.time_entry + timedelta(days=30)

            db = DatabaseManager()
            car_data = {
                'fecha_ingreso':self.time_entry.timestamp(),
                'fecha_salida': fecha_terminado.timestamp(),
                'tipo_vehiculo':self.type.get(),
                'placa':        self.plate.get(),
                'mensualidad':  1,
                'valor':        0,
            }

            # se trabaja con dos base de datos para los carros activos y para el historial

            db.insert_data('historial',car_data)
            db.close_connection()
            window.destroy()

        # crea un frame para el formulario

        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40)

        # texto y barra desplegable para el tipo de vehiculo

        Label(frame, text= 'tipo de vehiculo : ').grid(row=0, column=0)
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

        Label(frame, text= "fecha de entrada").grid(row=2,column=0)
        self.time_entry = datetime.now()
        Label(frame, text= self.time_entry.strftime("%d/%m/%Y")).grid(row=2,column=1)

        # texto de hora de salida con la fecha actual tomada del sistema mas 30 dias

        Label(frame, text= "fecha de salida ").grid(row=3,column=0)
        fecha_terminado = self.time_entry.date() + timedelta(days=30)
        Label(frame, text= fecha_terminado.strftime("%d/%m/%Y")).grid(row=3,column=1)

        # texto de valor a pagar con la tarifa de un mes

        Label(frame, text= "valor a pagar").grid(row=4,column=0)
        Label(frame, text= f"$ {tarifa(self.type.get())}").grid(row=4,column=1)

        # boton de confirmacion

        Button(frame,text='confirmar',command= send_db).grid(row=5, column=0)