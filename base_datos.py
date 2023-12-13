import sqlite3

with sqlite3.connect('base_puntajes.db') as conexion:
    try:
        sentencia = '''create table puntos
        (
        id integer primary key autoincrement, nombre text, puntaje int    
        )
        '''
        conexion.execute(sentencia)
        print('Se creo la tabla de puntos')

    except sqlite3.OperationalError:
        print('La tabla de puntos existe!!')



    #INSERT
def guardar_datos(nombre:str, score:int):
    with sqlite3.connect('base_puntajes.db') as conexion:
        try:
            conexion.execute('INSERT into puntos(nombre,puntaje) values (?,?)', (nombre, score))
            conexion.commit()
            print("guardo datos en base")
        except:
            print('error')

#SELECT
def obtener_datos():
    with sqlite3.connect('base_puntajes.db') as conexion:
        cursor = conexion.execute("SELECT * FROM puntos order by puntaje desc LIMIT 3")
        datos = []
        for fila in cursor:
            datos.append({'nombre':fila[1], 'puntos': fila[2]})

        return datos
