from random import *
from datetime import *
from string import *
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
            while validacion_numeros(self.telefono) != True:
                print("Telefono no valido.")
                self.telefono = input("Ingrese Telefono: ")
        else: 
            self.telefono = telefono
        
        if edad is None:
            self.edad = input("Ingrese Edad: ")    
            while validacion_numeros(self.edad) != True:
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
        usuarios[self.dni] = Usuario()    
        print("Sus datos fueron cambiados con exito")    
        
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
      
class Cancha (): 
    def __init__(self, codigo=None, techada=None, piso=None, estado=None):
        if codigo is None:
            self.codigo = input ("Ingrese el codigo de cancha (numero de 4 digitos): ")
            while validacion_Codigo (self.codigo) != True:
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
    
    @staticmethod    
    def instanciar_cancha (canchas, codigo): 
        """BUSCA UNA CANCHA EN EL DICCIONARIO Y LA INSTANCIA"""
        for cancha in canchas.values():
            if cancha.codigo == codigo:
                return cancha
        else:
            print("No se encontró el codigo ingresado")
    
    @staticmethod
    def leer_canchas(filename):  
        """LEE LA BASE DE DATOS E INSTANCIA CANCHAS EN PYTHON, LAS DEVUELVE EN UN DICCIONARIO """
        canchas = {}
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    cancha = Cancha(datos[0], datos[1], datos[2], datos[3])            
                    canchas[cancha.codigo] = cancha
            return canchas     
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False                
    
    def agregar_cancha(self,canchas):  
        """AGREGA UNA CANCHA EN EL DICCIONARIO"""
        if self.codigo not in canchas.keys():
            canchas[self.codigo] = self       
            print("Cancha registrada correctamente")
        else:                               
            print("La cancha ya está ingresada")  
    
    def cambiar_cancha(self, canchas):   
        """CAMBIA UNA CANCHA EN EL DICCIONARIO"""
        print(f"Los datos de la cancha son:\n{self}\nIngrese los nuevos datos:")
        canchas[self.codigo] = Cancha(codigo=self.codigo)    
        print("Los datos fueron cambiados con exito") 
    
    @staticmethod
    def eliminar_cancha(canchas): 
        """ELIMINA UNA CANCHA EN EL DICCIONARIO"""
        codigo = input("Ingrese el codigo de la cancha a eliminar: ")
        if codigo in canchas.keys():
            canchas.pop(codigo)
            print("Cancha eliminada con exito")
        else: 
            print("Codigo incorrecto")
    
    @staticmethod
    def reescribir_basecanchas(canchas, filename): 
        """REESCRIBE LA BASE DE DATOS DE CANCHAS"""
        try:
            with open(filename,"w") as basecanchas:
                for cancha in canchas.values():
                    basecanchas.write(f"{cancha.codigo};{cancha.techada};{cancha.piso};{cancha.estado};\n")
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def __str__(self):
        return f"Codigo: {self.codigo} \nTechada: {self.techada} \nSuperficie: {self.piso} \nEstado: {self.estado}"

            
class Reserva (): 
    def __init__(self, codigo=None, cancha=None, fecha_hora=None, cliente=None):        
        if codigo is None: 
            self.codigo = randint(1000,9999)
        else: 
            self.codigo = codigo
        
        self.cancha = cancha
        
        if fecha_hora is None:
            while True: 
                self.fecha_hora = input("ingrese la fecha y la hora de la reserva (dd/mm/aaaa/hh:mm): ")
                try:
                    self.fecha_hora = datetime.strptime(self.fecha_hora, "%d/%m/%Y/%H:%M")
                except ValueError:
                    print("Fecha invalida, ingresarla con formato (dd/mm/aaaa/hh:mm)")
                    continue
                else: 
                    break   
            
        else: 
            self.fecha_hora = fecha_hora

        self.cliente = cliente
    
    @staticmethod
    def leer_reservas(filename):  
        """LEE LA BASE DE DATOS E INSTANCIA RESERVAS EN PYTHON, DEVUELVE UN DICCIONARIO"""
        reservas = {}
        try:
            with open(filename) as f:
                lineas = f.readlines()
                for linea in lineas:
                    datos = linea.split(";")
                    reserva = Reserva(datos[0], datos[1], datos[2],datos[3])
                    reservas[reserva.codigo] = reserva
            return reservas    
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    @staticmethod
    def buscar_reserva (reservas, cliente): # NO SE USA
        """BUSCA UNA RESERVA EN EL DICCIONARIO Y LA INSTANCIA"""
        for reserva in reservas.values():
            if reserva.cliente == cliente:
                return reserva

    def ver_canchas_disponibles(canchas): 
        """SUB MENU QUE MUESTRA LAS CANCHAS DISPONIBLES SEGUN LA PREFERENCIA DEL USUARIO"""
        techada = input ("Ingrese si desea una cancha techada (si,no): ")
        while validacionTechada (techada) != True:
            print ("Respuesta no valida (debe ser si o no)")
            techada = input ("Ingrese si la cancha que desea es techada: ")
        superficie = input("Que tipo de superficie desea? (cesped/cemento/polvo de ladrillo) ")
        while validacionPiso (superficie) != True:
            print("Respuesta no valida")
            superficie = input("Que tipo de superficie desea? (cesped/cemento/polvo de ladrillo) ")
        codigos = []
        for cancha in canchas.values():
            if cancha.techada == techada and cancha.piso == superficie:
                codigos.append(cancha.codigo)
        return codigos
        
    def hacer_reserva (reservas,canchas,usuario):    
        """REALIZA UNA RESERVA Y LA AGREGA AL DICCIONARIO"""
        cod_canchas_disponibles = Reserva.ver_canchas_disponibles(canchas)
        if len(cod_canchas_disponibles) == 0:
            print ("No hay canchas de esas características")
            return
        while True: 
            fecha_hora_input = input("ingrese la fecha y la hora de la reserva (dd/mm/aaaa/hh:mm): ")
            try:
                fecha_hora_input = datetime.strptime(fecha_hora_input, "%d/%m/%Y/%H:%M")
            except ValueError:
                print("Fecha invalida, ingresarla con formato (dd/mm/aaaa/hh:mm)")
                continue
            else: 
                break  
        salir = False
        for cod_cancha in cod_canchas_disponibles:
            for reserva in reservas.values():    
                if cod_cancha == reserva.cancha and str(fecha_hora_input) != str(reserva.fecha_hora):
                    reserva1 = Reserva(cancha = cod_cancha, cliente = usuario.usuario, fecha_hora=fecha_hora_input)
                    reservas[reserva1.codigo]=reserva1
                    salir = True
                    break
                elif  cod_cancha != reserva.cancha:
                    reserva1 = Reserva(cancha = cod_cancha, cliente = usuario.usuario, fecha_hora=fecha_hora_input)
                    reservas[reserva1.codigo]=reserva1
                    salir = True
                    break
                else:
                    continue
            if salir == True:
                print("Reserva realizada con exito")
                break
        # NO FUNCA !!!! SE PUEDEN REPETIR RESERVAS IDENTICAS (DEBERIA SALTAR ERROR) Y NO LEE BIEN TODAS LAS CANCHAS
                                 
    def cambiar_reserva(reserva, reservas):   
        """CAMBIA UNA RESERVA EN EL DICCIONARIO"""
        reservas[reserva.codigo] = Reserva(codigo = reserva.codigo, cancha = reserva.cancha, cliente = reserva.cliente)    
        print("Los datos fueron cambiados con exito") 
    
    # HACER ESTO BIEN !!!
    # ACÁ HABRIA QUE VERIFICAR QUE LA NUEVA FECHA INGRESADA NO ESTÉ RESERVADA, Y TAMBIEN HABRÍA QUE VER SI NO QUIERE CAMBIAR LA CANCHA...
    
    @staticmethod
    def eliminar_reserva(reservas): 
        """ELIMINA UNA RESERVA DEL DICCIONARIO"""
        codigo = input("Ingrese el codigo de la reserva a eliminar: ")
        if codigo in reservas.keys():
            reservas.pop(codigo)
            print("Reserva eliminada con exito")
        else: 
            print("Codigo incorrecto")
    
    @staticmethod
    def reescribir_basereservas(reservas, filename):   
        """REESCRIBE LA BASE DE DATOS DE RESERVAS"""
        try:
            with open(filename,"w") as basereservas:
                for reserva in reservas.values():
                    basereservas.write(f"{reserva.codigo};{reserva.cancha};{reserva.fecha_hora};{reserva.cliente};\n")
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False 
        
    def __str__(self):
        return f"Codigo de reserva: {self.codigo}\nCodigo de cancha: {self.cancha}\nFecha y hora: {self.fecha_hora}"
