#######################################         LIBRERIAS      ################################################################# 

from random import *
from datetime import *
from string import *
import validaciones as val

#######################################         CLASES      ###############################################################

class Usuario ():
    def __init__(self):
        #VALIDACIONES
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ")
        while val.validacionStringUsuario(self.nombre, self.apellido) != True:
            self.nombre = input("Ingrese Nombre: ")
            self.apellido = input("Ingrese Apellido: ")
        ###    
        self.dni = input("Ingrese DNI: ")
        self.telefono = input("Ingrese Telefono: ")
        while val.validacionDNIyTelefono(self.dni, self.telefono) != True:
            self.dni = input("Ingrese DNI: ")
            self.telefono = input("Ingrese Telefono: ")
        ###
        self.edad = input("Ingrese Edad: ")    
        while val.validacionEdad(self.edad) != True:
            self.edad = input("Ingrese Edad: ")
        ###
        self.email = input("Ingrese Email: ")  
        while val.validacionEmail(self.email) != True:
           self.email = input("Ingrese Email: ")
        ###
        def __str__(self):
            return "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nDNI: " + str(self.dni) + "\nTelefono: " + str(self.telefono) + "\nEdad: " + str(self.edad) + "\nEmail: " + self.email
        def getDNI(self):
            return self.dni   
        def getNombre(self):
            return self.nombre
class Cancha (): 
    def __init__(self):
        #VALIDACIONES
        self.codigo = input ("Ingrese Codigo: ")
        while val.validacionCodigo (self.codigo) != True:
            self.codigo = input ("Ingrese Codigo: ")
        ###    
        self.techada = input ("Ingrese Techada: ")
        self.piso = input ("Ingrese Piso: ")
        self.estado = input ("Ingrese Estado: ")
        while val.validacionStringCancha (self.techada, self.piso, self.estado) != True:
            self.techada = input ("Ingrese Techada: ")
            self.piso = input ("Ingrese Piso: ")
            self.estado = input ("Ingrese Estado: ")
        
        def __str__(self):
            return "Codigo: " + str(self.codigo) + "\nTechada: " + self.techada + "\nPiso: " + self.piso + "\nEstado: " + self.estado
               
class Reserva ():
    def __init__(self):
        #VALIDACIONES
        self.fechareserva = input("Ingrese la fecha de la reserva: ")
        self.horareserva = input("Ingrese la hora de la reserva: ")
        while val.validacionFecha(self.fechareserva, self.horareserva):
            self.fechareserva = input("Ingrese la fecha de la reserva: ")
            self.horareserva = input("Ingrese la hora de la reserva: ")
        def __str__(self):
            return "Fecha de la reserva: " + str(self.fechareserva) + "\nHora de la reserva: " + str(self.horareserva)
        
class Club ():
    
    lista_usuarios = []
    lista_canchas = []
    lista_reservas = []
    
    def __init__(self,nombreclub):
        self.nombreclub = nombreclub
        
    def agregar_usuarios (self):
        user = Usuario()
        self.lista_usuarios.append(user)
    
    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append(cancha)
    
    def agregar_reservas (self):
        reserva = Reserva()
        self.lista_reservas.append(reserva)
    
    def mostrar_usuarios(self):
        print("USUARIOS:")
        for user in self.lista_usuarios:
           print(user)       
    def mostrar_canchas(self):
        print("CANCHAS:")
        for cancha in self.lista_canchas: 
            print(cancha)
    def mostrar_reservas(self):                             
        print("RESERVAS:")
        for reserva in self.lista_reservas:
            print(reserva)
      
            
################################## PRUEBA DE FUNCIONAMIENTO #################################################################

club1 = Club("Darling")
Club.agregar_usuarios(club1)
Club.mostrar_usuarios(club1)





    










