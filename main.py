from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES

usuarios_guardados = Usuario.leer_usuarios("Usuarios.txt")
reservas_guardadas = Reserva.leer_reservas("Reservas.txt")
canchas_guardadas = Cancha.leer_canchas("Canchas.txt")

def menuPrincipal():

    while True:
        print("MENU PRINCIPAL")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Salir \nIngrese una opción: ")
        if menu == "1":
            user = Usuario()
            user.registrar_usuario(usuarios_guardados)
                
        elif menu == "2":
            usuario = input("Ingrese su usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            for us in usuarios_guardados.values():
                if usuario == us.usuario and contraseña == us.contraseña:
                    user = Usuario.buscar_usuario(usuarios_guardados,usuario,contraseña)
                    print("Sesion iniciada como " + str(usuario))
                    if usuario in {"admin", "Admin", "ADMIN"}:
                        menuAdmins(user) 
                    else:
                        menuUsuarios(user)
            else:
                print("Datos incorrectos")  ### POR ALGUNA RAZON TIRA ESTE MENSAJE CADA VEZ QUE SE CIERRA SESION... CORREGIR
                     
        elif menu == "3":
            with open("Usuarios.txt","w") as baseusuarios:
                for us in usuarios_guardados.values():
                    baseusuarios.write(f"{us.dni};{us.nombre};{us.apellido};{us.telefono};{us.edad};{us.email};{us.usuario};{us.contraseña};\n")
            break
        else: 
            print("Opcion no valida")

def menuUsuarios(user):
    
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Cancelar reserva \n7. Cerrar sesion \nIngrese una opción: ")
        
        if menu == "1": 
            print(user) 
            
            # ACA ABAJO AGREGARIA UN MENU QUE PERMITA ELEGIR SI VOLVER AL MENUUSUARIO O SALIR DEL PROGRAMA
            #  O QUE AL PRESIONAR ENTER TE VUELVA AL MENUUSUARIOS, PERO Q NO SE HAGA AUTOMATICAMENTE (ES ESTETICA NOMAS)
            
        elif menu == "2": 
            user.cambiar_usuario(usuarios_guardados)
        
        elif menu == "3":
            user.eliminar_usuario(usuarios_guardados)
            break
        
        elif menu == "4":
            for reserva in reservas_guardadas.values():     ### NO FUNCA BIEN, CORREGIR 
                if user.dni == reserva.codigo:
                    print(reserva)
            
        elif menu == "5":
            pass
            
        elif menu == "6":
            pass
            
        elif menu == "7":
            break 
        
        else:
            print("Opcion no disponible")
            
def menuAdmins(user):
    
    while True:
        print("ADMINISTRACION")
        menu = input("1. Ver canchas\n2. Agregar cancha\n3. Eliminar cancha\n4. Ver mis datos\n5. Cambiar mis datos\n6. Borrar mi cuenta\n7. Salir \nIngrese una opción: ")
        if menu == "1":
            for cancha in canchas_guardadas.values():
                print(cancha)
            
        elif menu == "2":
            cancha = Cancha()
            cancha.agregar_cancha(canchas_guardadas)
            
        elif menu == "3":
            codigo = input("Ingrese el codigo de la cancha a eliminar: ")
            Cancha.eliminar_cancha(codigo, canchas_guardadas)
            pass
                    
        elif menu == "4": 
            print(user) 
            
        elif menu == "5": 
            user.cambiar_usuario(usuarios_guardados)
        
        elif menu == "6":
            user.eliminar_usuario(usuarios_guardados)
            break
            
        elif menu == "7":
            with open("Canchas.txt","w") as basecanchas:
                for canchas in canchas_guardadas.values():
                    basecanchas.write(f"{canchas.codigo};{canchas.techada};{canchas.piso};{canchas.estado};\n")
            break
        
        else: 
            print("Opcion no disponible") 
          
menuPrincipal()
   
### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO 