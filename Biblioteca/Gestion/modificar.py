from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import limpiar_Consola,continuar_Consola
def modificar_libro():
    opcionCase = int(input("1. Modificar Código\n2. Modificar Nombre\n3. Modificar Autor\n4. Modificar Todo\nDigite el # de ópcion: "))
    match opcionCase:
        case 1:
            limpiar_Consola()
            modificarLibro = input("Digite el código del libro a modificar: ")
            nuevoCodigo = input("Digite el nuevo código: ")
            libros_general[nuevoCodigo] = libros_general[modificarLibro]
            del libros_general[modificarLibro]
            continuar_Consola()
        case 2:
            limpiar_Consola()
            modificarLibro = input("Digite el código del libro a modificar: ")
            nuevoTitulo = input("Digite el nuevo título: ")
            libros_general[modificarLibro]["Titulo"] = nuevoTitulo
            continuar_Consola()
        case 3:
            limpiar_Consola()
            modificarLibro = input("Digite el código del libro a modificar: ")
            nuevoAutor = input("Digite el nuevo autor: ")
            libros_general[modificarLibro]["Autor"] = nuevoAutor
            continuar_Consola()
        case 4:
            limpiar_Consola()
            modificarLibro = input("Digite el código del libro a modificar: ")
            nuevoCodigo = input("Digite el nuevo código: ")
            nuevoTitulo = input("Digite el nuevo título: ")
            nuevoAutor = input("Digite el nuevo autor: ")
            libros_general[modificarLibro]["Titulo"] = nuevoTitulo
            libros_general[modificarLibro]["Autor"] = nuevoAutor
            libros_general[nuevoCodigo] = libros_general[modificarLibro]
            del libros_general[modificarLibro]
            continuar_Consola()
            
            
            
            
        