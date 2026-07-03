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

marca_buscada=input("Ingrese marca: ")

cursor_db=conexion_db.cursor()
consulta_sql="SELECT marca,modelo,precio_soles  FROM inventario_laptops WHERE marca=%(marca)s ORDER BY precio_soles DESC"
params = {"marca":marca_buscada}
cursor_db.execute(consulta_sql,params)
respuesta_sql=cursor_db.fetchall()

contador=1
for fila in respuesta_sql:
    print(f" {contador}.{fila[0]} {fila[1]} | S/.{fila[2]:,.2f}")
    contador+=1