from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
def contar_libro():
    print(f"-- Cantidad de libros totales: {len(libros_general)} --")
    continuar_Consola()