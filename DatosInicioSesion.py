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
                print("Datos incorrectos")
                     
        elif menu == "3":
            with open("Usuarios.txt","w") as baseusuarios:
                for us in usuarios_guardados.values():
                    baseusuarios.write(str(us) + "\n")
                
            break
        else: 
            print("Opcion no valida")



def menuUsuarios(user):
    
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Cancelar reserva \n7. Cerrar sesion \nIngrese una opción: ")
        
        if menu == "1": 
            print(f" Nombre: {user.nombre} \n Apellido: {user.apellido} \n DNI: {user.dni} \n Telefono: {user.telefono} \n Edad: {user.edad} \n Mail: {user.email}")
            
            # ACA ABAJO AGREGARIA UN MENU QUE PERMITA ELEGIR SI VOLVER AL MENUUSUARIO O SALIR DEL PROGRAMA
            #  O QUE AL PRESIONAR ENTER TE VUELVA AL MENUUSUARIOS, PERO Q NO SE HAGA AUTOMATICAMENTE (ES ESTETICA NOMAS)
            
        elif menu == "2": 
            user.cambiar_usuario(usuarios_guardados)
        
        elif menu == "3":
            usuarios_guardados.pop(user.dni)
            print("Datos eliminados con exito")
            break
        
        elif menu == "4":
            pass
        
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
        menu = input("1. Ver canchas\n2. Agregar canchas\n3. Eliminar canchas\n4. Ver mis datos\n5. Cambiar mis datos\n6. Borrar mi cuenta\n7. Salir \nIngrese una opción: ")
        if menu == "1":
            pass
            
        elif menu == "2":
            pass
            
        elif menu == "3":
            pass
                    
        elif menu == "4": 
            print(f" Nombre: {user.nombre} \n Apellido: {user.apellido} \n DNI: {user.dni} \n Telefono: {user.telefono} \n Edad: {user.edad} \n Mail: {user.email}")
        
        elif menu == "5": 
            user.cambiar_usuario(usuarios_guardados)
        
        elif menu == "6":
            usuarios_guardados.pop(user.dni)
            print("Datos eliminados con exito")
            break
            
        elif menu == "7":
            break
        
        else: 
            print("Opcion no disponible") 
          
menuPrincipal()
   
### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO 