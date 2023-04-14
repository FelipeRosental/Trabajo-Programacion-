from random import *
from datetime import *
from string import *

from validaciones import *

class Usuario ():
    
    def __init__(self):
        
        # VALIDACIONES
        
        self.nombre = input("Ingrese Nombre: ")
        while validacionNombre(self.nombre) != True:
            print ("Nombre no valido.")
            self.nombre = input("Ingrese Nombre: ")
        
        self.apellido = input("Ingrese Apellido: ") 
        while validacionApellido(self.apellido) != True:
            print ("Apellido no valido.")
            self.apellido = input("Ingrese Apellido: ")
       
        self.dni = input("Ingrese DNI: ")
        while validacionDNI(self.dni) != True:
            print("DNI no valido.")
            self.dni = input("Ingrese DNI: ")
            
        self.telefono = input("Ingrese Telefono: ")
        while validacionTelefono(self.telefono) != True:
            print("Telefono no valido.")
            self.telefono = input("Ingrese Telefono: ")
        
        self.edad = input("Ingrese Edad: ")    
        while validacionEdad(self.edad) != True:
            print ("Edad no valida.")
            self.edad = input("Ingrese Edad: ")
        
        self.email = input("Ingrese Email: ")  
        while validacionEmail(self.email) != True:
           print ("Email no valido.")
           self.email = input("Ingrese Email: ")
        
        # IMPRESION
        
    def __str__(self):
        return ("Nombre: " + str(self.nombre) + "\nApellido: " + str(self.apellido) + "\nDNI: " + str(self.dni) + "\nTelefono: " + str(self.telefono) + "\nEdad: " + str(self.edad) + "\nEmail: " + str(self.email))
      
class Cancha (): 
    
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
        except ValueError:
            print("Fecha invalida, ingresarla con formato (dd-mm-yyyy)")
        try:
            self.horareserva = datetime.strptime(self.horareserva, "%H:%M").time()
        except ValueError:
            print("Hora invalida, ingresarla con formato (HH:MM)")
       
        # IMPRESION
        
    def __str__(self):
        return ("Fecha de la reserva: " + str(self.fechareserva) + "\nHora de la reserva: " + str(self.horareserva))