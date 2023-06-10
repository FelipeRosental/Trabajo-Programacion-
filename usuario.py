from validaciones import *

class Usuario ():
    def __init__(self,dni=None, nombre=None, apellido=None, telefono=None, edad=None, email=None, usuario=None, contraseña=None):
        if dni is None:
            self.dni = input("Ingrese DNI: ")
            while validacion_DNI(self.dni) != True:
                print("DNI no valido.")
                self.dni = input("Ingrese DNI: ")
        else:
            self.dni = dni
            
        if nombre is None:
            self.nombre = input("Ingrese Nombre: ")
            while validacion_string(self.nombre) != True:
                print ("Nombre no valido.")
                self.nombre = input("Ingrese Nombre: ")
        else: 
            self.nombre = nombre
        
        if apellido is None:
            self.apellido = input("Ingrese Apellido: ") 
            while validacion_string(self.apellido) != True:
                print ("Apellido no valido.")
                self.apellido = input("Ingrese Apellido: ")
        else: 
            self.apellido = apellido    
        
        if telefono is None:
            self.telefono = input("Ingrese Telefono: ")
            while validacion_numero(self.telefono) != True:
                print("Telefono no valido.")
                self.telefono = input("Ingrese Telefono: ")
        else: 
            self.telefono = telefono
        
        if edad is None:
            self.edad = input("Ingrese Edad: ")    
            while validacion_numero(self.edad) != True:
                print ("Edad no valida.")
                self.edad = input("Ingrese Edad: ")
        else: 
            self.edad = edad
            
        if email is None:    
            self.email = input("Ingrese Email: ")  
            while validacion_mail(self.email) != True:
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
    
    @staticmethod
    def leer_usuarios(filename): 
        """LEE LOS USUARIOS/ADMINISTRADORES DE LA BASE DE DATOS Y LOS INSTANCIA EN PYTHON EN UN DICCIONARIO"""
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
    
    @staticmethod
    def instanciar_usuario (usuarios, usuario, contraseña): 
        """BUSCA UN USUARIO EN EL DICCIONARIO QUE ALMACENA USUARIOS Y LO INSTANCIA"""
        for us in usuarios.values():
            if us.usuario == usuario and us.contraseña == contraseña:
                return us
        else:
            print("Error en los datos ingresados")
     
    def registrar_usuario(self, usuarios): 
        """REGISTRA USUARIOS Y ADMINISTRADORES EN UN DICCIONARIO"""
        if self.dni not in usuarios.keys():
            for us in usuarios.values():
                if self.usuario == us.usuario and self.usuario != "admin":
                    print("El usuario ingresado ya está en uso") 
                    break
            else:
                if self.usuario != "admin":
                    usuarios[self.dni] = self       
                    print("Usuario registrado correctamente")
                else:
                    for us in usuarios.values():
                        if self.contraseña == us.contraseña:
                            print("La contraseña ya está siendo utilizada por otro administrador")
                            break
                    else:
                        usuarios[self.dni] = self       
                        print("Usuario registrado correctamente")
        else:                               
            print("DNI incorrecto")  
                
    def cambiar_usuario(self, usuarios):  
        """CAMBIA UN USUARIO/ADMINISTRADOR EN EL DICCIONARIO"""
        print(f"Sus datos son:\n{self}\nIngrese sus nuevos datos:")
        dni_nuevo = input("Ingrese su dni: ")
        while validacion_DNI(self.dni) != True:
            print("DNI no valido.")
            dni_nuevo = input("Ingrese su dni: ")
        if dni_nuevo == self.dni:
            usuarios[self.dni] = Usuario(dni=dni_nuevo)    
            print("Sus datos fueron cambiados con exito")  
        else:
            if dni_nuevo not in usuarios.keys():
                usuarios[self.dni] = Usuario(dni=dni_nuevo)    
                print("Sus datos fueron cambiados con exito")    
            else:
                print("El dni ya se encuentra ingresado")
            
    def eliminar_usuario(self, usuarios):  
        """ELIMINA UN USUARIO/ADMINISTRADOR EN EL DICCIONARIO"""
        usuarios.pop(self.dni)
        print("Datos eliminados con exito")
    
    def ver_mis_reservas(self, reservas): 
        """MUESTRA LAS RESERVAS DE UN USUARIO"""
        print("Sus reservas:\n")
        tiene_reservas = []
        for reserva in reservas.values():    
            if self.usuario == reserva.cliente:
                print(f"{reserva}\n")
                tiene_reservas.append("Si")
        if "Si" not in set(tiene_reservas):
            print("No tiene reservas realizadas\n")
            
    def ver_mis_datos(self, usuarios):
        """MUESTRA LOS DATOS DE UN USUARIO/ADMINISTRADOR"""
        print("Sus datos: ")
        for user in usuarios.values():    
            if self.dni == user.dni and self.usuario == user.usuario:
                print(f"{user}\n")
    
    @staticmethod
    def iniciar_sesion(usuarios, usuario, contraseña, menu):   
        """INICIA SESION TANTO PARA USUARIOS COMO PARA ADMINISTRADORES"""
        for us in usuarios.values():
            if usuario == us.usuario and contraseña == us.contraseña:
                user = Usuario.instanciar_usuario(usuarios,usuario,contraseña)
                print("Sesion iniciada como " + str(usuario))
                if user.usuario != "admin":
                    menu(user)
                else:
                    menu(user)
                break
        else:
            print("Datos incorrectos") 
    
    @staticmethod
    def reescribir_baseusuarios(usuarios, filename):    
        """REESCRIBE LA BASE DE DATOS DE USUARIOS Y ADMINISTRADORES"""
        try:
            with open(filename,"w") as baseusuarios:
                for us in usuarios.values():
                    baseusuarios.write(f"{us.dni};{us.nombre};{us.apellido};{us.telefono};{us.edad};{us.email};{us.usuario};{us.contraseña};\n")
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def __str__(self):
        return f" Nombre: {self.nombre} \n Apellido: {self.apellido} \n DNI: {self.dni} \n Telefono: {self.telefono} \n Edad: {self.edad} \n Mail: {self.email}"
    

class Administrador (Usuario):
    def __init__(self,dni=None, nombre=None, apellido=None, telefono=None, edad=None, email=None, usuario="admin", contraseña=None):
        super().__init__(dni,nombre, apellido, telefono, edad, email, usuario,contraseña)
    
    def ver_datos(self,base_de_datos):
        """MUESTRA LOS USUARIOS, CANCHAS O RESERVAS GUARDADAS EN LOS DICCIONARIOS (QUE SE OBTIENEN DE LAS BASES DE DATOS)"""
        for dato in base_de_datos.values():
                print(f"{dato}\n")