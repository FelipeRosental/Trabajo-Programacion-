#######################################         LIBRERIAS      ################################################################# 

from random import *
from tkinter import * 
from datetime import *
from string import *

################################ VALIDACIONES DEL PROGRAMA #################################################################

def validacionDNIyTelefono ():
    while len(usuario.dni)==8:
        if usuario.dni.isdigit() == False or usuario.telefono.isdigit() == False :
            return False
        else:
            return True
    return False
def validacionEdad ():
    if usuario.edad.isdigit() == False:
        return False
    else:  
        return True  
def validacionCodigo ():
    if cancha.codigo.isdigit() == False:
        return False
    else:
        return True
def validacionFecha ():
    if reserva.fechareserva != datetime.date or reserva.horareserva != datetime.time:
        return False
    else:
        return True
def validacionStringUsuario ():
    if usuario.nombre.isalpha() == False or usuario.apellido.isalpha() == False:
        return False
    else:
        return True
def validacionStringCancha ():
    if cancha.techada.isalpha() == False or cancha.piso.isalpha() == False or cancha.estado.isalpha() == False:
        return False
    else:
        return True
def validacionEmail ():
    if "@" not in usuario.email:
        return False
    else:
        return True

#######################################         CLASES      ###############################################################

class usuario ():
    lista_usuarios = []
    def __init__(self):
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ")
        self.dni = input("Ingrese DNI: ")
        self.edad = input("Ingrese Edad: ")
        self.email = input("Ingrese Email: ")
        self.telefono = input("Ingrese Telefono: ")
        if validacionDNIyTelefono == True and validacionStringUsuario == True and validacionEmail == True and validacionEdad == True:
            usuario.lista_usuarios.append([self.nombre, self.apellido, self.dni, self.edad, self.email, self.telefono])
        else: 
            print("Los datos no son válidos")
    def eliminar_usuario (posicion):
        usuario.lista_usuarios.pop(posicion)
    def mostrar_usuarios():
        print("USUARIOS: " + str(usuario.lista_usuarios))

class cancha (): 
    lista_canchas = []
    def __init__(self):
        self.codigo = input ("Ingrese Codigo: ")
        self.techada = input ("Ingrese Techada: ")
        self.estado = input ("Ingrese Estado: ")
        self.piso = input ("Ingrese Piso: ")
        if validacionCodigo == True and validacionStringCancha == True:
            cancha.lista_canchas.append([self.codigo, self.techada, self.estado, self.piso])
        else: 
            print("Los datos no son válidos")
    def eliminar_cancha(posicion):
        cancha.lista_canchas.pop(posicion)  
    def mostrar_canchas():
        print("CANCHAS: " + str(cancha.lista_canchas))
       
class reserva (usuario, cancha):
    lista_reservas = []
    def __init__(self, fechareserva, horareserva):
        self.fechareserva = fechareserva
        self.horareserva = horareserva
        reserva.lista_reservas.append ([self.fechareserva, self.horareserva, usuario.dni, cancha.codigo])
    def mostrar_reservas():
        print("RESERVAS: " + str(reserva.lista_reservas))

################################## PRUEBA DE FUNCIONAMIENTO #################################################################

usuario1= usuario ()
cancha1 = cancha ()

"MOSTRAR RESERVAS FUNCIONA MAL!"


    










