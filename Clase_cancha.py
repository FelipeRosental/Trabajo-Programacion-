from validaciones import *

class Cancha: 
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
            while validacion_techada (self.techada) != True:
                print ("Respuesta no valida (debe ser si o no).")
                self.techada = input ("Ingrese si la cancha es techada: ")
        else: 
            self.techada = techada
        
        if piso is None:
            self.piso = input ("Ingrese el tipo de Piso (cesped, polvo de ladrillo, cemento): ")
            while validacion_tipo_piso (self.piso) != True:
                print ("Tipo de piso no valido.")
                self.piso = input ("Ingrese el tipo de Piso: ")
        else: 
            self.piso = piso    
           
        if estado is None: 
            self.estado = input ("Ingrese el Estado de la cancha (bueno, malo, intermedio): ")
            while validacion_estado_cancha (self.estado) != True:
                print ("Estado de la cancha no valido.")
                self.estado = input ("Ingrese el Estado de la cancha: ")
        else: 
            self.estado = estado  
    
    @staticmethod    
    def buscar_cancha (canchas, codigo): 
        """input: canchas = diccionario de canchas, codigo = codigo de la cancha buscada\n
        funcion: BUSCAR UNA CANCHA EN EL DICCIONARIO\n
        output: objeto cancha"""
        for cancha in canchas.values():
            if cancha.codigo == codigo:
                return cancha
        else:
            print("No se encontró el codigo ingresado")
    
    @staticmethod
    def leer_canchas(filename): 
        """input: filename = base de datos de canchas (archivo txt)\n
        funcion: LEER LA BASE DE DATOS E INSTANCIAR CANCHAS EN UN DICCIONARIO\n
        output: diccionario de canchas que tiene como clave el codigo de cancha y como valor el objeto cancha""" 
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
        """input: canchas = diccionario de canchas\n
        funcion: MOSTRAR LA CANCHA DISPONIBLE SEGUN LAS PREFERENCIAS DEL USUARIO\n
        output: nada"""  
        if self.codigo not in canchas.keys():
            canchas[self.codigo] = self       
            print("Cancha registrada correctamente")
        else:                               
            print("La cancha ya está ingresada")  
    
    def cambiar_cancha(self, canchas):   
        """input: self = objeto cancha, canchas = diccionario de canchas\n
        funcion: CAMBIAR UNA CANCHA EN EL DICCIONARIO\n
        output: nada"""
        print(f"Los datos de la cancha son:\n{self}\nIngrese los nuevos datos:")
        canchas[self.codigo] = Cancha(codigo=self.codigo)    
        print("Los datos fueron cambiados con exito") 
    
    @staticmethod
    def eliminar_cancha(canchas): 
        """input: canchas = diccionario de canchas\n
        funcion: ELIMINAR UNA CANCHA EN EL DICCIONARIO\n
        output: nada"""
        codigo = input("Ingrese el codigo de la cancha a eliminar: ")
        if codigo in set(canchas.keys()):
            canchas.pop(codigo)
            print("Cancha eliminada con exito")
        else: 
            print("Codigo incorrecto")
    
    @staticmethod
    def reescribir_basecanchas(canchas, filename): 
        """input: canchas = diccionario de canchas, filename = base de datos de canchas (archivo txt)\n
        funcion: REESCRIBE LA BASE DE DATOS DE CANCHAS (EL ARCHIVO TXT)\n
        output: nada"""
        try:
            with open(filename,"w") as basecanchas:
                for cancha in canchas.values():
                    basecanchas.write(f"{cancha.codigo};{cancha.techada};{cancha.piso};{cancha.estado};\n")
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False
    
    def __str__(self):
        return f"Codigo: {self.codigo} \nTechada: {self.techada} \nSuperficie: {self.piso} \nEstado: {self.estado}"