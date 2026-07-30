import pandas as pd

ruta_archivo=r"C:\Users\ACER\Desktop\advanced_python\clase_01\dataset_ventas.xlsx"

try:
    df=pd.read_excel(ruta_archivo)
except Exception as error:
    print(f"Se encontro un error: {error}")

#print(df.head(10))
#print(df.shape)
#print(df.info())
df["precio"]=df["precio"].astype(float)

df=df[["fecha","ciudad","sucursal","marca","modelo","precio","cantidad","gama","total","metodo_pago"]]
#df=df.rename(columns={"ciudad":"departamento"})

#filtros/consultas
df_filtrado=df[
    (df["marca"]=="Apple")&
    (df["precio"]>=4000)&
    (df["ciudad"]=="Lima")&
    (df["metodo_pago"]=="Yape")
    ]
df_filtrado_2=df[
    (df["ciudad"]=="Arequipa")&
    (df["sucursal"]=="Mall Aventura")&
    (df["marca"]=="Apple")&
    ((df["metodo_pago"]=="Yape")|(df["metodo_pago"]=="Tarjeta"))
    ]

df_filtrado_3=df[
    (df["ciudad"]=="Lima")&
    ((df["marca"]=="Apple")|(df["marca"]=="Samsung")|(df["marca"]=="Xiaomi"))&
    (df["gama"]=="Premium")&
    (df["precio"]>=4000)&
    ((df["metodo_pago"]=="Yape")|(df["metodo_pago"]=="Tarjeta"))
    ]
df_filtrado_3=df_filtrado_3.sort_values(by="total", ascending=False)
df_filtrado_3 = df_filtrado_3[["fecha","ciudad","marca","modelo","precio","cantidad","gama","total","metodo_pago"]]


ruta_reporte=r"C:\Users\ACER\Desktop\advanced_python\clase_01\archivos exportados\reporte_apple.xlsx"
ruta_reporte_2=r"C:\Users\ACER\Desktop\advanced_python\clase_01\archivos exportados\reporte_arequipa_mall_aventura.xlsx"
ruta_reporte_3=r"C:\Users\ACER\Desktop\advanced_python\clase_01\archivos exportados\Reporte_Gerencia_Lima.xlsx"
df_filtrado.to_excel(ruta_reporte, index=False)
df_filtrado_2.to_excel(ruta_reporte_2, index=False)
df_filtrado_3.to_excel(ruta_reporte_3, index=False)
print("Se exportaron los archivos")

