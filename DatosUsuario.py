from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL

def menuUsuarios():
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ingresar datos del usuario \n2. Cambiar datos \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")
        
        if menu == "1":
            club1.agregar_usuarios()
            
        elif menu == "2":
            club1.cambiar_usuarios()
                
        elif menu == "3":
            club1.eliminar_usuarios()
            
        elif menu == "4":
            if club1.total_canchas != 0:
                club1.agregar_reservas()
                with open("Reservas.txt", "a") as archivo:
                    archivo.write ("(USUARIO)" + "\n")
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "5":
            club1.eliminar_reservas()
            
        elif menu == "6":
            break
        
        else:
            print("Opcion no disponible")

def menuInvitados():
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
                with open("Reservas.txt", "a") as archivo:
                    archivo.write ("(INVITADO)" + "\n")
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "5":
            club1.eliminar_reservas()
            
        elif menu == "6":
            break
        
        else:
            print("Opcion no disponible")


