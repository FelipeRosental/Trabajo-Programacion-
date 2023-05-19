from random import *
from datetime import *
from string import *

from validaciones import *


# cada vez que creas un usuario, lo agregas a la lista de usuarios

class Usuario ():

    set_usuarios = set()
    
    def __init__(self, dni=None, nombre=None, apellido=None, telefono=None, edad=None, email=None):
        
        # VALIDACIONES
        if dni is None:
            self.dni = input("Ingrese DNI: ")
            while validacionDNI(self.dni) != True:
                print("DNI no valido.")
                self.dni = input("Ingrese DNI: ")
        else:
            self.dni = dni
            
        if nombre is None:
            self.nombre = input("Ingrese Nombre: ")
            while validacionNombre(self.nombre) != True:
                print ("Nombre no valido.")
                self.nombre = input("Ingrese Nombre: ")
        else: 
            self.nombre = nombre
        
        if apellido is None:
            self.apellido = input("Ingrese Apellido: ") 
            while validacionApellido(self.apellido) != True:
                print ("Apellido no valido.")
                self.apellido = input("Ingrese Apellido: ")
        else: 
            self.apellido = apellido    
        
        if telefono is None:
            self.telefono = input("Ingrese Telefono: ")
            while validacionTelefono(self.telefono) != True:
                print("Telefono no valido.")
                self.telefono = input("Ingrese Telefono: ")
        else: 
            self.telefono = telefono
        
        if edad is None:
            self.edad = input("Ingrese Edad: ")    
            while validacionEdad(self.edad) != True:
                print ("Edad no valida.")
                self.edad = input("Ingrese Edad: ")
        else: 
            self.edad = edad
            
        if email is None:    
            self.email = input("Ingrese Email: ")  
            while validacionEmail(self.email) != True:
                print ("Email no valido.")
                self.email = input("Ingrese Email: ")
        else: 
            self.email = email
        
        Usuario.set_usuarios.add(self)
    
    # METODOS DE USUARIOS 
    
    def read_usuarios(self,filename):
        users = set()
        try:
            with open(filename) as f:
                for line in f:
                    datos = line.split(";")
                    user = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])            
                    users.add(user)
            return users     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def agregar_usuario(self,filename):
        with open(filename, "a") as archivo:
            archivo.write(f"{self.dni};{self.nombre};{self.apellido};{self.telefono};{self.edad};{self.email}\n")
            
    def actualizar_archivo(self,filename):
        guardados = self.read_usuarios(filename)
        a_guardar = Usuario.set_usuarios - guardados 
        for user in a_guardar:
            user.agregar_usuario(filename)

    # TERMINAR  ( FUNCIONA MAL :( )
    
    def cambiar_usuarios (self):   ### CAMBIAR ESTO!!!
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
                        archivo.write (user.__str__()+"\n")
                    else: 
                        archivo.write(linea)
            with open("Usuarios.txt", 'r') as archivo:
                lista_lineasnueva = archivo.readlines()    
                if lista_lineasnueva == lista_lineas:
                    print("No se encontró el dni o el email del usuario a cambiar")
                else: 
                    print("Datos cambiados correctamente") 
        if self.set_usuarios.get (dni,None) != None:  
            self.set_usuarios [dni] = user
        
    def eliminar_usuarios(self):   ### CAMBIAR ESTO!!!
        
        dni = input("Ingrese el DNI del usuario a eliminar: ")
        while len(dni) !=8 :
            print("El dni debe tener 8 digitos") 
            dni = str(input("Ingrese el DNI del usuario a eliminar: "))
        
        if self.set_usuarios.get (dni,None) != None:  
            del self.set_usuarios [dni] 
            
        with open("Usuarios.txt", 'r') as archivo:
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
        
    # IMPRESION
    
    def __str__(self):
        return ("Nombre: " + self.nombre + " Apellido: " +  self.apellido + " Telefono: " + self.telefono + " Edad: " + str(self.edad) + " Mail: " + self.email + " Dni: "+ str(self.dni))
      
class Cancha (): 
    
    lista_canchas = {}
    total_canchas = 10    
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.codigo = input ("Ingrese el codigo de cancha (numero de 4 digitos): ")
        while validacionCodigo (self.codigo) != True:
            print ("Codigo de cancha no valido (debe ser de 4 digitos).")
            self.codigo = input ("Ingrese el codigo de cancha: ")
        
        self.techada = input ("Ingrese si la cancha es techada (si,no): ")
        while validacionTechada (self.techada) != True:
            print ("Respuesta no valida (debe ser si o no).")
            self.techada = input ("Ingrese si la cancha es techada: ")
            
        self.piso = input ("Ingrese el tipo de Piso (cesped, polvo de ladrillo, cemento): ")
        while validacionPiso (self.piso) != True:
            print ("Tipo de piso no valido.")
            self.piso = input ("Ingrese el tipo de Piso: ")
            
        self.estado = input ("Ingrese el Estado de la cancha (bueno, malo, intermedio): ")
        while validacionEstado (self.estado) != True:
            print ("Estado de la cancha no valido.")
            self.estado = input ("Ingrese el Estado de la cancha: ")
            
        while True:
            self.horario = input ("Ingrese horario disponible (HH:MM): ")
            try:
                self.horario = datetime.strptime(self.horario, "%H:%M").time()
            except ValueError:
                print("Hora invalida, ingresarla con formato (HH:MM)")
                continue
            else:
                break   
        
    # METODOS DE CANCHAS

    def agregar_canchas (self):
        self.lista_canchas.append("CODIGO:" + str(self.codigo))
        self.total_canchas += 1 
        with open("Canchas.txt", "a") as archivo:
            archivo.write (str(self.__str__)+"\n")
    
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
        
        # IMPRESION
        
    def __str__(self):
        return ("Codigo: " + str(self.codigo) + " Techada: " + self.techada + " Piso: " + self.piso + " Estado: " + self.estado + " Horario: " + str(self.horario))
               
class Reserva ():
    
    lista_reservas = []
    total_reservas = 0 
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.codreserva = randint(1000,9999)
        print("Su codigo de reserva es: ", str(self.codreserva))
        
        while True: 
            self.fechareserva = input("ingrese la fecha (dd-mm-yyyy): ")
            try:
                self.fechareserva = datetime.strptime(self.fechareserva, "%d-%m-%Y").date()
            except ValueError:
                print("Fecha invalida, ingresarla con formato (dd-mm-yyyy)")
                continue
            else: 
                break    
        
        while True:
            self.horareserva = input("ingrese hora (HH:MM): ")
            try:
                self.horareserva = datetime.strptime(self.horareserva, "%H:%M").time()
            except ValueError:
                print("Hora invalida, ingresarla con formato (HH:MM)")
                continue
            else:
                break       
        
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
        
    # IMPRESION
        
    def __str__(self):
        return ("Codigo de Reserva: " + str(self.codreserva) + " Fecha de la reserva: " + str(self.fechareserva) + " Hora de la reserva: " + str(self.horareserva))


Usuario.read_usuarios(Usuario,"Usuarios.txt")
usuario1 = Usuario() 

""" Usuario.agregar_usuario(user,"Usuarios.txt")    """

Usuario.actualizar_archivo(usuario1,"Usuarios.txt") 


    




