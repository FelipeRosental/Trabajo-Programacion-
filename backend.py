#######################################         LIBRERIAS      ################################################################# 

from random import *
from datetime import *
from string import *

################################ VALIDACIONES DEL PROGRAMA #################################################################

def validacionDNIyTelefono (dni, telefono):
    while len(dni)==8:
        if dni.isdigit() == False or telefono.isdigit() == False :
            return False
        else:
            return True
    return False
def validacionEdad (edad):
    if edad.isdigit() == False:
        return False
    else:  
        return True  
def validacionCodigo (codigo):
    while len(codigo)==4:
        if codigo.isdigit() == False:
            return False
        else:
            return True
    return False
def validacionFecha (fechareserva, horareserva):
    if fechareserva != datetime.date or horareserva != datetime.time:
        return False
    else:
        return True
def validacionStringUsuario (nombre, apellido):
    if nombre.isalpha() == False or apellido.isalpha() == False:
        return False
    else:
        return True
def validacionStringCancha (techada, piso, estado):
    if techada.isalpha() == False or piso.isalpha() == False or estado.isalpha() == False:
        return False
    else:
        return True
def validacionEmail (email):
    if "@" not in email:
        return False
    else:
        return True

#######################################         CLASES      ###############################################################

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
               
class Reserva ():
    def __init__(self):
        #VALIDACIONES
        self.fechareserva = input("Ingrese la fecha de la reserva: ")
        self.horareserva = input("Ingrese la hora de la reserva: ")
        while validacionFecha(self.fechareserva, self.horareserva):
            self.fechareserva = input("Ingrese la fecha de la reserva: ")
            self.horareserva = input("Ingrese la hora de la reserva: ")
        
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
        print("USUARIOS: " + str(self.lista_usuarios))
    def mostrar_canchas(self):
        print("CANCHAS: " + str(self.lista_canchas))
    def mostrar_reservas(self):
        print("RESERVAS: " + str(self.lista_reservas))
            
        
################################## PRUEBA DE FUNCIONAMIENTO #################################################################

usuario1 = Usuario()
cancha1 = Cancha()
club1= Club("Darling")
club1.agregar_usuarios()
club1.agregar_canchas()
club1.mostrar_usuarios()
club1.mostrar_canchas()




    










