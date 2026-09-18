from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import *
#1 Ningun libro en la biblioteca aún
def sin_Libro():
    if len(libros_general) <= 0:
        limpiar_Consola()
        input("[ADVERTENCIA] NO HAY LIBROS EXISTENTES... ENTER PARA CONTINUAR\n")
        return True
    else:
        return False