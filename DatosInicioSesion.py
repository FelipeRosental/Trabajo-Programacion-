from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from DatosUsuario import * ### DATOS DE USUARIOS Y RESERVAS
from DatosCanchas import * ### DATOS DE CANCHAS


   
def menuPrincipal():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Cambiar contraseña \n4. Ingresar como administrador \n5. Salir \nIngrese una opción: ")

        if menu == "1":
            user = Usuario()
            if validacion_usuario(user.usuario) == False:
                if validacion_contraseña (user.contraseña) == False:
                    user.registrar_usuario (user.usuario,user.contraseña)
                    user.actualizar_usuarios ("Usuarios.txt")
                else: 
                    print("La contraseña ya está en uso")
            else: 
                print("El usuario ya se encuentra ingresado")

        elif menu == "2":
            usuario = input("Ingrese usuario: ")
            contraseña = input("Ingrese contraseña: ")
            if Usuario.iniciar_sesion (usuario, contraseña) is True:
                print("Sesion iniciada como: " + str(usuario))
                menuUsuarios()
            else:
                print("Usuario o Contraseña incorrectos")
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Inicio de sesion incorrecto " + "\n")
        elif menu == "3": ### NO FUNCA BIEN 
            login = user.usuario
            contraseña_nueva = input("Ingrese su nueva contraseña: ")
            if validacion_usuario(login) == True:
                if validacion_contraseña(contraseña_nueva) == False:
                    user.cambiar_contraseña (login, contraseña_nueva)
                else: 
                    print("La contraseña ingresada es igual a la anterior o ya está en uso")
            else: 
                print("No se encontró el usuario ingresado")
        elif menu == "4":
            user = Usuario()
            if user.es_administrador (user.usuario,user.contraseña) == True:
                user.registrar_usuario (user.usuario,user.contraseña)
                user.actualizar_usuarios("Usuarios.txt")
                print ("Sesion iniciada como administrador")
                menuCanchas()
            else: 
                print ("Inicio de sesion incorrecto")
        elif menu == "5":
            break
        else: 
            print("Opcion no valida")

menuPrincipal()

### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO Y ABRIR EN SIMULTANEO LOS ARCHIVOS DE TEXTO 