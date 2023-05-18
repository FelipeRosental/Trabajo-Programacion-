from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES


def menuUsuarios():
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ingresar datos del usuario \n2. Cambiar datos \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")
        
        if menu == "1":
            Usuario.agregar_usuario()
            
        elif menu == "2":
            Usuario.cambiar_usuarios()
                
        elif menu == "3":
            Usuario.eliminar_usuarios()
            
        elif menu == "4":
            if Cancha.total_canchas != 0:
                Reserva.agregar_reservas()
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "5":
            Reserva.eliminar_reservas()
            
        elif menu == "6":
            break
        
        else:
            print("Opcion no disponible")

### DEJAMOS INVITADOS ???

""" def menuInvitados():
    while True:
        print("DATOS Y RESERVAS - INVITADOS")
        menu = input("1. Ingresar datos del usuario \n2. Cambiar datos \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")
        
        if menu == "1":
            club1.agregar_invitados()
         
        elif menu == "2":
            club1.cambiar_invitados()
               
        elif menu == "3":
            club1.eliminar_invitados()
            
        elif menu == "4":
            if club1.total_canchas != 0:
                club1.agregar_reservas()
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "5":
            club1.eliminar_reservas()
            
        elif menu == "6":
            break
        
        else:
            print("Opcion no disponible") """


