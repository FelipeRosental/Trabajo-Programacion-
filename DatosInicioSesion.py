from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL
from DatosUsuario import * ### DATOS DE USUARIOS Y RESERVAS

def registrar_usuario (usuario,contraseña):
    with open("InicioSesion.txt", "a") as archivo:
        archivo.write (f"{usuario}:{str(contraseña)}\n")
            
def validacion_usuario (usuario):
    with open("InicioSesion.txt", "r") as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        credenciales = linea.strip().split(':')
        if credenciales[0] == usuario:
            return True
    return False

def iniciar_sesion (usuario,contraseña):
    with open("InicioSesion.txt", 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            credenciales = linea.strip().split(':')
            if credenciales[0] == usuario and credenciales[1] == str(contraseña):
                return True
    return False

def cambiar_contraseña(usuario, contraseña_nueva):
    with open("InicioSesion.txt", 'r') as archivo:
        lineas = archivo.readlines()
    with open("InicioSesion.txt", 'w') as archivo:                    
        for linea in lineas:
            if usuario not in linea:
                archivo.write(str(linea))
            else:
                archivo.write(usuario + ":" + str(contraseña_nueva) + "\n")

def menu3():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrar usuario \n2. Iniciar sesión \n3. Cambiar contraseña \n4. Ingresar como invitado \n5. Salir \nIngrese una opción: ")

        if menu == "1":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if validacion_usuario(usuario) == False:
                registrar_usuario (usuario,contraseña)
            else: 
                print("El usuario ya se encuentra ingresado")

        elif menu == "2":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if iniciar_sesion (usuario,contraseña) is True:
                print("Inicio de Sesion correcto")
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Inicio de sesion correcto " + "\n")
                menu1()
            else:
                print("Usuario o Contraseña incorrectos")
                with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Inicio de sesion incorrecto " + "\n")
        elif menu == "3":
            usuario = input("Ingrese su usuario: ")
            contraseña_nueva = input("Ingrese se nueva contraseña: ")
            cambiar_contraseña (usuario, contraseña_nueva)
            
        elif menu == "4":
            with open("InicioSesion.txt", "a") as archivo:
                    archivo.write ("Sesion iniciada como invitado " + "\n")
            menu4()
        elif menu == "5":
            break
        else: 
            print("Opcion no valida")

menu3()