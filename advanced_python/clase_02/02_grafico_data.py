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

#Facturacion total de vehiculos vendidos por marca
facturacion_marca=df.groupby("marca")["facturacion_total"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    facturacion_marca.index,
    facturacion_marca.values,
    color="#2E8B57",      # Verde SeaGreen
    edgecolor="black",
    linewidth=0.8
)

# Título
ax.set_title(
    "Facturación total de vehículos vendidos por marca",
    fontsize=18,
    fontweight="bold",
    pad=15
)

# Etiquetas
ax.set_xlabel("Marca", fontsize=12)
ax.set_ylabel("Facturación total (S/.)", fontsize=12)

# Etiquetas del eje X
plt.xticks(rotation=30, ha="right")

# Cuadrícula
ax.grid(axis="y", linestyle="--", alpha=0.35)

# Quitar bordes innecesarios
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Mostrar la facturación encima de cada barra
for bar in bars:
    valor = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width()/2,
        valor + max(facturacion_marca.values)*0.015,
        f"S/. {valor:,.2f}",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )

ax.set_ylim(0, max(facturacion_marca.values)*1.18)

plt.tight_layout()
plt.show()