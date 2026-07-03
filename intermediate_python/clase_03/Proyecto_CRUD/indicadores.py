from conexion import fun_conexion

def fun_indicadores():
    conexion_db = fun_conexion() # Llamando a la función de conexion.py
    cursor_db = conexion_db.cursor() # Cursor para enviar comandos SQL                  
    consulta_sql = 'SELECT COUNT(*), AVG(precio_soles), MAX(precio_soles),MIN(precio_soles), SUM(stock) FROM inventario_laptops;' 
    cursor_db.execute(consulta_sql)   # Enviar consulta SQL                      
    total_laptops,promedio,maximo,minimo,stock=cursor_db.fetchone()
    print("="*20)
    print("INDICADORES GENERALES")
    print("="*20)    
    print(f"Total de laptops: {total_laptops}")
    print(f"Precio promedio: {promedio}")
    print(f"Precio maximo: {maximo}")
    print(f"Precio minimo: {minimo}")
    print(f"Stock total: {stock}")
    input("\nPresione ENTER para volver al menú...")
