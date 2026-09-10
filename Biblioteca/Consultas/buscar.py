from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import limpiar_Consola,continuar_Consola
def buscar_libro():
    buscarLibro = input("Digite el código del libro a buscar: ")
    limpiar_Consola()
    print(f"Código: [{buscarLibro}]\nTítulo: {libros_general[buscarLibro]["Titulo"]}\nAutor: {libros_general[buscarLibro]["Autor"]}")
    continuar_Consola()
    
            