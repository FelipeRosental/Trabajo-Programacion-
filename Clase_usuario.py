from validaciones import *

class Usuario:
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
        """input: filename = archivo txt que almacena a los usuarios (base de datos de usuarios)\n
        funcion: LEE LOS USUARIOS/ADMINISTRADORES DE LA BASE DE DATOS Y LOS INSTANCIA EN PYTHON EN UN DICCIONARIO\n
        output: diccionario de usuarios que tiene como clave el dni del usuario y como valor el objeto usuario"""
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
    def buscar_usuario (usuarios, usuario, contraseña): 
        """input: usuarios = diccionario de usuarios, usuario = nombre de usuario ingresado por teclado
        contraseña = contraseña ingresada por teclado\n
        funcion: BUSCAR UN USUARIO EN EL DICCIONARIO DE USUARIOS\n
        output: objeto usuario buscado"""
        for us in usuarios.values():
            if us.usuario == usuario and us.contraseña == contraseña:
                return us
        else:
            print("Error en los datos ingresados")
     
    def registrar_usuario(self, usuarios): 
        """input: self = objeto usuario, usuarios = diccionario de usuarios\n
        funcion: REGISTRAR UN USUARIO/ADMIN EN EL DICCIONARIO DE USUARIOS\n
        output: nada"""
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
                        if self.contraseña == us.contraseña and us.usuario == "admin":
                            print("La contraseña ya está siendo utilizada por otro administrador")
                            break
                    else:
                        usuarios[self.dni] = self       
                        print("Usuario registrado correctamente")
        else:                               
            print("DNI incorrecto (ya se encuentra ingresado)")  
                
    def cambiar_usuario(self, usuarios):  
        """input: self = objeto usuario, usuarios = diccionario de usuarios\n
        funcion: CAMBIAR UN USUARIO/ADMIN EN EL DICCIONARIO\n
        output: nada"""
        print(f"Sus datos son:\n{self}\nIngrese sus nuevos datos:")
        dni_nuevo = input("Ingrese su dni: ")
        while validacion_DNI(dni_nuevo) != True:
            print("DNI no valido.")
            dni_nuevo = input("Ingrese su dni: ")
        if dni_nuevo == self.dni:
            if self.usuario == "admin":
                contraseña_nueva = str(input("Ingrese su nueva contraseña: "))
                contraseña_valida = []
                for admin in usuarios.values():
                    if str(admin.contraseña) == contraseña_nueva and str(admin.contraseña) != self.contraseña:
                        contraseña_valida.append("No")
                if len(contraseña_valida) == 0:
                    usuarios[self.dni] = Usuario(dni=dni_nuevo, usuario=self.usuario, contraseña = contraseña_nueva)    
                    print("Sus datos fueron cambiados con exito")  
                else:
                    print("La contraseña ingresada ya se encuentra registrada")
            else: 
                usuario_nuevo = input("Ingrese su nuevo usuario: ")
                while usuario_nuevo == "admin":
                    print("Usuario no valido (usted no es un administrador)")
                    usuario_nuevo = input("Ingrese su nuevo usuario: ")
                usuario_valido = []
                for us in usuarios.values():
                    if usuario_nuevo == us.usuario and self.usuario != "admin" and usuario_nuevo != self.usuario:
                        usuario_valido.append("No")
                if len(usuario_valido) == 0:
                    usuarios[self.dni] = Usuario(dni=dni_nuevo, usuario=usuario_nuevo)    
                    print("Sus datos fueron cambiados con exito")     
                else:
                    print("El usuario ingresado ya se encuentra registrado")   
        else:
            if dni_nuevo not in usuarios.keys():
                if self.usuario == "admin":
                    contraseña_nueva = str(input("Ingrese su nueva contraseña: "))
                    contraseña_valida = []
                    for admin in usuarios.values():
                        if str(admin.contraseña) == contraseña_nueva:
                            contraseña_valida.append("No")
                    if len(contraseña_valida) == 0:
                        usuarios[self.dni] = Usuario(dni=dni_nuevo, usuario=self.usuario, contraseña = contraseña_nueva)    
                        print("Sus datos fueron cambiados con exito")  
                    else:
                        print("La contraseña ingresada ya está registrada")
                else:
                    usuario_nuevo = input("Ingrese su nuevo usuario: ")
                    while usuario_nuevo == "admin":
                        print("Usuario no valido (usted no es un administrador)")
                        usuario_nuevo = input("Ingrese su nuevo usuario: ")
                    usuario_valido = []
                    for us in usuarios.values():
                        if usuario_nuevo == us.usuario and self.usuario != "admin" and usuario_nuevo != self.usuario:
                            usuario_valido.append("No")
                    if len(usuario_valido) == 0:
                        usuarios[self.dni] = Usuario(dni=dni_nuevo, usuario=usuario_nuevo)    
                        print("Sus datos fueron cambiados con exito")     
                    else:
                        print("El usuario ingresado ya se encuentra registrado")   
            else:
                print("El dni ya se encuentra registrado")
            
    def eliminar_usuario(self, usuarios):  
        """input: self = objeto usuario, usuarios = diccionario de usuarios\n
        funcion: ELIMINAR UN USUARIO/ADMIN EN EL DICCIONARIO\n
        output: nada"""
        usuarios.pop(self.dni)
        print("Datos eliminados con exito")
    
    def ver_mis_reservas(self, reservas): 
        """input: self = objeto usuario, reservas = diccionario de reservas\n
        funcion: MOSTRAR LAS RESERVAS DE UN USUARIO\n
        output: reservas del usuario"""
        print("Sus reservas:\n")
        tiene_reservas = []
        for reserva in reservas.values():    
            if self.usuario == reserva.cliente:
                print(f"{reserva}\n")
                tiene_reservas.append("Si")
        if "Si" not in set(tiene_reservas):
            print("No tiene reservas realizadas\n")
            
    def ver_mis_datos(self, usuarios):
        """input: self = objeto usuario, usuarios = diccionario de usuarios\n
        funcion: MOSTRAR LOS DATOS DE UN USUARIO/ADMIN\n
        output: datos del usuario"""
        print("Sus datos: ")
        for dni in usuarios.keys():    
            if self.dni == dni:
                print(f"{self}\n")
    
    @staticmethod
    def iniciar_sesion(usuarios, usuario, contraseña, menu):   
        """input: usuarios = diccionario de usuarios, usuario = nombre de usuario del objeto usuario/admin,
        contraseña = contraseña del usuario/admin, menu = funcion menu (puede ser de usuarios o admins)\n
        funcion: INICIAR SESION DEL USUARIO/ADMIN\n
        output: menu de usuarios o menu de admins"""
        for us in usuarios.values():
            if usuario == us.usuario and contraseña == us.contraseña:
                user = Usuario.buscar_usuario(usuarios,usuario,contraseña)
                print("Sesion iniciada como " + str(usuario) + "\n")
                if user.usuario != "admin":
                    menu(user)
                else:
                    menu(user)
                break
        else:
            print("Datos incorrectos") 
    
    @staticmethod
    def reescribir_baseusuarios(usuarios, filename):  
        """input: usuarios = diccionario de usuarios, filename = base de datos de usuarios (archivo txt)\n
        funcion: REESCRIBIR LA BASE DE DATOS DE USUARIOS Y ADMINISTRADORES\n
        output: nada"""  
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
    
    @staticmethod
    def ver_datos(base_de_datos):
        """input: base de datos = diccionario de usuarios, canchas o reservas (segun lo que se desee)\n
        funcion: MOSTRAR LOS USUARIOS, CANCHAS O RESERVAS GUARDADAS EN LOS DICCIONARIOS\n
        output: datos de usuarios, canchas o reservas"""
        for dato in base_de_datos.values():
                print(f"{dato}\n")
