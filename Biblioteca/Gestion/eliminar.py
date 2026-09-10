from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
def eliminar_libro():
    eliminarLibro = input("Digite el código del libro a eliminar: ")
    del libros_general[eliminarLibro]
    continuar_Consola()