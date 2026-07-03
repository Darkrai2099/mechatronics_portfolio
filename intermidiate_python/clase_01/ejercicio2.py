lista_salarios=[]

with open("planilla_trabajadores.csv", "r") as archivo:
    next(archivo)
    for linea in archivo:
        datos=linea.split(",")
        salario=int(datos[6])
        lista_salarios.append(salario)
planilla=sum(lista_salarios)      
promedio=planilla/len(lista_salarios)
mayor=max(lista_salarios)
menor=min(lista_salarios)
print("="*20)
print("REPORTE SALARIAL")
print("="*20)
print(f"{'Planilla total:':<10} {planilla}")
print(f"{'Salario promedio:':<10} {promedio}")
print(f"{'Salario maximo:':<10} {mayor}")
print(f"{'Salario minimo:':<10} {menor}")