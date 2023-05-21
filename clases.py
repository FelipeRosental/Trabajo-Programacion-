from random import *
from datetime import *
from string import *

from validaciones import *

class Usuario ():
    # cada vez que creas un usuario, lo agregas a la lista de usuarios
    set_usuarios = set()
    
    def __init__(self, dni=None, nombre=None, apellido=None, telefono=None, edad=None, email=None):
        
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
        
        Usuario.set_usuarios.add(self)
    
    # METODOS DE USUARIOS 
    
    def leer_usuarios(self,filename):
        users = set()
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    user = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])            
                    users.add(user)
            return users     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def agregar_usuario(self,filename):
        with open(filename, "a") as archivo:
            archivo.write(f"{self.dni};{self.nombre};{self.apellido};{self.telefono};{self.edad};{self.email};\n")
            
    def actualizar_usuarios(self,filename):    
        guardados = self.leer_usuarios(filename)
        a_guardar = Usuario.set_usuarios - guardados 
        for user in a_guardar:
            user.agregar_usuario(filename)

    # NO FUNCIONA BIEN!!! CUANDO SE INGRESA UN USUARIO QUE YA ESTÁ EN LA BASE DE DATOS NO SALTA ERROR
    
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
    
    def registrar_usuario (usuario,contraseña):
        with open("InicioSesion.txt", "a") as archivo:
            archivo.write (f"{usuario}:{str(contraseña)}\n")
    
    def cambiar_contraseña(usuario, contraseña_nueva):
        with open("InicioSesion.txt", 'r') as archivo:
            lineas = archivo.readlines()
        with open("InicioSesion.txt", 'w') as archivo:                    
            for linea in lineas:
                if usuario not in linea:
                    archivo.write(str(linea))
                else:
                    archivo.write(usuario + ":" + str(contraseña_nueva) + "\n")
    
    def es_administrador (usuario, contraseña):
        if usuario in {"Admin", "admin", "ADMIN"} and contraseña in {"Admin", "admin", "ADMIN"}:
            return True
                
    # IMPRESION
    
    def __str__(self):
        return ("Nombre: " + self.nombre + " Apellido: " +  self.apellido + " Telefono: " + self.telefono + " Edad: " + str(self.edad) + " Mail: " + self.email + " Dni: " + str(self.dni))
      
class Cancha (): 
    
    lista_canchas = [] 
    
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
        
        Cancha.lista_canchas.append(self)
        
    # METODOS DE CANCHAS
        
    def agregar_cancha (self,filename):
        with open(filename, "a") as archivo:
            archivo.write(f"{self.codigo};{self.techada};{self.piso};{self.estado};{self.horario};\n")
    
    def leer_canchas(filename):
        canchas = []
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    cancha = Cancha(datos[0], datos[1], datos[2], datos[3], datos[4])            
                    canchas.append(cancha)
            return canchas     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def actualizar_canchas(self,filename): 
        a_guardar = []   
        guardadas = Cancha.leer_canchas(filename)
        for cancha in Cancha.lista_canchas:
            if cancha not in guardadas:
                a_guardar.append(cancha)
        for user in a_guardar:
            user.agregar_cancha(filename)
    
    ### PASA LO MISMO QUE CON LOS METODOS DE USUARIOS, CORREGIR
    
    def eliminar_canchas(self):   ### CAMBIAR ESTO!!!
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
    
    def __init__(self, codigo=None, fechareserva=None, horareserva=None):
        
        # ATRIBUTOS
        
        if codigo is None: 
            self.codreserva = randint(1000,9999)
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
        
        self.lista_reservas.append(self)
    
    # METODOS DE RESERVAS
    
    def agregar_reservas (self):        ### CAMBIAR
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
    
    def eliminar_reservas(self):      ### CAMBIAR 
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







    




