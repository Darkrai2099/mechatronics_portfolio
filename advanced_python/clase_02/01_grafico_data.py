import matplotlib.pyplot as plt
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


#grafico

""" plt.figure(figsize=(10,6))
plt.bar(
    ventas_marca.index,
    ventas_marca.values,
    color="skyblue",
    edgecolor="black"
)
plt.title("Cantidad de vehiculos vendidos por marca",fontsize=20)
plt.xlabel("Marca")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()
 """

fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    ventas_marca.index,
    ventas_marca.values,
    color="#4E79A7",
    edgecolor="black",
    linewidth=0.8
)

ax.set_title(
    "Cantidad de vehículos vendidos por marca",
    fontsize=18,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Marca", fontsize=12)
ax.set_ylabel("Cantidad de vehículos vendidos", fontsize=12)

ax.tick_params(axis='x', rotation=30)

ax.grid(axis="y", linestyle="--", alpha=0.4)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Mostrar el valor encima de cada barra
for bar in bars:
    y = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        y + max(ventas_marca.values)*0.01,
        f"{int(y)}",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

ax.set_ylim(0, max(ventas_marca.values)*1.12)

plt.tight_layout()
plt.show()
