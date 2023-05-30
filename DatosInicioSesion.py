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
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Salir \nIngrese una opción: ")
        opciones_ingresadas = []
        if menu == "1":
            opciones_ingresadas.append(1)
            user = Usuario()
            if Usuario.es_administrador(user.usuario) == True:
                if validacion_DNI_repetido(user.dni) == False:
                    if validacion_contraseña (user.contraseña)== False:    
                        user.agregar_usuario ("Usuarios.txt")
                    else: 
                        print("La contraseña ya está en uso")
                else: 
                    print ("El DNI ya se encuentra registrado")
            else:  
                if validacion_usuario(user.usuario) == False: 
                    if validacion_DNI_repetido(user.dni) == False:
                        user.agregar_usuario ("Usuarios.txt")
                    else: 
                        print ("El DNI ya se encuentra registrado")
                else: 
                    print("El usuario ya se encuentra ingresado")
                    
        elif menu == "2":
            if 1 not in set(opciones_ingresadas): 
                username = input("Ingrese su usuario: ")
                password = input("Ingrese su contraseña: ")
                if Usuario.es_administrador(username) is True:
                    if Usuario.iniciar_sesion (username, password) is True:
                        print("Sesion iniciada como administrador")
                        menuCanchas()
                    else:
                        print("Usuario o Contraseña incorrectos") 
                else: 
                    if Usuario.iniciar_sesion (username, password) is True:
                        print("Sesion iniciada como: " + str(username))
                        user = Usuario.buscar_usuario ("Usuarios.txt" ,username, password)
                        menuUsuarios(user)
                    else:
                        print("Usuario o Contraseña incorrectos")
                           
                
        elif menu == "3":
            break
        else: 
            print("Opcion no valida")

menuPrincipal()

### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO Y ABRIR EN SIMULTANEO LOS ARCHIVOS DE TEXTO 