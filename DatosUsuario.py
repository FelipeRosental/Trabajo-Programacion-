from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES


def menuUsuarios(user):
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar contraseña \n3. Eliminar usuario \n4. Hacer reserva \n5. Cancelar reserva \n6. Cerrar sesion \nIngrese una opción: ")
        
        if menu == "1": 
            Usuario.ver_datos(user.usuario,"Usuarios.txt")
        
        elif menu == "2": ### NO FUNCA BIEN  (CORREGIR LA FUNCION EN CLASES)
            login = user.usuario
            contraseña_nueva = input("Ingrese su nueva contraseña: ")
            if validacion_usuario(login) == True:
                if validacion_contraseña(contraseña_nueva) == False:
                    user.cambiar_contraseña (login, contraseña_nueva)
                else: 
                    print("La contraseña ingresada es igual a la anterior o ya está en uso")
            else: 
                print("No se encontró el usuario ingresado")       
        
        elif menu == "3":
            Usuario.eliminar_usuarios() ### CORREGIR LA FUNCION EN CLASES (HACERLA POO)
            
        elif menu == "4":
            reserva1 = Reserva()
            Reserva.agregar_reservas(reserva1, "Reservas.txt")
                 
        elif menu == "5":
            reserva2 = Reserva()
            Reserva.eliminar_reservas(reserva2, "Reservas.txt")
            
        elif menu == "6":
            #user.actualizar_usuarios("Usuarios.txt")
            #reserva1.actualizar_reservas("Reserva.txt")
            #reserva2.actualizar_reservas("Reserva.txt")
            break ### COMO USAR ESOS METODOS?
        
        else:
            print("Opcion no disponible")




