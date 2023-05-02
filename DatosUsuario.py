from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL


def menu1():
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ingresar datos del usuario \n2. Eliminar usuario \n3. Hacer reserva \n4. Cancelar reserva \n5. Salir \nIngrese una opción: ")
        
        if menu == "1":
            club1.agregar_usuarios()
            
        elif menu == "2":
            club1.eliminar_usuarios()
            
        elif menu == "3":
            if club1.mostrar_canchas() != 0:
                club1.agregar_reservas()
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "4":
            club1.eliminar_reservas()
            
        elif menu == "5":
            break
        
        else:
            print("Opcion no disponible")





