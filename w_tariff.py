from tkinter import *
from tkinter import messagebox
from window import Window
from database_manager import DatabaseManager

class W_tariff(Window):
    def __init__(self, window, title, geometry):
        super().__init__(window, title, geometry)

        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40)

        def cambiar_tarifas(hora_carro, hora_moto, mes_carro, mes_moto):

            # funcion para cambiar las tarifas
            # se debe validar que los valores ingresados sean numeros

            db = DatabaseManager()

            tarifas_actualizadas = [
                [0,'carro', hora_carro],
                [0,'moto', hora_moto],
                [1,'carro', mes_carro],
                [1,'moto', mes_moto]
            ]

            # se recorre la lista de tarifas actualizadas y se valida que el valor ingresado sea un numero

            for tiempo, tipo_vehiculo, input_valor in tarifas_actualizadas:
                
                if input_valor != None :
                    if input_valor.isdigit():

                        # se actualiza la base de datos

                        update_data = {
                            tipo_vehiculo : input_valor
                        }
                        condicion = f"tiempo = '{tiempo}'"
                        db.update_data('tarifas', update_data, condicion)
                        messagebox.showinfo('info', f"El valor de la tarifa de {tipo_vehiculo} se actualizó correctamente")

                else:
                    
                    # en caso de que el valor ingresado no sea un numero se muestra un mensaje de error pero si el valor es None no se muestra nada

                    if input_valor == None:
                        pass
                    elif tiempo == 0:
                        messagebox.showerror('error', f"El valor de la hora de {tipo_vehiculo} no puede es valido")
                    else:
                        messagebox.showerror('error', f"El valor mensual de la hora de {tipo_vehiculo} no es válido")

            db.close_connection()

        # llamado a base de dato para sacar el valor de las tarifas

        db =DatabaseManager()
        tarifas = db.select_data('tarifas')
        db.close_connection()

        # primera fila
        Label(frame, text= "tiempo").grid(row=0,column=0)
        Label(frame, text= "carro").grid(row=0,column=1)
        Label(frame, text= "moto").grid(row=0,column=2)

        # segunda fila
        Label(frame, text= "horas").grid(row=1,column=0)

        Label(frame, text= f"$ {tarifas[0][1]}").grid(row=1,column=1)
        self.valor_hora_carro = Entry(frame)
        self.valor_hora_carro.grid(row=2,column=1)

        Label(frame, text= f"$ {tarifas[0][2]}").grid(row=1,column=2)
        self.valor_hora_moto = Entry(frame)
        self.valor_hora_moto.grid(row=2,column=2)

        # tercera fila
        Label(frame, text= "mes").grid(row=3,column=0)

        Label(frame, text= f"$ {tarifas[1][1]}").grid(row=3,column=1)
        self.valor_mes_carro = Entry(frame)
        self.valor_mes_carro.grid(row=4,column=1)

        Label(frame, text= f"$ {tarifas[1][2]}").grid(row=3,column=2)
        self.valor_mes_moto = Entry(frame)
        self.valor_mes_moto.grid(row=4,column=2)

        # boton para cambiar las tarifas

        Button( frame,
                text='cambiar',
                command=lambda:cambiar_tarifas(
                    self.valor_hora_carro.get(),
                    self.valor_hora_moto.get(),
                    self.valor_mes_carro.get(),
                    self.valor_mes_moto.get()
                    )
                ).grid(row=5, column=2)
        