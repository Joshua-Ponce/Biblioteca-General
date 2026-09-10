from Biblioteca.Datos.inventario import libros_general
from Biblioteca.Utilidades.limpiarConsola import continuar_Consola
def mostrar_libro():
    print("--- BIBLIOTECA GENERAL ---")
    for codigo,informacion in libros_general.items():
        print(f"---{codigo}---\nTítulo: {informacion["Titulo"]}\nAutor: {informacion["Autor"]}")
    continuar_Consola()
        