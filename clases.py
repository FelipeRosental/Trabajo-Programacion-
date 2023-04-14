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
            print ("Error en los datos ingresados, por favor pruebe nuevamente")
            self.nombre = input("Ingrese Nombre: ")
            self.apellido = input("Ingrese Apellido: ")
        
        self.dni = input("Ingrese DNI: ")
        self.telefono = input("Ingrese Telefono: ")
        while validacionDNIyTelefono(self.dni, self.telefono) != True:
            print ("Error en los datos ingresados, por favor pruebe nuevamente")
            self.dni = input("Ingrese DNI: ")
            self.telefono = input("Ingrese Telefono: ")
        
        self.edad = input("Ingrese Edad: ")    
        while validacionEdad(self.edad) != True:
            print ("Error en los datos ingresados, por favor pruebe nuevamente")
            self.edad = input("Ingrese Edad: ")
        
        self.email = input("Ingrese Email: ")  
        while validacionEmail(self.email) != True:
           print ("Error en los datos ingresados, por favor pruebe nuevamente")
           self.email = input("Ingrese Email: ")
        
        # IMPRESION
        
    def __str__(self):
        return ("Nombre: " + str(self.nombre) + "\nApellido: " + str(self.apellido) + "\nDNI: " + str(self.dni) + "\nTelefono: " + str(self.telefono) + "\nEdad: " + str(self.edad) + "\nEmail: " + str(self.email))
      
class Cancha (): 
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.codigo = input ("Ingrese el codigo de cancha: ")
        while validacionCodigo (self.codigo) != True:
            print ("Error en los datos ingresados, por favor pruebe nuevamente")
            self.codigo = input ("Ingrese el codigo de cancha: ")
        
        self.techada = input ("Ingrese si la cancha es techada: ")
        self.piso = input ("Ingrese el tipo de Piso: ")
        self.estado = input ("Ingrese el Estado de la cancha: ")
        while validacionStringCancha (self.techada, self.piso, self.estado) != True:
            print ("Error en los datos ingresados, por favor pruebe nuevamente")
            self.techada = input ("Ingrese si la cancha es techada: ")
            self.piso = input ("Ingrese el tipo de Piso: ")
            self.estado = input ("Ingrese el Estado de la cancha: ")
            
        # IMPRESION
        
    def __str__(self):
        return ("Codigo: " + str(self.codigo) + "\nTechada: " + self.techada + "\nPiso: " + self.piso + "\nEstado: " + self.estado)
               
class Reserva ():
    
    def __init__(self):
        
        # VALIDACIONES
       
        self.fechareserva = input("ingrese la fecha (dd-mm-yyyy): ")
        self.horareserva = input("ingrese hora (HH:MM): ")
        try:
            self.fechareserva = datetime.strptime(self.fechareserva, "%d-%m-%Y").date()
            print("Fecha ingresada: ", self.fechareserva)
        except ValueError:
            print("Fecha invalida, ingresarla con formato (dd-mm-yyyy)")
        try:
            self.horareserva = datetime.strptime(self.horareserva, "%H:%M").time()
            print("Hora ingresada: ", self.horareserva)
        except ValueError:
            print("Hora invalida, ingresarla con formato (HH:MM)")
       
        # IMPRESION
        
    def __str__(self):
        return ("Fecha de la reserva: " + str(self.fechareserva) + "\nHora de la reserva: " + str(self.horareserva))