import pandas as pd
import mysql.connector

try:
    conexion_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="wigo_motors"
    )

    consulta_sql = "SELECT * FROM ventas_vehiculos" # Consulta de toda la tabla de la DB
    df = pd.read_sql(consulta_sql, conexion_db)     # Creando el DataFrame basado en la tabla


except Exception as error:
    print(f"SE ENCONTRÓ UN PROBLEMA: {error}")

df["facturacion_total"]=df["precio_venta"]*df["cantidad"]   

#Cantidad total de vehiculos vendidos por marca
ventas_marca=df.groupby("marca")["cantidad"].sum().sort_values(ascending=False)
print(ventas_marca)

#Facturacion total de vehiculos vendidos por marca
facturacion_marca=df.groupby("marca")["facturacion_total"].sum().sort_values(ascending=False)
facturacion_marca=facturacion_marca.map("S/.{:,.2f}".format)
print(facturacion_marca)

#Participacion porcentual por marca:
participacion_marca=df.groupby("marca")["cantidad"].sum().sort_values(ascending=False)
participacion_marca=(participacion_marca/participacion_marca.sum())*100
participacion_marca=participacion_marca.map("{:,.2f}%".format)
print(participacion_marca)

#Top 10 modelos mas vendidos
ventas_modelos=df.groupby("modelo")["cantidad"].sum().sort_values(ascending=False).head(10)
print(ventas_modelos)

# Facturacion total por tienda:
facturacion_tienda = df.groupby("tienda")["facturacion_total"].sum().sort_values(ascending=False)
facturacion_tienda = facturacion_tienda.map("S/{:,.2f}".format) # Aplicando un formato 
print(facturacion_tienda)



