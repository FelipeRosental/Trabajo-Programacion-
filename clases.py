from random import *
from datetime import *
from string import *

from validaciones import *

class Usuario ():
    
    def __init__(self):
        
        # VALIDACIONES
        self.dni = input("Ingrese DNI: ")
        while validacionDNI(self.dni) != True:
            print("DNI no valido.")
            self.dni = input("Ingrese DNI: ")
            
        self.nombre = input("Ingrese Nombre: ")
        while validacionNombre(self.nombre) != True:
            print ("Nombre no valido.")
            self.nombre = input("Ingrese Nombre: ")
        
        self.apellido = input("Ingrese Apellido: ") 
        while validacionApellido(self.apellido) != True:
            print ("Apellido no valido.")
            self.apellido = input("Ingrese Apellido: ")
            
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
        return ("Nombre: " + str(self.nombre) + " Apellido: " + str(self.apellido) + " DNI: " + str(self.dni) + " Telefono: " + str(self.telefono) + " Edad: " + str(self.edad) + " Email: " + str(self.email))
      
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
            
        while True:
            self.horario = input ("Ingrese horario disponible (HH:MM): ")
            try:
                self.horario = datetime.strptime(self.horario, "%H:%M").time()
            except ValueError:
                print("Hora invalida, ingresarla con formato (HH:MM)")
                continue
            else:
                break   
        
        # IMPRESION
        
    def __str__(self):
        return ("Codigo: " + str(self.codigo) + " Techada: " + self.techada + " Piso: " + self.piso + " Estado: " + self.estado + " Horario: " + str(self.horario))
               
class Reserva ():
    
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
        
        # IMPRESION
        
    def __str__(self):
        return ("Codigo de Reserva: " + str(self.codreserva) + " Fecha de la reserva: " + str(self.fechareserva) + " Hora de la reserva: " + str(self.horareserva))