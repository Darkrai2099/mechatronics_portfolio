lista_nombres=[]
lista_apellidos=[]
lista_dni=[]
lista_areas=[]
lista_cargos=[]
lista_salarios=[]

with open("planilla_trabajadores.csv", "r") as archivo:
    next(archivo)
    for linea in archivo:
        datos=linea.split(",")
        nombre=datos[1]
        apellido=datos[2]
        dni=int(datos[3])
        area=datos[4]
        cargo=datos[5]
        salario=int(datos[6])
        lista_nombres.append(nombre)
        lista_apellidos.append(apellido)
        lista_dni.append(dni)
        lista_areas.append(area)
        lista_cargos.append(cargo)
        lista_salarios.append(salario)

dni_buscado=int(input("Ingrese DNI: "))
if dni_buscado in lista_dni:
    trabajador=lista_dni.index(dni_buscado)
    nombre_trabajador=lista_nombres[trabajador]
    apellido_trabajador=lista_apellidos[trabajador]
    dni_trabajador=lista_dni[trabajador]
    area_trabajador=lista_areas[trabajador]
    cargo_trabajador=lista_cargos[trabajador]
    salario_trabajador=lista_salarios[trabajador]
    print(f"Nombre: {nombre_trabajador} {apellido_trabajador}")
    print(f"Area: {area_trabajador}")
    print(f"Cargo: {cargo_trabajador}")
    print(f"Salario: {salario_trabajador}")
else:
    print("Trabajador no encontrado")
