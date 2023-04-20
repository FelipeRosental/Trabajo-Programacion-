from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL

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

def menu():
    while True:
        print("INICIO DE SESION")
        menu = input("1. Registrar usuario\n2. Iniciar sesión\n3. Cargar datos\n4. Hacer reserva \n5. Cancelar reserva \n6. Salir \nIngrese una opción: ")

        if menu == "1":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            registrar_usuario (usuario,contraseña)

        elif menu == "2":
            usuario = input ("Ingrese el Usuario: ")
            contraseña = input ("Ingrese la Contraseña: ")
            if iniciar_sesion (usuario,contraseña) is True:
                print("Inicio de Sesion correcto")
            else:
                print("Usuario o Contraseña incorrectos")
        
        elif menu == "3":
            club1.agregar_usuarios()
            
        elif menu == "4":
            if club1.mostrar_canchas() != 0:
                club1.agregar_reservas()
            else: 
                print("No hay mas canchas disponibles")
                 
        elif menu == "5":
            club1.eliminar_reservas()
     
        elif menu == "6":
            break
        
        else:
            print("Opcion no disponible")

menu()



