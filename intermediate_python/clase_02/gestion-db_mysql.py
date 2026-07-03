import mysql.connector  # Librería para trabajar con MySQL 

try:
    conexion_db = mysql.connector.connect( # Método para configurar parámatros de conexión
        host = "localhost",                # Información del servidor DB 
        user = "root",                     # Nombre del administrador DB
        password = "12345",                # Password del administrador 
        database = "techstore_peru"        # Nombre de la DB
    )
except Exception as tipo_error:
    print(f"SE DETECTO UN PROBLEMA: {tipo_error}")
print("SEGUIMOS CON EL PROGRAMA")

cursor_db=conexion_db.cursor()
consulta_sql="SELECT marca,modelo,precio_soles  FROM inventario_laptops"
cursor_db.execute(consulta_sql)
respuesta_sql=cursor_db.fetchall()

contador=1
for fila in respuesta_sql:
    print(f" {contador}.{fila[1]} {fila[2]} | S/.{fila[3]:,.2f} | Stock: {fila[4]} | Sede: {fila[5]} | {fila[6]}")
    contador+=1