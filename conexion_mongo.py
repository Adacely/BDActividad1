from pymongo import MongoClient

# Conectar a MongoDB en el servidor local (localhost)
client = MongoClient('mongodb://localhost:27017/')

# Crear la base de datos "Proyecto_Torneo"
db = client['PROYECTO_TORNEO_TEST']

# Imprimir para verificar la conexión
print("Conexión exitosa a la base de datos 'PROEYECTO_TORNEO_TEST'")
