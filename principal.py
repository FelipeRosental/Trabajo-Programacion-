from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES

class Club ():

    lista_usuarios = []
    lista_canchas = []
    total_canchas = 10     
    lista_reservas = []
    total_reservas = 0

    def __init__(self,nombreclub):
        self.nombreclub = nombreclub
        
    # METODOS DE USUARIOS
    
    def agregar_usuarios (self):
        user = Usuario()
        self.lista_usuarios.append(user)
        with open("Usuarios.txt", "a") as archivo:
            archivo.write (str(user)+"\n")

    def mostrar_usuarios(self):         ### NO SE USA 
        print("USUARIOS:")
        for user in self.lista_usuarios: 
            print(user)         

    def eliminar_usuarios(self):
         with open("Usuarios.txt", 'r') as archivo:
            dni = input("Ingrese el DNI del usuario a eliminar: ")
            while len(dni) !=8:
               print("El dni debe tener 8 digitos") 
               dni = input("Ingrese el DNI del usuario a eliminar: ")
            lista_lineas = archivo.readlines()
            with open("Usuarios.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if dni not in linea:
                        archivo.write(linea)
                    
    # METODOS DE CANCHAS

    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append(cancha)
        self.total_canchas += 1 
        with open("Canchas.txt", "a") as archivo:
            archivo.write (str(cancha)+"\n")
    
    def mostrar_canchas(self):          ### NO SE USA
        print("CANCHAS:")
        for cancha in self.lista_canchas:           
            print(cancha)
        print("Canchas disponibles: " + str(self.total_canchas))
    
    def eliminar_canchas(self):
        with open("Canchas.txt", 'r') as archivo:
            codigo = input("Ingrese el codigo de la cancha a eliminar: ")
            while len(codigo) != 4:
                print("El codigo debe tener 4 digitos")
                codigo = input("Ingrese el codigo de la cancha a eliminar: ")
            lista_lineas = archivo.readlines()
            with open("Canchas.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if codigo not in linea:
                        archivo.write(linea)
        
    # METODOS DE RESERVAS
    
    def agregar_reservas (self):
        reserva = Reserva()
        self.lista_reservas.append(reserva)
        with open("Reservas.txt", "a") as archivo:
            archivo.write (str(reserva)+"\n")
        self.total_canchas -= 1  
        self.total_reservas += 1
        
    def mostrar_reservas(self):               ### NO SE USA                
        print("RESERVAS:")
        for reserva in self.lista_reservas:        
            print(reserva)
        print("Reservas totales: " + str(self.total_reservas))
    
    def eliminar_reservas(self):     
        with open("Reservas.txt", 'r') as archivo:
            codigo = input("Ingrese codigo de la reserva a eliminar: ")
            while len(codigo) != 4:
                print("El codigo debe tener 4 digitos")
                codigo = input("Ingrese codigo de la reserva a eliminar: ")
            lista_lineas = archivo.readlines()
            with open("Reservas.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if codigo not in linea:
                        archivo.write(linea)
                  
                            
club1 = Club("ITBA")




# COSAS PARA HACER:
#  1) PRIMER HORARIO DISPONIBLE PARA RESERVAR
#  2) VER CANCHAS DISPONIBLES (aca para no hacerla dificil, unicamente mostrar cantidad de canchas disponibles)
#  3) ARREGLAR LOS ERRORES







    










