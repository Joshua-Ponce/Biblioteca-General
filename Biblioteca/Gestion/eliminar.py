from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import *
from Biblioteca.Consultas.mostrar import *
from Biblioteca.Utilidades.manejoErrores import *

def eliminar_libro():
    while True:
        if sin_Libro():
            break
        else:
            limpiar_Consola()
            mostrar_libro()
            eliminarLibro = input("Digite el código del libro a eliminar: ")
            if eliminarLibro in libros_general:
                del libros_general[eliminarLibro]
                limpiar_Consola()
                print("Eliminado exitosamente.")
                continuar_Consola()
                break
            else:
                input("\nCódigo no existente... Enter para continuar")
        
    