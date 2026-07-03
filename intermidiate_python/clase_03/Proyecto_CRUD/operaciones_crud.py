from conexion import fun_conexion



# OPERACIÓN CRUD: READ 
def fun_listar():
    conexion_db = fun_conexion() # Llamando a la función de conexion.py
    cursor_db = conexion_db.cursor() # Cursor para enviar comandos SQL                  
    consulta_sql = 'SELECT * FROM inventario_laptops;' # Consulta SQL
    cursor_db.execute(consulta_sql)   # Enviar consulta SQL                 
    respuesta_sql = cursor_db.fetchall() # Recibir consulta SQL              


    contador = 1
    for fila in respuesta_sql:      
        print(f"{contador}. {fila[1]} {fila[2]} | S/{fila[3]:,.2f} | Stock: {fila[4]} | Sede: {fila[5]} | {fila[6]}")
        contador += 1   
        
    input("Presione cualquier tecla para continuar...")

def fun_registrar():
    conexion_db = fun_conexion() 
    cursor_db = conexion_db.cursor() 
         
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad: "))
    tienda = input("Tienda: ")
    categoria = input("Categoría: ")
    
    sql = """INSERT INTO inventario_laptops
    (marca, modelo, precio_soles, stock, tienda, categoria)
    VALUES (%s,%s,%s,%s,%s,%s)"""
    
    datos = (marca, modelo, precio, stock, tienda, categoria) # Datos del input()
    
    cursor_db.execute(sql, datos)
    conexion_db.commit() # Guardar cambios
    print("Registro agregado correctamente")
    cursor_db.close()    # Deshabilitar el cursor
    conexion_db.close()  # Cerrar la conexión a la DB
    input("\nPrecione cualquier tecla para continuar...")
    


# OPERACIÓN CRUD: UPDATE


def fun_actualizar():
    conexion_db = fun_conexion() 
    cursor_db = conexion_db.cursor()     
    
    id_laptop = int(input("ID de Laptop: "))
    nuevo_stock = int(input("Nueva cantidad: "))
    
    
    sql = "UPDATE inventario_laptops SET stock = %s WHERE id_laptop = %s"
    cursor_db.execute(sql, (nuevo_stock, id_laptop))
    conexion_db.commit()
    print("Registro actualizado")
    cursor_db.close()    # Deshabilitar el cursor
    conexion_db.close()  # Cerrar la conexión a la DB
    input("\nPrecione cualquier tecla para continuar...")   
    
# OPERACIÓN CRUD: DELETE

def fun_eliminar():
    conexion_db = fun_conexion() 
    cursor_db = conexion_db.cursor()   
       
    id_laptop = int(input("ID de Laptop: "))
    
    sql = "DELETE FROM inventario_laptops WHERE id_laptop = %s"
    cursor_db.execute(sql, (id_laptop,))
    conexion_db.commit()
    print("Registro eliminado")
    cursor_db.close()   
    conexion_db.close()  
    input("\nPrecione cualquier tecla para continuar...")   
