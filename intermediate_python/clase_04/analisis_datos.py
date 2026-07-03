import mysql.connector  
import pandas as pd 
import time


try:
    conexion_db = mysql.connector.connect( 
        host = "localhost",                 
        user = "root",                    
        password = "12345",             
        database = "techstore_peru"        
    )
    sql = "SELECT * FROM inventario_laptops;"
    df = pd.read_sql(sql, conexion_db)
  

except Exception as tipo_error:            
    print(f"SE DETECTÓ UN PROBLEMA: {tipo_error}")

#tabla_db=df.head(20) -> mostrar las primeras 20 filas

#print(tabla_db) 

#print(df.info()) -> verificar los tipos de datos

filtro_01=df[df["categoria"] == "Gaming"]
#print(filtro_01)    
filtro_02=df[df["precio_soles"] >= 5000]
#print(filtro_02)
filtro_03=df[(df["marca"]=="Acer") & (df["precio_soles"]>=2000)]
#print(filtro_03)

#Marca: HP, Tienda: San Isidro, Categoria:Profesional, Precio: >=2000
filtro_04=df[(df["marca"]=="HP") & (df["tienda"]=="San Isidro") & (df["categoria"]=="Profesional") & (df["precio_soles"]>=2000)]
#print(filtro_04)

ordenamiento_01 = df.sort_values(by="precio_soles", ascending=False)
#print(ordenamiento_01)

ordenamiento_02 = df.sort_values(by="marca", ascending=False)
#print(ordenamiento_02)

ordenamiento_03 = df.sort_values(by=["categoria", "precio_soles"], ascending=[True, False])
#print(ordenamiento_03)

tabla_01=df.groupby("tienda")["stock"].sum()
#print(tabla_01)

tabla_02=df.groupby("marca")["precio_soles"].mean()
#print(tabla_02)

tabla_03=df.groupby("marca")["precio_soles"].max()
#print(tabla_03.map("S/.{:.2f}".format))

tabla_04=df.groupby("marca")["precio_soles"].min()
#print(tabla_04.map("S/.{:.2f}".format))

stock_total=df["stock"].sum()
precio_promedio=df["precio_soles"].mean()
precio_alto=df["precio_soles"].max()
precio_bajo=df["precio_soles"].min()
valor_total=(df["precio_soles"] * df["stock"]).sum()

#print(f"Stock total: {stock_total}")
#print(f"Precio promedio: S/.{precio_promedio:,.2f} soles")
#print(f"Precio mas alto: S/.{precio_alto:,.2f} soles")
#print(f"Precio mas bajo: S/.{precio_bajo:,.2f} soles")
#print(f"Valor total del inventario: S/.{valor_total:,.2f} soles")

#df.to_csv("inventario_equipos.csv",index=False)
#print("Se exporto de forma correcta.")

import openpyxl
df.to_excel("reporte_laptops.xlsx",index=False)
print("Se exporto la tabla en un archivo de excel.")