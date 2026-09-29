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
                    if validar_Noexistente(modificarLibro):
                        continue
                    while True:
                        limpiar_Consola()
                        nuevoCodigo = input("Digite el nuevo código: ")
                        if validar_codigo(nuevoCodigo):
                            continue
                        libros_general[nuevoCodigo] = libros_general[modificarLibro]
                        del libros_general[modificarLibro]
                        continuar_Consola()
                        break
                    break
                       
            case 2:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if validar_Noexistente(modificarLibro):
                        continue
                    nuevoTitulo = input("Digite el nuevo título: ")
                    libros_general[modificarLibro]["Titulo"] = nuevoTitulo
                    continuar_Consola()
                    break
            case 3:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if validar_Noexistente(modificarLibro):
                        continue
                    nuevoAutor = input("Digite el nuevo autor: ")
                    libros_general[modificarLibro]["Autor"] = nuevoAutor
                    continuar_Consola()
                    break
            case 4:
                while True:
                    limpiar_Consola()
                    modificarLibro = input("Digite el código del libro a modificar: ")
                    if validar_Noexistente(modificarLibro):
                        continue
                    while True:
                     limpiar_Consola()
                     nuevoCodigo = input("Digite el nuevo código: ")
                     if validar_codigo(nuevoCodigo):
                         continue
                     break
                    nuevoTitulo = input("Digite el nuevo título: ")
                    nuevoAutor = input("Digite el nuevo autor: ")
                    libros_general[modificarLibro]["Titulo"] = nuevoTitulo
                    libros_general[modificarLibro]["Autor"] = nuevoAutor
                    libros_general[nuevoCodigo] = libros_general[modificarLibro]
                    del libros_general[modificarLibro]
                    continuar_Consola()
                    break
            case 5:
                break        
            
            
            
        