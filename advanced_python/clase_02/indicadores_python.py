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
    
#KPIS generales
total_registros=len(df)
total_ventas=df["cantidad"].sum()

df["facturacion_total"]=df["precio_venta"]*df["cantidad"]
facturacion_total=df["facturacion_total"].sum()

precio_promedio=df["precio_venta"].mean()
precio_maximo=df["precio_venta"].max()
precio_minimo=df["precio_venta"].min()
ticket_promedio=facturacion_total/total_registros

#Visualizacion de KPIS:
print(f""" KPIS PRINCIPALES - WIGO MOTORS SAC
Total de registros de ventas    :   {total_registros} 
Total de vehiculos vendidos     :   {total_ventas}
Facturacion total               :   {facturacion_total:,.2f}
Precio promedio de venta        :   {precio_promedio:,.2f}
Precio maximo de venta          :   {precio_maximo:,.2f}
Precio minimo de venta          :   {precio_minimo:,.2f}
Ticket promedio por operacion   :   {ticket_promedio:,.2f}
""")