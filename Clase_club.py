from Clase_cancha import *
from Clase_usuario import *
from Clase_reserva import *

class Club:
    """Clase que guarda los usuarios, administradores, canchas y reservas. En ella también se lleva a cabo la parte financiera"""
    usuarios_y_admins = Usuario.leer_usuarios("Usuarios.txt")
    canchas = Cancha.leer_canchas("Canchas.txt")
    reservas = Reserva.leer_reservas("Reservas.txt")
    
    def __init__(self, nombre, direccion, horario):
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        
    def ver_ingresos_del_mes (self):
        """input: self = objeto club\n
        funcion: MOSTRAR LOS INGRESOS DEL CLUB EN UN DETERMINADO MES\n
        output: ingresos del mes"""
        mes_deseado = validacion_mes()
        cant_reservas_del_mes = 0
        for reserva in self.reservas.values(): 
            fecha = datetime.strptime(reserva.fecha_hora, "%Y-%m-%d %H:%M:%S")
            if fecha.month == mes_deseado:
                cant_reservas_del_mes += 1       
        ingresos = cant_reservas_del_mes * 3000 #El precio por hora de una cancha es de 3000$ (se puede modificar)   
        print(f"\nIngresos del club en el mes numero {mes_deseado}: {ingresos}$\n")
        
    def __str__(self):
        return f"\nClub: {self.nombre}\nDireccion: {self.direccion}\nHorario: {self.horario}\n"

