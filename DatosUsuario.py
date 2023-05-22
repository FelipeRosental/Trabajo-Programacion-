from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES


def menuUsuarios():
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar datos \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")
        
        if menu == "1": ### NO FUNCA
            for user in Usuario.leer_usuarios(user,"Usuarios.txt"):
                print(user)
        
        elif menu == "2":
            Usuario.cambiar_usuarios()
                
        elif menu == "3":
            Usuario.eliminar_usuarios()
            
        elif menu == "4":
            Reserva.agregar_reservas()
                 
        elif menu == "5":
            Reserva.eliminar_reservas()
            
        elif menu == "6":
            #user.actualizar_usuarios("Usuarios.txt")
            break
        
        else:
            print("Opcion no disponible")




