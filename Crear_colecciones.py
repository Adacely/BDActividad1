from pymongo import MongoClient

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Crear la base de datos "proyecto_torneo"
db = client['PROYECTO_TORNEO_TEST']

db.equipos.drop()
db.entrenadores.drop()
db.jugadores_america.drop()
db.jugadores_tolima.drop()
db.jugadores_junior.drop()
db.jugadores_once_caldas.drop()
db.partidos.drop()
db.arbitros.drop()



db.tabla_posiciones.drop()

tabla_posiciones = [
    {"equipo": "América de Cali", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "puntos": 0},
    {"equipo": "Junior de Barranquilla", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "puntos": 0},
    {"equipo": "Deportes Tolima", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "puntos": 0},
    {"equipo": "Once Caldas", "pj": 0, "pg": 0, "pe": 0, "pp": 0, "puntos": 0}
]

# Insertar la tabla de posiciones en la colección
db.tabla_posiciones.insert_many(tabla_posiciones)
print("tabla de posiciones insertada exitosamente en MongoDB")


# equipos del grupo B
db.equipos.drop()

equipos = [
    {"nombre": "América de Cali", "grupo": "B", "jugadores": []},
    {"nombre": "Junior de Barranquilla", "grupo": "B", "jugadores": []},
    {"nombre": "Deportes Tolima", "grupo": "B", "jugadores": []},
    {"nombre": "Once Caldas", "grupo": "B", "jugadores": []}
]

# Insertar los equipos en la colección
db.equipos.insert_many(equipos)
print("equipos insertados exitosamente en MongoDB")



# Insertar datos en la colección "entrenadores"
# Limpiar la colección de entrenadores y agregar solo los del grupo B
db.entrenadores.drop()

entrenadores = [
    {
        "nombre": "lucas gonzales",
        "equipo": "América de Cali"
    },
    {
        "nombre": "Arturo Reyes",
        "equipo": "Junior de Barranquilla"
    },
    {
        "nombre": "Hernán Torres",
        "equipo": "Deportes Tolima"
    },
    {
        "nombre": "Pedro Sarmiento",
        "equipo": "Once Caldas"
    }
]

# Insertar los entrenadores en la colección
db.entrenadores.insert_many(entrenadores)
print("entrenadores insertados exitosamente en MongoDB")

db.jugadores_america.drop()

# Insertar datos en la colección "jugadores" del equipo América de Cali
jugadores_america = [
    {"nombre": "Joel Graterol", "posición": "Portero", "f_nacimiento": "15/05/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "800 mil €"},
    {"nombre": "Jorge Soto", "posición": "Portero", "f_nacimiento": "02/08/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "David Quintero", "posición": "Portero", "f_nacimiento": "29/01/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Juan Munera", "posición": "Portero", "f_nacimiento": "17/07/2001", "edad": 23, "nacionalidad": "España", "valor_mercado": "-"},
    {"nombre": "Andrés Mosquera", "posición": "Defensa central", "f_nacimiento": "20/02/1990", "edad": 34, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Jeisson Palacios", "posición": "Defensa central", "f_nacimiento": "20/03/1994", "edad": 30, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Brayan Medina", "posición": "Defensa central", "f_nacimiento": "04/03/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Daniel Bocanegra", "posición": "Defensa central", "f_nacimiento": "23/04/1987", "edad": 37, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "David Mina", "posición": "Lateral izquierdo", "f_nacimiento": "12/04/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Edwin Velasco", "posición": "Lateral izquierdo", "f_nacimiento": "05/11/1991", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Yerson Candelo", "posición": "Lateral derecho", "f_nacimiento": "24/02/1992", "edad": 32, "nacionalidad": "Colombia", "valor_mercado": "600 mil €"},
    {"nombre": "Nilson Castrillón", "posición": "Lateral derecho", "f_nacimiento": "28/01/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Josen Escobar", "posición": "Pivote", "f_nacimiento": "12/12/2004", "edad": 19, "nacionalidad": "Colombia", "valor_mercado": "2,00 mill. €"},
    {"nombre": "Éder Balanta", "posición": "Pivote", "f_nacimiento": "28/02/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "900 mil €"},
    {"nombre": "Franco Leys", "posición": "Pivote", "f_nacimiento": "18/10/1993", "edad": 31, "nacionalidad": "Argentina", "valor_mercado": "400 mil €"},
    {"nombre": "Luis Alejandro Paz", "posición": "Pivote", "f_nacimiento": "08/09/1988", "edad": 36, "nacionalidad": "Colombia", "valor_mercado": "100 mil €"},
    {"nombre": "Jader Quiñónes", "posición": "Mediocentro", "f_nacimiento": "12/12/2000", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "700 mil €"},
    {"nombre": "Harold Rivera", "posición": "Mediocentro", "f_nacimiento": "19/03/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Alexis Zapata", "posición": "Mediocentro ofensivo", "f_nacimiento": "10/05/1995", "edad": 29, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Duván Vergara", "posición": "Extremo izquierdo", "f_nacimiento": "09/09/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "2,00 mill. €"},
    {"nombre": "Mateo Zuleta", "posición": "Extremo izquierdo", "f_nacimiento": "07/06/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Éver Valencia", "posición": "Extremo izquierdo", "f_nacimiento": "23/01/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Pipe Gómez", "posición": "Extremo izquierdo", "f_nacimiento": "11/10/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Cristian Barrios", "posición": "Extremo derecho", "f_nacimiento": "19/05/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "1,60 mill. €"},
    {"nombre": "Rodrigo Holgado", "posición": "Delantero centro", "f_nacimiento": "28/06/1995", "edad": 29, "nacionalidad": "Argentina", "valor_mercado": "800 mil €"},
    {"nombre": "Yojan Garcés", "posición": "Delantero centro", "f_nacimiento": "27/05/2006", "edad": 18, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Adrián Ramos", "posición": "Delantero centro", "f_nacimiento": "22/01/1986", "edad": 38, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"}
    ]

#Insertar jugadores de america en la colección

db.jugadores_america.insert_many(jugadores_america)
print("jugadores_america insertados exitosamente en MongoDB")

db.jugadores_tolima.drop()

jugadores_tolima = [
    {"nombre": "Neto Volpi", "posición": "Portero", "f_nacimiento": "01/08/1992", "edad": 32, "nacionalidad": "Brasil", "valor_mercado": "400 mil €"},
    {"nombre": "Juan Camilo Chaverra", "posición": "Portero", "f_nacimiento": "12/12/1992", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "William Cuesta", "posición": "Portero", "f_nacimiento": "19/02/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "150 mil €"},
    {"nombre": "Marlon Torres", "posición": "Defensa central", "f_nacimiento": "17/04/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "650 mil €"},
    {"nombre": "Anderson Angulo", "posición": "Defensa central", "f_nacimiento": "01/07/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Alfonso Simarra", "posición": "Defensa central", "f_nacimiento": "13/07/2000", "edad": 24, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Juan Mera", "posición": "Defensa central", "f_nacimiento": "12/03/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Julián Quiñones", "posición": "Defensa central", "f_nacimiento": "05/11/1989", "edad": 35, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Jhon Quiñones", "posición": "Defensa central", "f_nacimiento": "16/04/2004", "edad": 20, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Junior Hernández", "posición": "Lateral izquierdo", "f_nacimiento": "05/04/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "1,20 mill. €"},
    {"nombre": "Jeison Angulo", "posición": "Lateral izquierdo", "f_nacimiento": "27/06/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Yhormar Hurtado", "posición": "Lateral derecho", "f_nacimiento": "14/12/1996", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Yilson Rosales", "posición": "Lateral derecho", "f_nacimiento": "09/12/2000", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Cristian Trujillo", "posición": "Pivote", "f_nacimiento": "09/08/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "650 mil €"},
    {"nombre": "Brayan Rovira", "posición": "Pivote", "f_nacimiento": "02/12/1996", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Fabian Mosquera", "posición": "Pivote", "f_nacimiento": "03/03/1995", "edad": 29, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Juan Pablo Nieto", "posición": "Mediocentro", "f_nacimiento": "25/02/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Carlos Esparragoza", "posición": "Mediocentro", "f_nacimiento": "06/03/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Yeison Guzmán", "posición": "Mediocentro ofensivo", "f_nacimiento": "22/03/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "2,80 mill. €"},
    {"nombre": "Eduardo Sosa", "posición": "Mediocentro ofensivo", "f_nacimiento": "20/06/1996", "edad": 28, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Andrés Arroyo", "posición": "Mediocentro ofensivo", "f_nacimiento": "20/01/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "William Dávila", "posición": "Mediocentro ofensivo", "f_nacimiento": "01/06/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Alex Castro", "posición": "Extremo izquierdo", "f_nacimiento": "08/03/1994", "edad": 30, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Facundo Boné", "posición": "Extremo izquierdo", "f_nacimiento": "16/11/1995", "edad": 29, "nacionalidad": "Italia", "valor_mercado": "450 mil €"},
    {"nombre": "Kevin Pérez", "posición": "Extremo derecho", "f_nacimiento": "18/07/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "650 mil €"},
    {"nombre": "Jeison Lucumí", "posición": "Extremo derecho", "f_nacimiento": "08/04/1995", "edad": 29, "nacionalidad": "Colombia", "valor_mercado": "600 mil €"},
    {"nombre": "Luis Miranda", "posición": "Extremo derecho", "f_nacimiento": "27/08/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Brayan Gil", "posición": "Delantero centro", "f_nacimiento": "28/06/2001", "edad": 23, "nacionalidad": "El Salvador", "valor_mercado": "700 mil €"},
    {"nombre": "Franco López", "posición": "Delantero centro", "f_nacimiento": "20/10/1992", "edad": 32, "nacionalidad": "Uruguay", "valor_mercado": "400 mil €"},
    {"nombre": "Carlos Cortés", "posición": "Delantero centro", "f_nacimiento": "17/09/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Gustavo Ramírez", "posición": "Delantero centro", "f_nacimiento": "13/05/1990", "edad": 34, "nacionalidad": "Paraguay", "valor_mercado": "200 mil €"},
    {"nombre": "Jeinner Fuentes", "posición": "Delantero centro", "f_nacimiento": "07/05/2005", "edad": 19, "nacionalidad": "Colombia", "valor_mercado": "100 mil €"},
    {"nombre": "Juan Carabalí", "posición": "Delantero centro", "f_nacimiento": "26/02/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"}
    ]

# Insertar jugadores en la colección
db.jugadores_tolima.insert_many(jugadores_tolima)
print("jugadores_tolima insertados exitosamente en MongoDB")


db.jugadores_junior.drop()


jugadores_junior = [
    {"nombre": "Santiago Mele", "posición": "Portero", "f_nacimiento": "06/09/1997", "edad": 27, "nacionalidad": "Uruguay", "valor_mercado": "2,50 mill. €"},
    {"nombre": "Jefersson Martínez", "posición": "Portero", "f_nacimiento": "16/08/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "Sebastián Araujo", "posición": "Portero", "f_nacimiento": "19/06/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Jaime Acosta", "posición": "Portero", "f_nacimiento": "26/11/2001", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Jermein Peña", "posición": "Defensa central", "f_nacimiento": "16/10/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "850 mil €"},
    {"nombre": "Emanuel Olivera", "posición": "Defensa central", "f_nacimiento": "02/04/1990", "edad": 34, "nacionalidad": "Argentina", "valor_mercado": "500 mil €"},
    {"nombre": "Rafael Pérez", "posición": "Defensa central", "f_nacimiento": "09/01/1990", "edad": 34, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Howell Mena", "posición": "Defensa central", "f_nacimiento": "19/04/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Nicolás Zalazar", "posición": "Defensa central", "f_nacimiento": "29/01/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Yairo Moreno", "posición": "Lateral izquierdo", "f_nacimiento": "04/04/1995", "edad": 29, "nacionalidad": "Colombia", "valor_mercado": "1,20 mill. €"},
    {"nombre": "Edwin Herrera", "posición": "Lateral izquierdo", "f_nacimiento": "02/09/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "750 mil €"},
    {"nombre": "Jhon Navia", "posición": "Lateral izquierdo", "f_nacimiento": "27/07/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Jhon Lerma", "posición": "Lateral derecho", "f_nacimiento": "01/01/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Yeferson Moreno", "posición": "Lateral derecho", "f_nacimiento": "16/01/2004", "edad": 20, "nacionalidad": "Colombia", "valor_mercado": "50 mil €"},
    {"nombre": "Víctor Cantillo", "posición": "Pivote", "f_nacimiento": "15/10/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "900 mil €"},
    {"nombre": "Andrés Colorado", "posición": "Pivote", "f_nacimiento": "01/12/1998", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "800 mil €"},
    {"nombre": "Didier Moreno", "posición": "Pivote", "f_nacimiento": "15/09/1991", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Jhon Vélez", "posición": "Pivote", "f_nacimiento": "25/07/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Yani Quintero", "posición": "Pivote", "f_nacimiento": "17/07/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Léider Berrío", "posición": "Mediocentro", "f_nacimiento": "07/06/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Léider Berdugo", "posición": "Mediocentro", "f_nacimiento": "19/02/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Carlos Cantillo", "posición": "Mediocentro", "f_nacimiento": "21/02/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Roberto Hinojoza", "posición": "Mediocentro ofensivo", "f_nacimiento": "02/07/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "800 mil €"},
    {"nombre": "José Enamorado", "posición": "Extremo izquierdo", "f_nacimiento": "13/01/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "2,40 mill. €"},
    {"nombre": "Luis González", "posición": "Extremo izquierdo", "f_nacimiento": "22/12/1990", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Bryan Castrillón", "posición": "Extremo izquierdo", "f_nacimiento": "30/03/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Joel Canchimbo", "posición": "Extremo izquierdo", "f_nacimiento": "12/08/2005", "edad": 19, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Yimmi Chará", "posición": "Extremo derecho", "f_nacimiento": "02/04/1991", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "500 mil €"},
    {"nombre": "Steven Rodríguez", "posición": "Delantero centro", "f_nacimiento": "13/10/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "450 mil €"},
    {"nombre": "Carlos Bacca", "posición": "Delantero centro", "f_nacimiento": "08/09/1986", "edad": 38, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Marco Pérez", "posición": "Delantero centro", "f_nacimiento": "18/09/1990", "edad": 34, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"}
    ]

# Insertar jugadores en la colección
db.jugadores_junior.insert_many(jugadores_junior)
print("jugadores_junior insertados exitosamente en MongoDB")



db.jugadores_once_caldas.drop()

# Insertar datos en la colección "jugadores" del equipo Once Caldas
jugadores_once_caldas = [
    {"nombre": "James Aguirre", "posición": "Portero", "f_nacimiento": "21/05/1992", "edad": 32, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Ezequiel Mastrolía", "posición": "Portero", "f_nacimiento": "25/03/1991", "edad": 33, "nacionalidad": "Argentina", "valor_mercado": "200 mil €"},
    {"nombre": "Juan Gallego", "posición": "Portero", "f_nacimiento": "26/10/2004", "edad": 20, "nacionalidad": "Colombia", "valor_mercado": "-"},
    {"nombre": "Stalin Valencia", "posición": "Defensa central", "f_nacimiento": "10/10/2003", "edad": 21, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "Jorge Cardona", "posición": "Defensa central", "f_nacimiento": "23/02/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "Yonatan Murillo", "posición": "Defensa central", "f_nacimiento": "05/07/1992", "edad": 32, "nacionalidad": "Colombia", "valor_mercado": "250 mil €"},
    {"nombre": "Jáider Riquett", "posición": "Defensa central", "f_nacimiento": "10/05/1990", "edad": 34, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Léyder Morán", "posición": "Defensa central", "f_nacimiento": "25/12/2004", "edad": 19, "nacionalidad": "Colombia", "valor_mercado": "150 mil €"},
    {"nombre": "Juan Patiño", "posición": "Lateral izquierdo", "f_nacimiento": "10/09/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Juan David Cuesta", "posición": "Lateral derecho", "f_nacimiento": "21/11/1997", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "550 mil €"},
    {"nombre": "Daniel Quiñones", "posición": "Lateral derecho", "f_nacimiento": "07/04/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "100 mil €"},
    {"nombre": "Iván Rojas", "posición": "Pivote", "f_nacimiento": "24/07/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "650 mil €"},
    {"nombre": "Dánnovi Quiñones", "posición": "Pivote", "f_nacimiento": "05/01/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Álvaro Montaño", "posición": "Pivote", "f_nacimiento": "14/09/2000", "edad": 24, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Juan Camilo García", "posición": "Pivote", "f_nacimiento": "24/02/1997", "edad": 27, "nacionalidad": "Colombia", "valor_mercado": "100 mil €"},
    {"nombre": "Alejandro Garcia", "posición": "Mediocentro", "f_nacimiento": "28/02/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "900 mil €"},
    {"nombre": "Mateo García", "posición": "Mediocentro", "f_nacimiento": "28/08/1998", "edad": 26, "nacionalidad": "Colombia", "valor_mercado": "700 mil €"},
    {"nombre": "Lucas Ríos", "posición": "Mediocentro ofensivo", "f_nacimiento": "08/03/1998", "edad": 26, "nacionalidad": "Argentina", "valor_mercado": "700 mil €"},
    {"nombre": "Johan Beltrán", "posición": "Mediocentro ofensivo", "f_nacimiento": "18/10/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Róger Torres", "posición": "Mediocentro ofensivo", "f_nacimiento": "13/07/1991", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Manuel Arteaga", "posición": "Mediocentro ofensivo", "f_nacimiento": "26/02/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Luis Palacios", "posición": "Extremo izquierdo", "f_nacimiento": "10/04/2001", "edad": 23, "nacionalidad": "Colombia", "valor_mercado": "400 mil €"},
    {"nombre": "Joel Contreras", "posición": "Extremo izquierdo", "f_nacimiento": "01/05/1999", "edad": 25, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "Jefry Zapata", "posición": "Extremo izquierdo", "f_nacimiento": "03/02/2000", "edad": 24, "nacionalidad": "Colombia", "valor_mercado": "350 mil €"},
    {"nombre": "Michael Barrios", "posición": "Extremo derecho", "f_nacimiento": "21/04/1991", "edad": 33, "nacionalidad": "Colombia", "valor_mercado": "600 mil €"},
    {"nombre": "John Deiby Araujo", "posición": "Extremo derecho", "f_nacimiento": "18/07/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "300 mil €"},
    {"nombre": "Jesús Hernández", "posición": "Delantero centro", "f_nacimiento": "06/01/1993", "edad": 31, "nacionalidad": "Colombia", "valor_mercado": "275 mil €"},
    {"nombre": "Dayro Moreno", "posición": "Delantero centro", "f_nacimiento": "16/09/1985", "edad": 39, "nacionalidad": "Colombia", "valor_mercado": "200 mil €"},
    {"nombre": "Felipe Cifuentes", "posición": "Delantero centro", "f_nacimiento": "14/04/2002", "edad": 22, "nacionalidad": "Colombia", "valor_mercado": "100 mil €"}
    ]


# Insertar jugadores en la colección
db.jugadores_once_caldas.insert_many(jugadores_once_caldas)
print("jugadores_once_caldas insertados exitosamente en MongoDB")

db.partidos.drop()

partidos = [
    {
        "equipo_local": "América de Cali",
        "equipo_visitante": "Once Caldas",
        "fecha": "2024-11-20",
        "hora": "20:00",
        "estadio": "Pascual Guerrero (Cali)",
        "arbitro": "Jhon Ospina"
    },
    {
        "equipo_local": "Junior de Barranquilla",
        "equipo_visitante": "Deportes Tolima",
        "fecha": "2024-11-21",
        "hora": "18:00",
        "estadio": "Metropolitano Roberto Meléndez (Barranquilla)",
        "arbitro": "Carlos Ortega"
    }
]

# Insertar los partidos en la colección
db.partidos.insert_many(partidos)
print("partidos insertados exitosamente en MongoDB")

db.arbitros.drop()

arbitros = [
    {
        "nombre": "Jhon Ospina",
        "ciudad": "Quindío",
        "partidos_asignados": ["América de Cali vs. Once Caldas"]
    },
    {
        "nombre": "Carlos Ortega",
        "ciudad": "Bolívar",
        "partidos_asignados": ["Junior de Barranquilla vs. Deportes Tolima"]
    }
]

# Insertar los árbitros en la colección
db.arbitros.insert_many(arbitros)
print("arbitros insertados exitosamente en MongoDB")



