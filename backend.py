#######################################  CLASES DEL PROGRAMA ###############################################################

class usuario ():
    lista_usuarios = []
    def __init__(self, nombre, apellido, dni, edad, email, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.email = email
        self.telefono = telefono
        usuario.lista_usuarios.append([self.nombre, self.apellido, self.dni, self.edad, self.email, self.telefono])
    def eliminar_usuario (posicion):
        usuario.lista_usuarios.pop(posicion)
    def mostrar_usuarios():
        print("USUARIOS: " + str(usuario.lista_usuarios))
              
class cancha (): 
    lista_canchas = []
    def __init__(self, codigo, techada, estado, piso):
        self.codigo = codigo
        self.techada = techada
        self.estado = estado
        self.piso = piso
        cancha.lista_canchas.append([self.codigo, self.techada, self.estado, self.piso])
    def eliminar_cancha(posicion):
        cancha.lista_canchas.pop(posicion)  
    def mostrar_canchas():
        print("CANCHAS: " + str(cancha.lista_canchas))
       
class reserva (usuario, cancha):
    lista_reservas = []
    def __init__(self, fechareserva, horareserva):
        self.fechareserva = fechareserva
        self.horareserva = horareserva
        reserva.lista_reservas.append ([self.fechareserva, self.horareserva, usuario.dni, cancha.codigo])
    def mostrar_reservas():
        print("RESERVAS: " + str(reserva.lista_reservas))

################################## PRUEBA DE FUNCIONAMIENTO #################################################################

usuario1= usuario ("Felipe", " Perez", 42729645, 20, "pepito@gmail.com", 48348433)
usuario2 = usuario ("Carlos", "Rodriguez", 34729675, 24, "pepito1@gmail.com", 78481433)
cancha1 = cancha (123, "Si", "Bueno", "Polvo de ladrillo")
cancha2 = cancha (124, "No", "Malo", "Cesped")
reserva1 = reserva ("2023/04/12", "12:00")
reserva2 = reserva ("2023/04/14", "15:00")

usuario.mostrar_usuarios ()
cancha.mostrar_canchas ()
reserva.mostrar_reservas()











