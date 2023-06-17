from random import *
from validaciones import *
           
class Reserva: 
    def __init__(self, codigo=None, cancha=None, fecha_hora=None, cliente=None):        
        if codigo is None: 
            self.codigo = randint(1000,9999)
        else: 
            self.codigo = codigo
        
        self.cancha = cancha
        
        if fecha_hora is None:
            self.fecha_hora = validacion_fecha_hora() 
        else: 
            self.fecha_hora = fecha_hora

        self.cliente = cliente
    
    @staticmethod
    def leer_reservas(filename): 
        """input: filename = base de datos de reservas (archivo txt)\n
        funcion: LEER LA BASE DE DATOS E INSTANCIAR LAS RESERVAS EN UN DICCIONARIO CUYA CLAVE ES EL CODIGO DE RESERVA
        Y CUYO VALOR ES EL OBJETO RESERVA\n
        output: diccionario de reservas""" 
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

    def ver_cancha_disponible(canchas): 
        """input: canchas = diccionario de canchas\n
        funcion: MOSTRAR LA CANCHA DISPONIBLE SEGUN LAS PREFERENCIAS DEL USUARIO\n
        output: objeto cancha"""
        techada = input ("Ingrese si desea una cancha techada (si,no): ")
        while validacion_techada (techada) != True:
            print ("Respuesta no valida (debe ser si o no)")
            techada = input ("Ingrese si la cancha que desea es techada: ")
        superficie = input("Que tipo de superficie desea? (cesped/cemento/polvo de ladrillo) ")
        while validacion_tipo_piso (superficie) != True:
            print("Respuesta no valida")
            superficie = input("Que tipo de superficie desea? (cesped/cemento/polvo de ladrillo) ")
        for cancha in canchas.values():
            if cancha.techada == techada and cancha.piso == superficie:
                return cancha.codigo
        
    def hacer_reserva (reservas,canchas,user):    
        """input: reservas = diccionario de reservas, canchas = diccionario de canchas,
        user = objeto usuario que realiza la reserva\n
        funcion: HACER UNA RESERVA\n
        output: se agrega el objeto reserva al diccionario"""
        print("A saber: las canchas se pueden reservar únicamente por 1 hora entre las 10:00 y las 18:00")
        print("El precio de las canchas es de 3000$ por hora")
        print("Que tipo de cancha desea?")
        cod_cancha_disponible = Reserva.ver_cancha_disponible(canchas)
        if cod_cancha_disponible is None:
            print ("No hay canchas de esas características")
            return
        fecha_hora_input = validacion_fecha_hora()
        reserva_valida = False
        for reserva in reservas.values():
            if cod_cancha_disponible == reserva.cancha and str(fecha_hora_input) != str(reserva.fecha_hora):
                reserva_valida = True
            elif cod_cancha_disponible == reserva.cancha and str(fecha_hora_input) == str(reserva.fecha_hora):
                reserva_valida = False
                break
            else: 
                reserva_valida = True
        if reserva_valida is True:
            codigo_reserva = randint(1000,9999)
            reservas[codigo_reserva] = Reserva(codigo = codigo_reserva, cancha = cod_cancha_disponible,fecha_hora = fecha_hora_input, cliente = user.usuario)
            print("Reserva realizada con exito")
        else: 
            print("No hay canchas de las características ingresadas disponibles en ese horario")       
            
    def cambiar_reserva(self, reservas, canchas):   
        """input: self = objeto reserva, reservas = diccionario de reservas, canchas = diccionario de canchas\n
        funcion: MODIFICAR UNA RESERVA\n
        output: nada"""
        cancha_nueva = Reserva.ver_cancha_disponible(canchas)
        if cancha_nueva is None:
            print ("No hay canchas de esas características")
            return
        fecha_hora_nueva = validacion_fecha_hora()
        reserva_valida = False
        for reserva in reservas.values():
            if cancha_nueva == reserva.cancha and str(fecha_hora_nueva) != str(reserva.fecha_hora):
                reserva_valida = True
            elif cancha_nueva == reserva.cancha and str(fecha_hora_nueva) == str(reserva.fecha_hora):
                reserva_valida = False
                break
            else: 
                reserva_valida = True
        if reserva_valida is True:
            reservas[self.codigo] = Reserva(codigo = self.codigo, cancha = cancha_nueva, cliente = self.cliente, fecha_hora = fecha_hora_nueva)    
            print("Los datos fueron cambiados con exito") 
        else:
            print("El horario ingresado ya está reservado en esa cancha")
        
    @staticmethod
    def eliminar_reserva(reservas): 
        """input: reservas = diccionario de reservas\n
        funcion: ELIMINA UNA RESERVA DEL DICCIONARIO\n
        output: nada"""
        codigo = input("Ingrese el codigo de la reserva a eliminar: ")
        if codigo in list(reservas.keys()):
            reservas.pop(codigo)
            print("Reserva eliminada con exito")
        else: 
            print("Codigo incorrecto")
    
    @staticmethod
    def reescribir_basereservas(reservas, filename):   
        """input: reservas = diccionario de reservas, filename = base de datos de reservas (archivo txt)\n
        funcion: REESCRIBE LA BASE DE DATOS DE RESERVAS (EL ARCHIVO TXT)\n
        output: nada"""
        try:
            with open(filename,"w") as basereservas:
                for reserva in reservas.values():
                    basereservas.write(f"{reserva.codigo};{reserva.cancha};{reserva.fecha_hora};{reserva.cliente};\n")
        except FileNotFoundError:
            print("Error: archivo vacio")
            return False 
        
    def __str__(self):
        return f"Codigo de reserva: {self.codigo}\nCodigo de cancha: {self.cancha}\nFecha y hora: {self.fecha_hora}"

       