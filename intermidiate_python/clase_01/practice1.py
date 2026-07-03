lista_nombres=[]
lista_apellidos=[]
lista_areas=[]
lista_salarios=[]

with open("planilla_trabajadores.csv", "r") as archivo:
    next(archivo)
    for linea in archivo:
        datos=linea.split(",")
        nombre=datos[1]
        apellido=datos[2]
        area=datos[4]
        salario=int(datos[6])
        lista_nombres.append(nombre)
        lista_apellidos.append(apellido)
        lista_areas.append(area)
        lista_salarios.append(salario)
mejor=max(lista_salarios)
trabajador=lista_salarios.index(mejor)
nombre_trabajador=lista_nombres[trabajador]
apellido_trabajador=lista_apellidos[trabajador]
area_trabajador=lista_areas[trabajador]
salario_trabajador=lista_salarios[trabajador]
print("="*25)
print("TRABAJADOR MEJOR PAGADO")
print("="*25)
print(f"Nombre: {nombre_trabajador} {apellido_trabajador}")
print(f"Area: {area_trabajador}")
print(f"Salario: {salario_trabajador}")