# import streamlit as st
# import pandas as pd
# import mysql.connector
# import plotly.express as px

# try:
#     conexion_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="12345",
#         database="wigo_motors"
#     )

#     consulta_sql = "SELECT * FROM ventas_vehiculos" # Consulta de toda la tabla de la DB
#     df = pd.read_sql(consulta_sql, conexion_db)     # Creando el DataFrame basado en la tabla

# except Exception as error:
#     print(f"SE ENCONTRÓ UN PROBLEMA: {error}")


# st.set_page_config(page_title="Wigo Motors", layout="wide")
# st.title("WIGO MOTORS S.A.C")   
# st.subheader("Buscador comercial")

# st.sidebar.header("Buscador")
# tipo_busqueda=st.sidebar.selectbox("Seleccione tipo de busqueda", ["marca","Asesor comercial","Sede"])

# df_filtrado=df.copy()

# if tipo_busqueda =="Marca":
#     valor=st.sidebar.selectbox("Seleccionar marca",df["marca"].unique())
#     df_filtrado=df[df["marca"]==valor]

# if tipo_busqueda =="Asesor comercial":
#     valor=st.sidebar.selectbox("Seleccionar asesor",df["asesor_comercial"].unique())
#     df_filtrado=df[df["asesor_comercial"]==valor]

# if tipo_busqueda =="Sede":
#     valor=st.sidebar.selectbox("Seleccionar sede",df["tienda"].unique())
#     df_filtrado=df[df["tienda"]==valor]

# st.success(f"Registros encontrados: {len(df_filtrado)}") 
# st.dataframe(df_filtrado)

# st.subheader("Indicadores:")

# c1, c2, c3, c4 = st.columns(4)          # CREANDO 4 COLUMNAS  


# c1.metric("Precio Total", f"S/{df_filtrado["precio_venta"].sum():,.2f}")          # Calcular el total de monto 
# c2.metric("Unidades vendidas", f"{df_filtrado["cantidad"].sum()}")                # Calcular el total de unidades vendidad
# c3.metric("Precio promedio", f"S/{df_filtrado["precio_venta"].mean():,.2f}")      # Calculcar el precio promedio
# c4.metric("Operaciones", len(df_filtrado))   

# c5,c6,c7,c8=st.columns(4)

# c5.metric("Precio mas alto", f"S/{df_filtrado["precio_venta"].max():,.2f}")
# c6.metric("Precio mas bajo", f"S/{df_filtrado["precio_venta"].min():,.2f}")

# # GRÁFICOS DE BARRAS EN STREAMLIT:
# # GRÁFICO 1
# ventas = df_filtrado.groupby("marca")["cantidad"].sum().reset_index()

# grafico01 = px.bar(
#     ventas,
#     x = "marca",
#     y = "cantidad",
#     title = "Ventas por Marca"
# )

# # GRÁFICO 2
# promedio = df_filtrado.groupby("marca")["precio_venta"].mean().reset_index()

# grafico02 = px.bar(
#     promedio,
#     x = "marca",
#     y = "precio_venta",
#     title = "Precio promedio por marca"
# )
# st.plotly_chart(grafico01)  # Mostrar el gráfico en el Dashboard
# st.plotly_chart(grafico02) 

#####################################################

import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

try:
    conexion_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="wigo_motors"
    )

    consulta_sql = "SELECT * FROM ventas_vehiculos"  # Consulta de toda la tabla de la DB
    df = pd.read_sql(consulta_sql, conexion_db)      # Creando el DataFrame basado en la tabla

except Exception as error:
    print(f"SE ENCONTRÓ UN PROBLEMA: {error}")


st.set_page_config(page_title="Wigo Motors", layout="wide")
st.title("WIGO MOTORS S.A.C")
st.subheader("Buscador comercial")

st.sidebar.header("Filtros")

# --- Filtro por Marca ---
opciones_marca = ["Todos"] + sorted(df["marca"].unique().tolist())
marca_sel = st.sidebar.selectbox("Marca", opciones_marca)

# --- Filtro por Sede (tienda) ---
opciones_tienda = ["Todos"] + sorted(df["tienda"].unique().tolist())
tienda_sel = st.sidebar.selectbox("Sede", opciones_tienda)

# --- Filtro por Asesor comercial ---
opciones_asesor = ["Todos"] + sorted(df["asesor_comercial"].unique().tolist())
asesor_sel = st.sidebar.selectbox("Asesor comercial", opciones_asesor)

# --- Filtro por Método de pago ---
opciones_pago = ["Todos"] + sorted(df["metodo_pago"].unique().tolist())
pago_sel = st.sidebar.selectbox("Método de pago", opciones_pago)

# --- Filtro por rango de precios (Slider) ---
precio_min = float(df["precio_venta"].min())
precio_max = float(df["precio_venta"].max())
rango_precio = st.sidebar.slider(
    "Rango de precio",
    min_value=precio_min,
    max_value=precio_max,
    value=(precio_min, precio_max)
)

# --- Aplicando los filtros en cadena (AND lógico) ---
df_filtrado = df.copy()

if marca_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["marca"] == marca_sel]

if tienda_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tienda"] == tienda_sel]

if asesor_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["asesor_comercial"] == asesor_sel]

if pago_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["metodo_pago"] == pago_sel]

df_filtrado = df_filtrado[
    (df_filtrado["precio_venta"] >= rango_precio[0]) &
    (df_filtrado["precio_venta"] <= rango_precio[1])
]

# --- Resultados ---
st.success(f"Registros encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)

st.subheader("Indicadores:")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Precio Total", f"S/{df_filtrado['precio_venta'].sum():,.2f}")
c2.metric("Unidades vendidas", f"{df_filtrado['cantidad'].sum()}")
c3.metric("Precio promedio", f"S/{df_filtrado['precio_venta'].mean():,.2f}")
c4.metric("Operaciones", len(df_filtrado))

c5, c6, c7, c8 = st.columns(4)

c5.metric("Precio mas alto", f"S/{df_filtrado['precio_venta'].max():,.2f}")
c6.metric("Precio mas bajo", f"S/{df_filtrado['precio_venta'].min():,.2f}")

# GRÁFICOS DE BARRAS EN STREAMLIT:
# GRÁFICO 1
ventas = df_filtrado.groupby("marca")["cantidad"].sum().reset_index()

grafico01 = px.bar(
    ventas,
    x="marca",
    y="cantidad",
    title="Ventas por Marca"
)

# GRÁFICO 2
promedio = df_filtrado.groupby("marca")["precio_venta"].mean().reset_index()

grafico02 = px.bar(
    promedio,
    x="marca",
    y="precio_venta",
    title="Precio promedio por marca"
)

st.plotly_chart(grafico01)
st.plotly_chart(grafico02)