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
        print("INICIO DE SESION")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Salir \nIngrese una opción: ")
        if menu == "1":
            user = Usuario()
            if user.dni not in usuarios_guardados.keys():
                usuarios_guardados[user.dni] = user        #ANTES ESTABA ESTO:f"{user.nombre};{user.apellido};{user.telefono};{user.edad};{user.email};{user.usuario};{user.contraseña}"
                print("Usuario registrado correctamente")
            else:                               
                print("El usuario ya está ingresado")
                
        elif menu == "2":
            usuario = input("Ingrese su usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            for us in usuarios_guardados.values():
                if usuario == us.usuario and contraseña == us.contraseña:
                    print("Sesion iniciada como " + str(usuario))
                    if usuario in {"admin", "Admin", "ADMIN"}:
                        menuAdmins()
                    else:
                        user = Usuario.buscar_usuario(usuarios_guardados,usuario,contraseña)
                        menuUsuarios(user)
                    break
            else:
                print("Datos incorrectos")
                     
        elif menu == "3":
            with open("Usuarios.txt","w") as baseusuarios:
                for us in usuarios_guardados.values():
                    baseusuarios.write(str(us))
                
            break
        else: 
            print("Opcion no valida")



def menuUsuarios(user):
    
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Cambiar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Cancelar reserva \n7. Cerrar sesion \nIngrese una opción: ")
        
        if menu == "1": 
            usuario = usuarios_guardados.get(user.dni)
            print(usuario.__str__())
            
        elif menu == "2": 
            pass     
        
        elif menu == "3":
            pass
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
            
def menuAdmins():
    
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
            pass
        
        elif menu == "5": 
            pass   
        
        elif menu == "6":
            pass
            
        
        elif menu == "7":
            break
        
        else: 
            print("Opcion no disponible") 
          
menuPrincipal()
   
### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO 