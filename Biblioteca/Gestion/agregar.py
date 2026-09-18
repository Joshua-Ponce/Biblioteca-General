from Biblioteca.Datos.inventario import *
from Biblioteca.Utilidades.limpiarConsola import *
from Biblioteca.Utilidades.manejoErrores import *
def agregar_libro():
    while True:
        limpiar_Consola()
        agregarLibro = input("Digite el código del libro que desea agregar: ")
        if sin_Valor(agregarLibro):
            continue
        else:
            if agregarLibro not in libros_general:
                while True:
                    libros_general[agregarLibro] = {}
                    agregarNombre = input(f"Digite el título (#{agregarLibro}): ")
                    if sin_Valor(agregarNombre):
                        continue
                    else:
                        libros_general[agregarLibro]["Titulo"] = agregarNombre
                        while True:
                            agregarAutor = input(f"Digite el nombre del Autor (#{agregarLibro} / -{agregarNombre}-): ")
                            if sin_Valor(agregarAutor):
                                continue
                            else:
                                libros_general[agregarLibro]["Autor"] = agregarAutor
                            continuar_Consola()
                            break
                    break    
                
            else:
                input("\nCódigo ya existente... Enter para continuar")
                continue
        break
    

    
