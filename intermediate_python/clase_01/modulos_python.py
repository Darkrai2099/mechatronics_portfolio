from datetime import datetime
import os

fecha_actual=datetime.now().strftime("%d-%m-&Y %H: %M: %S %p")
print(fecha_actual)

os.chdir(r"C:\Users\ACER\Documents")

ruta_actual=os.getcwd()
print(f"Ubicacion actual: {ruta_actual}")

recursos=os.listdir()
print(recursos)