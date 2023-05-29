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
            if 1 not in set(opciones_ingresadas):
                username = input("Ingrese su usuario: ")
                password = input("Ingrese su contraseña: ")
                if Usuario.iniciar_sesion (username, password) is True:
                    print("Sesion iniciada como: " + str(username))
                    user = Usuario.buscar_usuario ("Usuarios.txt" ,username, password)
                    menuUsuarios(user)
                else:
                    print("Usuario o Contraseña incorrectos")
            opciones_ingresadas.append(2)
                
        elif menu == "3":
            opciones_ingresadas.append(3)
            admin = Usuario() ### MEJORAR EL INGRESO DE LOS ADMINS...
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