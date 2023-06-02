from random import *
from datetime import *
from string import *

from validaciones import *

class Usuario ():
    
    def __init__(self,dni=None, nombre=None, apellido=None, telefono=None, edad=None, email=None, usuario=None, contraseña=None):
        
        # ATRIBUTOS
        
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
        
        if usuario is None:
            self.usuario = input("Ingrese usuario: ")
        else:
            self.usuario = usuario
        
        if contraseña is None:
            self.contraseña = str(input("Ingrese contraseña: "))
        else:
            self.contraseña = contraseña
        
    
    # METODOS DE USUARIOS 
    
    @staticmethod
    def leer_usuarios(filename):  ### LEE LOS USUARIOS DE LA BASE DE DATOS Y LOS INSTANCIA EN PYTHON
        users = {}
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.strip().split(";")
                    user = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])            
                    users[user.dni] = user
            return users     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def buscar_usuario (usuarios, usuario, contraseña): ### BUSCA UN USUARIO EN el diccionario Y LO INSTANCIA
        for us in usuarios.values():
            if us.usuario == usuario and us.contraseña == contraseña:
                return us
            
    def agregar_usuario(self,filename): ### ya no sirve
        with open(filename, "a") as archivo:
            archivo.write(f"{self.dni};{self.nombre};{self.apellido};{self.telefono};{self.edad};{self.email};{self.usuario};{self.contraseña};\n")
        
    # IMPRESION
    
    def __str__(self):
        return (str(self.dni) +";"+ self.nombre +";" +self.apellido + ";" + self.telefono + ";" + str(self.edad) + ";" + self.email + ";" + str(self.usuario) +";"+ str(self.contraseña))
      
class Cancha (): 
    
    def __init__(self, codigo=None, techada=None, piso=None, estado=None, horario=None):
        
        # ATRIBUTOS
        
        if codigo is None:
            self.codigo = input ("Ingrese el codigo de cancha (numero de 4 digitos): ")
            while validacionCodigo (self.codigo) != True:
                print ("Codigo de cancha no valido (debe ser de 4 digitos).")
                self.codigo = input ("Ingrese el codigo de cancha: ")
        else: 
            self.codigo = codigo
        
        if techada is None: 
            self.techada = input ("Ingrese si la cancha es techada (si,no): ")
            while validacionTechada (self.techada) != True:
                print ("Respuesta no valida (debe ser si o no).")
                self.techada = input ("Ingrese si la cancha es techada: ")
        else: 
            self.techada = techada
        
        if piso is None:
            self.piso = input ("Ingrese el tipo de Piso (cesped, polvo de ladrillo, cemento): ")
            while validacionPiso (self.piso) != True:
                print ("Tipo de piso no valido.")
                self.piso = input ("Ingrese el tipo de Piso: ")
        else: 
            self.piso = piso    
           
        if estado is None: 
            self.estado = input ("Ingrese el Estado de la cancha (bueno, malo, intermedio): ")
            while validacionEstado (self.estado) != True:
                print ("Estado de la cancha no valido.")
                self.estado = input ("Ingrese el Estado de la cancha: ")
        else: 
            self.estado = estado
        
        if horario is None:  
            while True:
                self.horario = input ("Ingrese horario disponible (HH:MM): ")
                try:
                    self.horario = datetime.strptime(self.horario, "%H:%M").time()
                except ValueError:
                    print("Hora invalida, ingresarla con formato (HH:MM)")
                    continue
                else:
                    break   
        else: 
            self.horario = horario    
        
    # METODOS DE CANCHAS
        
    def agregar_cancha (self,filename): ### AGREGA UNA CANCHA A LA BASE DE DATOS
        with open(filename, "a") as archivo:
            archivo.write(f"{self.codigo};{self.techada};{self.piso};{self.estado};{self.horario};\n")
    
    def buscar_cancha (filename, codigo, horario): ### BUSCA UNA CANCHA EN LA BASE DE DATOS Y LA INSTANCIA
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    if datos [0] == codigo and datos[4] == horario:
                        cancha = Cancha(datos[0], datos[1], datos[2], datos[3], datos[4]) 
            return cancha
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    @staticmethod
    def leer_canchas(filename):  ### LEE LA BASE DE DATOS E INSTANCIA CANCHAS EN PYTHON
        canchas = {}
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    cancha = Cancha(datos[0], datos[1], datos[2], datos[3], datos[4])            
                    canchas[cancha.codigo] = f"{cancha.techada};{cancha.piso};{cancha.estado};{cancha.horario}"
            return canchas     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False                
    
    # IMPRESION
        
    def __str__(self):
        return ("Codigo: " + str(self.codigo) + " Techada: " + self.techada + " Piso: " + self.piso + " Estado: " + self.estado + " Horario: " + str(self.horario))
               
class Reserva ():
    
    lista_reservas = {}  
    
    def __init__(self, codigo=None, fechareserva=None, horareserva=None):
        
        # ATRIBUTOS
        
        if codigo is None: 
            self.codigo = randint(1000,9999)
        else: 
            self.codigo = codigo
        
        if fechareserva is None: 
            while True: 
                self.fechareserva = input("ingrese la fecha (dd-mm-yyyy): ")
                try:
                    self.fechareserva = datetime.strptime(self.fechareserva, "%d-%m-%Y").date()
                except ValueError:
                    print("Fecha invalida, ingresarla con formato (dd-mm-yyyy)")
                    continue
                else: 
                    break    
        else: 
            self.fechareserva = fechareserva
        
        if horareserva is None:
            while True:
                self.horareserva = input("ingrese hora (HH:MM): ")
                try:
                    self.horareserva = datetime.strptime(self.horareserva, "%H:%M").time()
                except ValueError:
                    print("Hora invalida, ingresarla con formato (HH:MM)")
                    continue
                else:
                    break       
        else: 
            self.horareserva = horareserva
        
        self.lista_reservas[self.codigo] = str(self.fechareserva) + ";" + str(self.horareserva)
    
    # METODOS DE RESERVAS
    
    @staticmethod
    def leer_reservas(filename):  ### LEE LA BASE DE DATOS E INSTANCIA RESERVAS EN PYTHON
        reservas = {}
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    user = Reserva(datos[0], datos[1], datos[2])
                    reservas[user.codigo] = str(user.fechareserva) + ";" + str(user.horareserva)
            return reservas    
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def agregar_reservas (self, filename):  ### ESCRIBE RESERVAS EN LA BASE DE DATOS
        with open(filename, "a") as archivo:
            archivo.write (f"{self.codigo};{self.fechareserva};{self.horareserva};\n")
    
    # IMPRESION
        
    def __str__(self):
        return ("Codigo de Reserva: " + str(self.codigo) + " Fecha de la reserva: " + str(self.fechareserva) + " Hora de la reserva: " + str(self.horareserva))


    




