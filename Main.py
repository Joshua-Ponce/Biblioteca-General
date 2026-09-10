from Biblioteca.Gestion.agregar import *
from Biblioteca.Gestion.eliminar import *
from Biblioteca.Gestion.modificar import *
from Biblioteca.Consultas.buscar import *
from Biblioteca.Consultas.mostrar import *
from Biblioteca.Consultas.contar import *
from Biblioteca.Utilidades.limpiarConsola import *


bandera = True
while bandera == True:
    limpiar_Consola()
    print("==== BIBLIOTECA - JOSHUA PONCE ====")
    opcionPrincipal = int(input("1. Agregar libro\n2. Buscar libro\n3. Mostrar libros\n4. Modificar libro\n5. Eliminar libro\n6. Contar libros\n7. Salir\nDigite el # de ópcion:  "))
    match opcionPrincipal:
        case 1:
            limpiar_Consola()
            agregar_libro()
        case 2:
            limpiar_Consola()
            buscar_libro()
            
        case 3:
            limpiar_Consola()
            mostrar_libro()
        case 4:
            limpiar_Consola()
            modificar_libro()
        case 5:
            limpiar_Consola()
            eliminar_libro()
        case 6:
            limpiar_Consola()
            contar_libro()
        case 7:
            limpiar_Consola()
            print("Muchas gracias por su uso...")
            bandera = False
        
            
            
            