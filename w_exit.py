from tkinter    import *
from datetime   import datetime

from window     import Window
from database_manager         import DatabaseManager

class W_exit(Window):
    def __init__(self, window, title, geometry):
        super().__init__(window, title, geometry)

        def busqueda_placa(placa):

            # esta funcion se encarga de buscar el registro de la paca que seleccionen
            # si el input es 0 se llamar toda la tabla de carros activos
            # si el input es uan placa devolvera el registro de esa placa

            db =DatabaseManager()

            if placa == 0:
                resultado = db.select_data('carros_activos')    

            else:
                condicion = f"placa = '{placa}'"
                resultado = db.select_data('carros_activos', condicion)
                resultado = list(resultado[0])

            return resultado
        
        def horas_parqueadero(registro):

            # esta funcion se encarga de calcular las horas que estuvo el carro en el parqueadero
            # input debera de ser un registro de la tabla carros activos

            hora_entrada    = datetime.fromtimestamp(registro[1])
            hora_salida     = self.time_exit
            horas_en_parqueadero = hora_salida - hora_entrada
            return horas_en_parqueadero

        def precio_parqueadero(tiempo_parquedero, registro):

            # esta funcion se encarga de calcular el precio que debe de pagar el usuario
            # input debera de ser un registro de la tabla carros activos
            # y el tiempo que estuvo en el parqueadero

            # sale que tipo de vehiculo es
            tipo_vehiculo = registro[3]

            # consulta en cuanto esta la tarifa en horas para ese tipo de vehiculo
            db =DatabaseManager()
            condicion = f"tiempo = '0'"
            resultado = db.select_data('tarifas', condicion)
            resultado = list(resultado[0])

            # se asigna la tarifa segun el tipo de vehiculo
            if tipo_vehiculo == 'carro' :
                tarifa = resultado[1]
            else:
                tarifa = resultado[2]
                
            # se calcula el tiempo que estuvo en el parqueadero en horas
            tiempo_en_horas = tiempo_parquedero.days * 24 + tiempo_parquedero.seconds // 3600

            # se calcula el valor que debe de pagar el usuario si el usario no completo la hora se le cobra la mitad
            if tiempo_en_horas == 0:
                valor_parqueadero = tarifa/2
            else:
                valor_parqueadero=tarifa*tiempo_en_horas

            return valor_parqueadero, tiempo_en_horas
        

        def pago(hora_salida,valor,placa):
            db =DatabaseManager()
            
            # modificar la hora de salida y el valor pagado en el historial

            update_data = {
                'fecha_salida'  : hora_salida.timestamp(),
                'valor'         : valor
                }
    
            condicion = f"placa = '{placa}'"
            db.update_data('historial', update_data, condicion,)

            # eliminar el registro del carro de carros activos

            condicion = f"placa = '{placa}'"
            db.delete_data('carros_activos', condicion)

            db.close_connection()

        def mostrar_ventana_emergente(valor, tiempo, placa):

            # esta funcion se encarga de mostrar una ventana emergente con el valor a pagar
            # input valor a pagar y el tiempo que estuvo en el parqueadero

            ventana_emergente = Toplevel(self.wind)
            ventana_emergente.title("precion a pagar")
            ventana_emergente.geometry('720x100')

            # crea un frame para trabajar con la herramienta grid

            frame = LabelFrame(ventana_emergente)
            frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40)

            # muestra el valor a pagar y los botones de pagar y volver

            if tiempo == 0:
                Label(frame, text=f"El valor a pagar es $ {valor} por no haber completado la hora se cobra la mitad de la tarifa").grid(row=0, column=0)
            else:
                Label(frame, text=f"El valor a pagar es $ {valor} por su estancia de {tiempo}").grid(row=0, column=0)
 
            Button(frame, text="Pagar", command= lambda:(pago(self.time_exit, valor, placa ),ventana_emergente.destroy())).grid(row=1, column=0)
            Button(frame, text="Volver", command= ventana_emergente.destroy).grid(row=1, column=1)


        def aviso_pago():

            # esta funcion se encarga de mostrar una ventana emergente con el valor a pagar

            registro = busqueda_placa(self.placa.get())
            horas_parqueadas = horas_parqueadero(registro)
            valor_parqueadero, tiempo_en_horas = precio_parqueadero(horas_parqueadas, registro)
            mostrar_ventana_emergente(valor_parqueadero, tiempo_en_horas, registro[4])


        # crea un frame para trabajar con la herramienta grid

        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, columnspan=5, pady=20, padx=40)

        # seleccionar la placa del vehiculo
        # se crea una lista con las placas de los vehiculos que estan en el parqueadero

        registros = busqueda_placa(0)
        placas_disponibles=[]

        for placas in registros:
            placas_disponibles.append(placas[4])

        # se crea un menu con las placas disponibles

        Label(frame, text= 'placa : ').grid(row=0, column=0)
        self.placa=StringVar(frame)
        self.placa.set(placas_disponibles[0])
        options = placas_disponibles
        OptionMenu(frame,self.placa,*options).grid(row=0, column=1)

        # se muestra la hora de entrada y la hora de salida

        Label(frame, text= "tiempo de entrada").grid(row=1,column=0)
        self.time_exit = datetime.now()
        Label(frame, text= self.time_exit.strftime("%I:%M %p")).grid(row=1,column=1)

        # se muestra el boton de confirmar

        Button(frame,text='confirmar',command= aviso_pago ).grid(row=3, column=0)