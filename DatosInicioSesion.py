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
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Ingresar como administrador \n4. Salir \nIngrese una opción: ")
        opciones_ingresadas = []
        if menu == "1":
            opciones_ingresadas.append(1)
            user = Usuario()
            if validacion_usuario(user.usuario) == False:
                if validacion_contraseña (user.contraseña) == False:
                    user.registrar_usuario (user.usuario,user.contraseña)
                    user.agregar_usuario ("Usuarios.txt")
                else: 
                    print("La contraseña ya está en uso")
            else: 
                print("El usuario ya se encuentra ingresado")

        elif menu == "2":
            if len(opciones_ingresadas) == 0 :
                print("Ingrese sus datos: ")
                user = Usuario()
            opciones_ingresadas.append(2)
            if Usuario.iniciar_sesion (user.usuario, user.contraseña) is True:
                print("Sesion iniciada como: " + str(user.usuario))
                menuUsuarios(user)
            else:
                print("Usuario o Contraseña incorrectos")
                
        elif menu == "3":
            opciones_ingresadas.append(3)
            admin = Usuario()
            if admin.es_administrador (admin.usuario,admin.contraseña) == True:
                admin.registrar_usuario (admin.usuario,admin.contraseña)
                admin.actualizar_usuarios("Usuarios.txt")
                print ("Sesion iniciada como administrador")
                menuCanchas()
            else: 
                print ("Inicio de sesion incorrecto")
        elif menu == "4":
            break
        else: 
            print("Opcion no valida")

menuPrincipal()

### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO Y ABRIR EN SIMULTANEO LOS ARCHIVOS DE TEXTO 