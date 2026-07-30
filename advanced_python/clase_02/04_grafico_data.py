import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import mysql.connector
import numpy as np

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

#Participacion porcentual por marca:
participacion_marca=df.groupby("marca")["cantidad"].sum().sort_values(ascending=False)
participacion_marca=(participacion_marca/participacion_marca.sum())*100

# Datos
labels = participacion_marca.index
valores = participacion_marca.values

# Paleta de colores profesional
colores = cm.Blues_r(np.linspace(0.15, 0.85, len(labels)))

fig, ax = plt.subplots(figsize=(9, 7))

# Resaltar la marca con mayor participación (explode)
explode = [0.06 if i == 0 else 0 for i in range(len(labels))]

wedges, texts, autotexts = ax.pie(
    valores,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False,
    colors=colores,
    explode=explode,
    pctdistance=0.75,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 10}
)

# Estilo de los porcentajes internos
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)

# Efecto "donut" (opcional, se ve muy profesional)
centro = plt.Circle((0, 0), 0.45, fc='white')
fig.gca().add_artist(centro)

ax.set_title('Participación porcentual por marca', fontsize=14, fontweight='bold', pad=20)
ax.axis('equal')  # Asegura que el pie sea circular

plt.tight_layout()
plt.savefig('participacion_marca.png', dpi=300, bbox_inches='tight')
plt.show()