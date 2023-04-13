from random import *
from datetime import *
from string import *
from validaciones import *

class Usuario ():
    def __init__(self):
        #VALIDACIONES
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ")
        while validacionStringUsuario(self.nombre, self.apellido) != True:
            self.nombre = input("Ingrese Nombre: ")
            self.apellido = input("Ingrese Apellido: ")
        ###    
        self.dni = input("Ingrese DNI: ")
        self.telefono = input("Ingrese Telefono: ")
        while validacionDNIyTelefono(self.dni, self.telefono) != True:
            self.dni = input("Ingrese DNI: ")
            self.telefono = input("Ingrese Telefono: ")
        ###
        self.edad = input("Ingrese Edad: ")    
        while validacionEdad(self.edad) != True:
            self.edad = input("Ingrese Edad: ")
        ###
        self.email = input("Ingrese Email: ")  
        while validacionEmail(self.email) != True:
           self.email = input("Ingrese Email: ")
        #IMPRESION
        def __str__(self):
            return ("Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nDNI: " + str(self.dni) + "\nTelefono: " + str(self.telefono) + "\nEdad: " + str(self.edad) + "\nEmail: " + self.email)
      
class Cancha (): 
    def __init__(self):
        #VALIDACIONES
        self.codigo = input ("Ingrese Codigo: ")
        while validacionCodigo (self.codigo) != True:
            self.codigo = input ("Ingrese Codigo: ")
        ###
        self.techada = input ("Ingrese Techada: ")
        self.piso = input ("Ingrese Piso: ")
        self.estado = input ("Ingrese Estado: ")
        while validacionStringCancha (self.techada, self.piso, self.estado) != True:
            self.techada = input ("Ingrese Techada: ")
            self.piso = input ("Ingrese Piso: ")
            self.estado = input ("Ingrese Estado: ")
        #IMPRESION
        def __str__(self):
            return ("Codigo: " + str(self.codigo) + "\nTechada: " + self.techada + "\nPiso: " + self.piso + "\nEstado: " + self.estado)
               
class Reserva ():
    def __init__(self):
        #VALIDACIONES
        self.fechareserva = input("Ingrese la fecha de la reserva: ")
        self.horareserva = input("Ingrese la hora de la reserva: ")
        while validacionFecha(self.fechareserva, self.horareserva):
            self.fechareserva = input("Ingrese la fecha de la reserva: ")
            self.horareserva = input("Ingrese la hora de la reserva: ")
        #IMPRESION
        def __str__(self):
            return ("Fecha de la reserva: " + str(self.fechareserva) + "\nHora de la reserva: " + str(self.horareserva))