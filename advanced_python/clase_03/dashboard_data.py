import streamlit as st
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


st.set_page_config(page_title="Wigo Motors", layout="wide")
st.title("WIGO MOTORS S.A.C")   
st.subheader("Buscador comercial de vehiculos")
st.write("Consulta de informacion comercial utilizando Streamlit")


marcas=df["marca"].unique().tolist()
marca_seleccionada=st.selectbox("Seleccione una marca",["Todas"]+marcas)

if marca_seleccionada!= "Todas":
    df=df[df["marca"]== marca_seleccionada]

busqueda=st.text_input("Buscar modelo, asesor comercial o tienda")

if busqueda:
    df=df[
        df["modelo"].str.contains(busqueda, case=False) |
        df["asesor_comercial"].str.contains(busqueda, case=False) |
        df["tienda"].str.contains(busqueda, case=False) 
    ]

if len(df)==0:
    st.warning("No se encontraron resultados")
else:
    st.dataframe(df)

st.success(f"Registros encontrados: {len(df)}")