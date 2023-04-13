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
    lista_reservas = []
    # CONSTRUCTOR
    def __init__(self,nombreclub):
        self.nombreclub = nombreclub
    # METODOS DE USUARIOS
    def agregar_usuarios (self):
        user = Usuario()
        self.lista_usuarios.append(user)
    ###    
    def mostrar_usuarios(self):
        print("USUARIOS:")
        for user in self.lista_usuarios:
           print(user)  
    # METODOS DE CANCHAS
    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append(cancha)
    ###
    def mostrar_canchas(self):
        print("CANCHAS:")
        for cancha in self.lista_canchas: 
            print(cancha)
    # METODOS DE RESERVAS
    def agregar_reservas (self):
        reserva = Reserva()
        self.lista_reservas.append(reserva)
    ###        
    def mostrar_reservas(self):                             
        print("RESERVAS:")
        for reserva in self.lista_reservas:
            print(reserva)
                  
################################## PRUEBA DE FUNCIONAMIENTO #################################################################

club1 = Club("Darling")
club1.agregar_usuarios()
club1.mostrar_usuarios()


#AGREGAR, BORRAR Y MODIFICAR RESERVAS, USUARIOS, CANCHAS
#PRIMER HORARIO DISPONIBLE PARA RESERVAR
#VER CANCHAS DISPONIBLES
#



    










