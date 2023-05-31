from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES


def menuUsuarios(user):
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Cancelar reserva \n7. Cerrar sesion \nIngrese una opción: ")
        
        if menu == "1": 
            Usuario.ver_datos(user.usuario,"Usuarios.txt")
        
        elif menu == "2": 
            user.cambiar_usuario("Usuarios.txt")     
        
        elif menu == "3":
            user.eliminar_usuario("Usuarios.txt") 
            break
        
        elif menu == "4":
            Reserva.ver_reservas("Reservas.txt", user.dni) 
        
        elif menu == "5":
            disponibles = Cancha.ver_horarios("Canchas.txt")
            print("Canchas disponibles: ")
            Cancha.ver_canchas("Canchas.txt")
            reserva1 = Reserva(str(user.dni))
            if str(reserva1.horareserva) in set(disponibles.values()):
                horario = str(reserva1.horareserva)
                codigo = input("Seleccione el codigo de la cancha que desea: ")
                while codigo not in set(disponibles.keys()):
                    print("Codigo no disponible")
                    codigo = input("Seleccione el codigo de la cancha que desea: ")
                Reserva.agregar_reservas(reserva1, "Reservas.txt")
                reservada = Cancha.buscar_cancha("Canchas.txt", codigo, horario) 
                reservada.eliminar_canchas("Canchas.txt")
            else: 
                print ("No hay canchas disponibles en ese horario")
            
        elif menu == "6":
            reserva2 = Reserva(str(user.dni))
            Reserva.eliminar_reservas(reserva2, "Reservas.txt")
            
        elif menu == "7":
            #user.actualizar_usuarios("Usuarios.txt")
            #reserva1.actualizar_reservas("Reserva.txt")
            #reserva2.actualizar_reservas("Reserva.txt")
            break ### COMO USAR ESOS METODOS?
        
        else:
            print("Opcion no disponible")




