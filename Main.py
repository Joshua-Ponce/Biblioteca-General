from Biblioteca.Gestion.agregar import *
from Biblioteca.Gestion.eliminar import *
from Biblioteca.Gestion.modificar import *
from Biblioteca.Consultas.buscar import *
from Biblioteca.Consultas.mostrar import *
from Biblioteca.Consultas.contar import *
from Biblioteca.Utilidades.limpiarConsola import *
from Biblioteca.Utilidades.mostrarMenu import *

#Joshua Ponce #1 Proyecto en github
bandera = True
while bandera == True:
    limpiar_Consola()
    mostrar_Menu()
    while True:
        try:
          opcion = int(input("Digite una opción (1-7):  "))
          if opcion < 1 or opcion > 7:
              limpiar_Consola()
              mostrar_Menu()
              print("\n[ALERTA] Opción fuera de rango.")
              continue
          break
        except ValueError:
            limpiar_Consola()
            mostrar_Menu()
            print("\n[ALERTA] Válido solamente números.")
     
    match opcion:
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
        
            
            
            