from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from DatosUsuario import * ### DATOS DE USUARIOS Y RESERVAS
from DatosCanchas import * ### DATOS DE CANCHAS

def iniciar_sesion (usuario,contraseña):
    with open("InicioSesion.txt", 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            credenciales = linea.strip().split(':')
            if credenciales[0] == usuario and credenciales[1] == str(contraseña):
                return True
    return False
   
def menuPrincipal():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Cambiar contraseña \n4. Ingresar como administrador \n5. Salir \nIngrese una opción: ")

        if menu == "1":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if validacion_usuario(usuario) == False:
                if validacion_contraseña (contraseña) == False:
                    Usuario.registrar_usuario (usuario,contraseña)
                else: 
                    print("La contraseña ya está en uso")
            else: 
                print("El usuario ya se encuentra ingresado")

        elif menu == "2":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if iniciar_sesion (usuario,contraseña) is True:
                print("Inicio de Sesion correcto")
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Inicio de sesion correcto " + "\n")
                menuUsuarios()
            else:
                print("Usuario o Contraseña incorrectos")
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Inicio de sesion incorrecto " + "\n")
        elif menu == "3":
            usuario = input("Ingrese su usuario: ")
            contraseña_nueva = input("Ingrese se nueva contraseña: ")
            if validacion_usuario(usuario) == True:
                if validacion_contraseña(contraseña_nueva) == False:
                    Usuario.cambiar_contraseña (usuario, contraseña_nueva)
                else: 
                    print("La contraseña ingresada es igual a la anterior o ya está en uso")
            else: 
                print("No se encontró el usuario ingresado")
        elif menu == "4":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if Usuario.es_administrador (usuario,contraseña) == True:
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Sesion iniciada como administrador " + "\n")
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