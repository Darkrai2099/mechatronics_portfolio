import mysql.connector  
import pandas as pd 
import time


try:
    conexion_db = mysql.connector.connect( 
        host = "localhost",                 
        user = "root",                    
        password = "12345",             
        database = "sistema_ventas"        
    )
    sql = "SELECT * FROM ventas_mall_2026;"
    df = pd.read_sql(sql, conexion_db)
  

except Exception as tipo_error:            
    print(f"SE DETECTÓ UN PROBLEMA: {tipo_error}")

ingreso_total=(df["precio"] * df["cantidad"]).sum()
#print(ingreso_total)
cantidad_total_ventas=df["cantidad"].sum()
#print(cantidad_ventas)
df["venta_total"]=df["precio"]*df["cantidad"]
venta_total_sede=df.groupby("sede")["venta_total"].sum()
venta_total_sede.index.name=None
#print(venta_total_sede)
ventas_vendedor=df.groupby("vendedor")["venta_total"].sum()
mejor_vendedor = ventas_vendedor.idxmax()
#print(mejor_vendedor)
ventas_producto=df.groupby("producto")["cantidad"].sum()
producto_mas_vendido=ventas_producto.idxmax()
ventas_producto_mas_vendido=ventas_producto.max()
print("="*10+"REPORTE GERENCIAL"+"="*10)
print("1. Ingreso total generado:")
print(f"S/.{ingreso_total:,.2f}\n")
print("2. Cantidad total de productos vendidos:")
print(f"{cantidad_total_ventas} pizzas\n")
print("3. Venta total por sede:")
print(f"{venta_total_sede.map(lambda x: f"S/. {x:,.2f}").to_string()}\n")
print("4. Mejor vendedor del periodo:")
print(f"{mejor_vendedor}\n")
print("5. Producto mas vendido:")
print(f"{producto_mas_vendido} ({ventas_producto_mas_vendido} unidades)")
