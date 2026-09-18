from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
from Biblioteca.Utilidades.manejoErrores import *
def mostrar_libro():
    while True:
        if sin_Libro():
            break
        else:
            print("\t--- [BIBLIOTECA GENERAL] ---")
            for i in range(len(libros_general)):
                for codigo,informacion in libros_general.items():
                    print(f"\t\t---[#{i+1}]---\n\tCódigo: [{codigo}]\n\tTítulo: [{informacion["Titulo"]}]\n\tAutor: [{informacion["Autor"]}]") 
                    continuar_Consola()
            break
            