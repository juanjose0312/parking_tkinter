from database_manager import DatabaseManager

# Crear una tabla

db = DatabaseManager()
db.create_table('carros_activos','id INTEGER PRIMARY KEY, fecha_ingreso INTEGER, fecha_salida INTEGER, tipo_vehiculo TEXT, placa TEXT, mensualidad INTEGER, valor INTEGER')
db.create_table('historial     ','id INTEGER PRIMARY KEY, fecha_ingreso INTEGER, fecha_salida INTEGER, tipo_vehiculo TEXT, placa TEXT, mensualidad INTEGER, valor INTEGER')
db.create_table('tarifas       ','tiempo INTEGER, carro INTEGER, moto INTEGER')

# Insertar datos

user_data = {'tiempo':   0,'carro':    2000,'moto':     1000}
db.insert_data('tarifas', user_data)

user_data = {'tiempo':   1,'carro':    80000,'moto':     40000}
db.insert_data('tarifas', user_data)