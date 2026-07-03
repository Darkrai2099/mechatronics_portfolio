import mysql.connector  # Librería para trabajar con MySQL 

def fun_conexion():
    try:
        conexion_db = mysql.connector.connect( # Método para configurar parámatros de conexión
            host = "localhost",                # Información del servidor DB 
            user = "root",                     # Nombre del administrador DB
            password = "12345",                # Password del administrador 
            database = "techstore_peru"        # Nombre de la DB
        )
        return conexion_db
        
    except Exception as tipo_error:            # Captura el error y lo asigna a una variable
        print(f"SE DETECTÓ UN PROBLEMA: {tipo_error}")