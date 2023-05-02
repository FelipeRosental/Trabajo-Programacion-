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

def iniciar_sesion (usuario,contraseña):
    with open("InicioSesion.txt", 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            credenciales = linea.strip().split(':')
            if credenciales[0] == usuario and credenciales[1] == str(contraseña):
                return True
    return False

def menu3():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrar usuario\n2. Iniciar sesión\n3. Salir \nIngrese una opción: ")

        if menu == "1":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            registrar_usuario (usuario,contraseña)

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
            break
        else: 
            print("Opcion no valida")

menu3()