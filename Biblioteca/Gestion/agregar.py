from Biblioteca.Datos.inventario import *
from Biblioteca.Utilidades.limpiarConsola import *
def agregar_libro():
    while True:
        limpiar_Consola()
        agregarLibro = input("Digite el código del libro que desea agregar: ")
        if agregarLibro not in libros_general:
            libros_general[agregarLibro] = {}
            agregarNombre = input(f"Digite el título (#{agregarLibro}): ")
            libros_general[agregarLibro]["Titulo"] = agregarNombre
            agregarAutor = input("Digite el nombre del Autor: ")
            libros_general[agregarLibro]["Autor"] = agregarAutor
            continuar_Consola()
            break
        else:
            input("\nCódigo ya existente... Enter para continuar")
        
    

    
