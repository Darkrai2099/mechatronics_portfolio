cantidad=int(input("Cuantos estudiantes desea registrar? "))
with open("estudiantes.txt", "w") as archivo:
    for i in range(cantidad):
        nombre=input(f"Ingrese el nombre del estudiante {i+1}:")
        archivo.write(f"{nombre}\n")
print("Archivo generado correctamente.")