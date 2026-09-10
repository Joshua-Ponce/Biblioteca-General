from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
def agregar_libro():
    agregarLibro = input("Digite el código del libro que desea agregar: ")
    libros_general[agregarLibro] = {}
    agregarNombre = input(f"Digite el título (#{agregarLibro}): ")
    libros_general[agregarLibro]["Titulo"] = agregarNombre
    agregarAutor = input("Digite el nombre del Autor: ")
    libros_general[agregarLibro]["Autor"] = agregarAutor
    continuar_Consola()

    
