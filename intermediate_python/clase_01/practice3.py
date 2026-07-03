lista_nombres=[]
lista_apellidos=[]
lista_dni=[]
lista_areas=[]
lista_cargos=[]
lista_salarios=[]

with open("planilla_trabajadores.csv", "r") as file:
    next(file)
    for linea in file:
        datos=linea.split(",")
        nombre=datos[1]
        apellido=datos[2]
        dni=int(datos[3])
        area=datos[4]
        cargo=datos[5]
        salario=int(datos[6])
        if salario>4000:
            lista_nombres.append(nombre)
            lista_apellidos.append(apellido)
            lista_dni.append(dni)
            lista_areas.append(area)
            lista_cargos.append(cargo)
            lista_salarios.append(salario)
with open("salarios_altos.txt","w") as file:
    for i in range(len(lista_nombres)):
        file.write(f"{lista_nombres[i]} {lista_apellidos[i]} - {lista_salarios[i]} \n")