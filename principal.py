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
       
    def mostrar_usuarios(self):
        print("USUARIOS:")
        for user in self.lista_usuarios: 
            print(str(user))   ### FUNCIONA MAL!!!  
    
    def eliminar_usuarios(self):
        user = Usuario()
        self.lista_usuarios.remove(user)
        
    # METODOS DE CANCHAS
    
    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append(cancha)   ### FUNCIONA MAL!!!
    
    def mostrar_canchas(self):
        print("CANCHAS:")
        for cancha in self.lista_canchas: 
            print(cancha)
    
    def eliminar_canchas(self):
        cancha = Cancha()
        self.lista_canchas.remove(cancha)
        
    # METODOS DE RESERVAS
    
    def agregar_reservas (self):
        reserva = Reserva()
        self.lista_reservas.append(reserva)  ### FUNCIONA MAL!!!
        
    def mostrar_reservas(self):                             
        print("RESERVAS:")
        for reserva in self.lista_reservas:
            print(reserva)
    
    def eliminar_reservas(self):
        reserva = Reserva()
        self.lista_reservas.remove(reserva)
                  
################################## PRUEBA DE FUNCIONAMIENTO #################################################################

club1 = Club("Darling")
club1.agregar_usuarios()
club1.mostrar_usuarios()


# COSAS PARA HACER:
#  1) PRIMER HORARIO DISPONIBLE PARA RESERVAR
#  2) VER CANCHAS DISPONIBLES
#  3) ARREGLAR LOS ERROES

# Detalles esteticos
#  1) Cada vez que una validacion falla, mandar mensaje explicando el porque.




    










