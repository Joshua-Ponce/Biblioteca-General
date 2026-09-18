from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import limpiar_Consola,continuar_Consola
from Biblioteca.Utilidades.manejoErrores import *
def buscar_libro():
    while True:
        limpiar_Consola()
        if sin_Libro():
            break
        else:
            buscarLibro = input("Digite el código del libro a buscar: ")
            if buscarLibro in libros_general:
                limpiar_Consola()
                print(f"Código: [{buscarLibro}]\nTítulo: {libros_general[buscarLibro]["Titulo"]}\nAutor: {libros_general[buscarLibro]["Autor"]}")
                continuar_Consola()
                break
            else:
                input("\nCódigo no existente... Enter para continuar")
            