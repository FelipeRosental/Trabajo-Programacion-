#######################################         LIBRERIAS      ################################################################# 
from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
#######################################      CLASE PRINCIPAL (CLUB)   ##########################################################
        
class Club ():
    
    # LISTAS PRINCIPALES

    lista_usuarios = []
    lista_canchas = []
    total_canchas = 10     
    lista_reservas = []
    total_reservas = 0

    # CONSTRUCTOR

    def __init__(self,nombreclub):
        self.nombreclub = nombreclub
        
    # METODOS DE USUARIOS
    
    def agregar_usuarios (self):
        user = Usuario()
        self.lista_usuarios.append(user)
        with open("BaseDeDatos.txt", "a") as archivo:
                archivo.write (str(user)+"\n\n")

    def mostrar_usuarios(self):
        print("USUARIOS:")
        for user in self.lista_usuarios: 
            print(user)    

    def eliminar_usuarios(self):
        user = Usuario()
        self.lista_usuarios.remove(user) ### NO FUNCIONA

    # METODOS DE CANCHAS

    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append(cancha)
        self.total_canchas += 1 
    
    def mostrar_canchas(self):
        print("CANCHAS:")
        for cancha in self.lista_canchas: 
            print(cancha)
        print("Canchas disponibles: " + str(self.total_canchas))
    
    def eliminar_canchas(self):
        codigo = input ("Ingrese el codigo: ")
        if Cancha.codigo == codigo:
            self.lista_canchas.remove(Cancha()) 
            self.total_canchas -= 1
        print ("Canchas disponibles: " + str(self.total_canchas)) ### NO FUNCIONA
        
    # METODOS DE RESERVAS
    
    def agregar_reservas (self):
        reserva = Reserva()
        self.lista_reservas.append(reserva)
        with open("BaseDeDatos.txt", "a") as archivo:
                archivo.write (str(reserva)+"\n\n")
        self.total_canchas -= 1  
        self.total_reservas += 1
        
    def mostrar_reservas(self):                             
        print("RESERVAS:")
        for reserva in self.lista_reservas:
            print(reserva)
        print("Reservas totales: " + str(self.total_reservas))
    
    def eliminar_reservas(self):
        reserva = Reserva()
        self.lista_reservas.remove(reserva) 
        self.total_canchas += 1 
        self.total_reservas -= 1        ### NO FUNCIONA
                  
################################## PRUEBA DE FUNCIONAMIENTO #################################################################

club1 = Club("ITBA")

# COSAS PARA HACER:
#  1) PRIMER HORARIO DISPONIBLE PARA RESERVAR
#  2) VER CANCHAS DISPONIBLES
#  3) ARREGLAR LOS ERROES







    










