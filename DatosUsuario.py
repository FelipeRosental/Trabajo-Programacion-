from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES


def menuUsuarios(usuario, contraseña):
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar datos \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")
        
        if menu == "1": ### NO FUNCA
            for user in Usuario.set_usuarios:
                if usuario == user[6] and contraseña == user[7]:
                    print (user)
        
        elif menu == "2":
            Usuario.cambiar_usuarios()
                
        elif menu == "3":
            Usuario.eliminar_usuarios()
            
        elif menu == "4":
            reserva1 = Reserva()
            Reserva.agregar_reservas(reserva1, "Reserva.txt")
                 
        elif menu == "5":
            reserva2 = Reserva()
            Reserva.eliminar_reservas(reserva2, "Reserva.txt")
            
        elif menu == "6":
            #user.actualizar_usuarios("Usuarios.txt")
            #reserva1.actualizar_reservas("Reserva.txt")
            #reserva2.actualizar_reservas("Reserva.txt")
            break
        
        else:
            print("Opcion no disponible")




