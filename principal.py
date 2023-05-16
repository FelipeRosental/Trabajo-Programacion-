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
        with open("Usuarios.txt", "a") as archivo:
            archivo.write (str(user)+"\n")
        self.lista_usuarios.append ("DNI:" + str(user.dni)) 
        
    def agregar_invitados (self):
        user = Usuario()
        with open("UsuariosInvitados.txt", "a") as archivo:
            archivo.write (str(user) + " Cantidad de ingresos: ")  
        
    def eliminar_usuarios(self):
        with open("Usuarios.txt", 'r') as archivo:
            dni = input("Ingrese el DNI del usuario a eliminar: ")
            while len(dni) !=8 :
                print("El dni debe tener 8 digitos") 
                dni = input("Ingrese el DNI del usuario a eliminar: ")
            lista_lineas = archivo.readlines()
            with open("Usuarios.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if dni not in linea:
                        archivo.write(linea)
            with open("Usuarios.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró el dni del usuario a eliminar")
                else: 
                    print("Datos eliminados correctamente")
                        
    def eliminar_invitados(self):
        with open("UsuariosInvitados.txt", 'r') as archivo:
            dni = input("Ingrese el DNI del usuario a eliminar: ")
            while len(dni) !=8:
                print("El dni debe tener 8 digitos") 
                dni = input("Ingrese el DNI del usuario a eliminar: ")
            lista_lineas = archivo.readlines()
            with open("UsuariosInvitados.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if dni not in linea:
                        archivo.write(linea)
            with open("UsuariosInvitados.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró el dni del usuario a eliminar")
                else: 
                    print("Datos eliminados correctamente")
            
    def cambiar_usuarios (self):
        with open("Usuarios.txt", 'r') as archivo:
            dni = input("Ingrese el DNI del usuario a cambiar: ")
            while len(dni) !=8 :
                print("El dni debe tener 8 digitos") 
                dni = input("Ingrese el DNI del usuario a cambiar: ")
            mail = input ("Ingrese el email del usuario a cambiar: ")
            while validacionEmail (mail) != True :
                mail = input ("Ingrese el email del usuario a cambiar: ")
            lista_lineas = archivo.readlines()
            with open("Usuarios.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if dni not in linea or mail not in linea:
                        archivo.write(linea)
                    elif dni in linea and mail in linea:
                        user = Usuario()
                        archivo.write (str(user)+"\n")
                    else: 
                        archivo.write(linea)
            with open("Usuarios.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró el dni o el email del usuario a cambiar")
                else: 
                    print("Datos cambiados correctamente") 
         
    def cambiar_invitados (self):
        with open("UsuariosInvitados.txt", 'r') as archivo:
            dni = input("Ingrese el DNI del usuario a cambiar: ")
            while len(dni) !=8 :
                print("El dni debe tener 8 digitos") 
                dni = input("Ingrese el DNI del usuario a cambiar: ")
            mail = input ("Ingrese el email del usuario a cambiar: ")
            while validacionEmail (mail) != True :
                mail = input ("Ingrese el email del usuario a cambiar: ")
            lista_lineas = archivo.readlines()
            with open("UsuariosInvitados.txt", 'w') as archivo:
                for linea in lista_lineas:
                    if dni not in linea or mail not in linea:
                        archivo.write(linea)
                    elif dni in linea and mail in linea:
                        user = Usuario()
                        archivo.write (str(user)+"\n")
                    else: 
                        archivo.write(linea)
            with open("UsuariosInvitados.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró el dni o el email del usuario a cambiar")
                else: 
                    print("Datos cambiados correctamente")                                   
                    
    # METODOS DE CANCHAS

    def agregar_canchas (self):
        cancha = Cancha()
        self.lista_canchas.append("CODIGO:" + str(cancha.codigo))
        self.total_canchas += 1 
        with open("Canchas.txt", "a") as archivo:
            archivo.write (str(cancha)+"\n")
    
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
            with open("Canchas.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró la cancha a eliminar")
                else: 
                    print("Datos eliminados correctamente")
            
    # METODOS DE RESERVAS
    
    def agregar_reservas (self):
        reserva = Reserva()
        with open("Canchas.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if str(reserva.horareserva) in linea:
                    with open("Reservas.txt", "a") as archivo:
                        archivo.write (str(reserva))
                        
        with open("Canchas.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if str(reserva.horareserva) not in linea:
                    with open("Canchas.txt", "a") as archivo:
                        archivo.write (linea)  
                else: 
                    with open("Canchas.txt", "a") as archivo:
                        archivo.write (linea + "(RESERVADA)")
            ### FUNCIONA MAL!!! (REVISAR)
                                    
        self.lista_reservas.append(reserva) 
        self.total_canchas -= 1  
        self.total_reservas += 1 
    
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
            with open("Reservas.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró la reserva a eliminar")
                else: 
                    print("Datos eliminados correctamente")
                            
club1 = Club("ITBA")


# COSAS PARA HACER:
#  1) HACER MAS PROLIJAS LAS RESERVAS (DEVOLVER MENSAJES CUANDO HAY ERRORES, HACER VALIDACIONES DE FECHAS SEGUN CORRESPONDA, ELIMINAR O AGREGAR LAS CANCHAS RESERVADAS)
#  2) ARREGLAR ERRORES 







    










