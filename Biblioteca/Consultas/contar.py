from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
from Biblioteca.Utilidades.manejoErrores import *
def contar_libro():
    while True:
        if sin_Libro():
            break
        else:
            print(f"-- Cantidad de libros totales: {len(libros_general)} --")
            continuar_Consola()
            break
        