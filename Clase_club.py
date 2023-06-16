from Clase_cancha import *
from Clase_usuario import *
from Clase_reserva import *

class Club:
    
    """EN ESTA CLASE SE GUARDAN TODOS LOS USUARIOS, ADMINS, CANCHAS Y RESERVAS DEL CLUB"""
    usuarios_y_admins = Usuario.leer_usuarios("Usuarios.txt")
    canchas = Cancha.leer_canchas("Canchas.txt")
    reservas = Reserva.leer_reservas("Reservas.txt")
    
    def __init__(self, nombre, direccion, horario):
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        
    def ver_ingresos (self):
        """MUESTRA LOS INGRESOS DEL CLUB (DINERO OBTENIDO A PARTIR DE RESERVAS DE CANCHAS)"""
        cant_reservas = len(self.reservas.keys())
        ingresos = cant_reservas * 3000 #El precio por hora de una cancha es de 3000$ (se puede modificar)   
        print(f"\nIngresos del club: {ingresos}$\n")
        
    def __str__(self):
        return f"\nClub: {self.nombre}\nDireccion: {self.direccion}\nHorario: {self.horario}\n"
