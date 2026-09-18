from Biblioteca.Datos.inventario import *
from Biblioteca.Utilidades.limpiarConsola import *
from Biblioteca.Utilidades.manejoErrores import *
from Biblioteca.Utilidades.mostrarMenu import mostrar_Submenu
def modificar_libro():
    while True:
        if sin_Libro():
            break
        else:
            mostrar_Submenu()
            while True:
                try:
                    opcionCase = int(input("Digite una opción (1-5): "))
                    if opcionCase < 1 or opcionCase > 5:
                        limpiar_Consola()
                        mostrar_Submenu ()
                        print("\n[ALERTA] Opción fuera de rango.")
                        continue
                    break
                except ValueError:
                    limpiar_Consola()
                    mostrar_Submenu()
                    print("\n[ALERTA] Válido solamente números.")
        match opcionCase:
            case 1:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if modificarLibro in libros_general:
                        nuevoCodigo = input("Digite el nuevo código: ")
                        libros_general[nuevoCodigo] = libros_general[modificarLibro]
                        del libros_general[modificarLibro]
                        continuar_Consola()
                        break
                    else:
                        input("\nCódigo no existente... Enter para continuar")         
            case 2:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if modificarLibro in libros_general:
                        nuevoTitulo = input("Digite el nuevo título: ")
                        libros_general[modificarLibro]["Titulo"] = nuevoTitulo
                        continuar_Consola()
                        break
                    else:
                        input("\nCódigo no existente... Enter para continuar")
            case 3:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if modificarLibro in libros_general:
                        nuevoAutor = input("Digite el nuevo autor: ")
                        libros_general[modificarLibro]["Autor"] = nuevoAutor
                        continuar_Consola()
                        break
                    else:
                        input("\nCódigo no existente... Enter para continuar")
            case 4:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if modificarLibro in libros_general:
                        nuevoCodigo = input("Digite el nuevo código: ")
                        nuevoTitulo = input("Digite el nuevo título: ")
                        nuevoAutor = input("Digite el nuevo autor: ")
                        libros_general[modificarLibro]["Titulo"] = nuevoTitulo
                        libros_general[modificarLibro]["Autor"] = nuevoAutor
                        libros_general[nuevoCodigo] = libros_general[modificarLibro]
                        del libros_general[modificarLibro]
                        continuar_Consola()
                        break
                    else:
                        input("\nCódigo no existente... Enter para continuar")
            case 5:
                break        
            
            
            
        