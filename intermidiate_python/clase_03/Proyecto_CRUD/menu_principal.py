import os
from operaciones_crud import fun_listar
from operaciones_crud import fun_registrar
from operaciones_crud import fun_actualizar
from operaciones_crud import fun_eliminar
from indicadores import fun_indicadores




while True:
    os.system("cls") 
    print("""
    -------------------
    TECHSTORE PERÚ
    -------------------
    1.Listar tabla
    2.Consultar laptop
    3.Actualizar stock
    4.Eliminar laptop
    5.Mostrar indicadores
    6.Salir
    """)


    opcion = input("Selecciones una opción: ")


    if opcion == "1":
        fun_listar()
    elif opcion == "2":
        fun_registrar()
    elif opcion == "3":
        fun_actualizar()
    elif opcion == "4":
        fun_eliminar()
    elif opcion == "5":
        fun_indicadores()
    elif opcion == "6":
        print("Saliendo del sistema ...")
        break
    else:
        print("Opción incorrecta. Vuelva a intentarlo.\n")
        input("Presione cualquier tecla para continuar")