from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL

def registrar_usuario (usuario,contraseña):
    with open("BaseDeDatos.txt", "a") as archivo:
        archivo.write ("USUARIO: " + usuario + "\n" + "CONTRASEÑA: " + str(contraseña))

def iniciar_sesion (usuario,contraseña):
    usuario = input ("Ingrese el Usuario: ")
    contraseña = input ("Ingrese la Contraseña: ")
    with open("BaseDeDatos.txt", 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            credenciales = linea.strip().split(':')
            if credenciales[0] == usuario and credenciales[1] == str(contraseña):
                return True
    return False

def menu():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrar usuario\n2. Iniciar sesión\n3. Salir\nIngrese una opción: ")

        if menu == "1":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            registrar_usuario (usuario,contraseña)

        elif menu == "2":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if iniciar_sesion (usuario,contraseña):
                print("Inicio de Sesion correcto")
            else:
                print("Usuario o Contraseña incorrectos")
                
        elif menu == "3":
            break

        else:
            print("Opcion no disponible")

menu()



