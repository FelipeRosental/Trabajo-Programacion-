from random import *
from datetime import *
from string import *

from validaciones import *

class Usuario ():
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ") 
        while validacionStringUsuario(self.nombre, self.apellido) != True:
            self.nombre = input("Ingrese Nombre: ")
            self.apellido = input("Ingrese Apellido: ")
        
        self.dni = input("Ingrese DNI: ")
        self.telefono = input("Ingrese Telefono: ")
        while validacionDNIyTelefono(self.dni, self.telefono) != True:
            self.dni = input("Ingrese DNI: ")
            self.telefono = input("Ingrese Telefono: ")
        
        self.edad = input("Ingrese Edad: ")    
        while validacionEdad(self.edad) != True:
            self.edad = input("Ingrese Edad: ")
        
        self.email = input("Ingrese Email: ")  
        while validacionEmail(self.email) != True:
           self.email = input("Ingrese Email: ")
        
        # IMPRESION
        
    def __str__(self):
        return (self.nombre, self.apellido, str(self.dni), str(self.telefono), str(self.edad), self.email)
      
class Cancha (): 
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.codigo = input ("Ingrese el codigo de cancha: ")
        while validacionCodigo (self.codigo) != True:
            self.codigo = input ("Ingrese el codigo de cancha: ")
        
        self.techada = input ("Ingrese si la cancha es techada: ")
        self.piso = input ("Ingrese el tipo de Piso: ")
        self.estado = input ("Ingrese el Estado de la cancha: ")
        while validacionStringCancha (self.techada, self.piso, self.estado) != True:
            self.techada = input ("Ingrese si la cancha es techada: ")
            self.piso = input ("Ingrese el tipo de Piso: ")
            self.estado = input ("Ingrese el Estado de la cancha: ")
            
        # IMPRESION
        
        def __str__(self):
            return ("Codigo: " + str(self.codigo) + "\nTechada: " + self.techada + "\nPiso: " + self.piso + "\nEstado: " + self.estado)
               
class Reserva ():
    
    def __init__(self):
        
        # VALIDACIONES
        #mejorar validacion de la fecha
        self.fechareserva = datetime.date(input("ingrese año"),input("ingrese mes"),input("ingrese dia"))
        self.horareserva = datetime.time(input("ingrese hora"), input("ingrese minuto aprox"))
        while validacionFecha(self.fechareserva, self.horareserva):
            self.fechareserva = datetime.date(input("ingrese año"),input("ingrese mes"),input("ingrese dia"))
            self.horareserva = datetime.time(input("ingrese hora"), input("ingrese minuto aprox"))
            
        # IMPRESION
        
        def __str__(self):
            return ("Fecha de la reserva: " + str(self.fechareserva) + "\nHora de la reserva: " + str(self.horareserva))