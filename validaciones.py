from string import *
from datetime import *

def validacion_numero (dato_numerico):
    """VERIFICA QUE EL DATO INT INGRESADO SEA VALIDO"""
    if dato_numerico.isdigit() == False :
        return False
    else:
        return True

def validacion_string (dato_string):
    """VERIFICA QUE EL DATO STRING INGRESADO SEA VALIDO"""
    if dato_string.isalpha() == False:
        if  " " in dato_string: 
            return True
        else: 
            return False       
    else:
        return True
           
def validacion_DNI (dni):
    """VERIFICA QUE EL DNI INGRESADO SEA VALIDO"""
    if len(dni)==8:
        return validacion_numero(dni)
    return False

def validacion_Codigo (codigo):
    """VERIFICA QUE EL CODIGO DE LA CANCHA SEA VALIDO"""
    if len(codigo)==4:
        return validacion_numero(codigo)
    return False 
        
def validacion_techada (techada):
    """VERIFICA QUE EL TIPO DE TECHO DE LA CANCHA INGRESADO SEA VALIDO"""
    if  techada not in ["si", "no", "Si", "No"]:
        return False
    else:
        return True
    
def validacion_tipo_piso (piso):
    if  piso not in ["cesped", "polvo de ladrillo", "cemento", "Cesped", "Polvo de ladrillo", "Cemento"]:
        return False
    else:
        return True

def validacion_estado_cancha (estado):
    """VERIFICA QUE EL ESTADO DE LA CANCHA SEA VALIDO"""
    if  estado not in ["bueno", "malo", "intermedio", "Bueno", "Malo", "Intermedio"]:
        return False
    else:
        return True
    
def validacion_mail (email):
    """VERIFICA QUE EL MAIL INGRESADO POR EL USUARIO TENGA @"""
    if "@" not in email:
        return False
    else:
        return True

def validacion_fecha_hora ():
    """DEVUELVE UNA FECHA Y HORA CON FORMATO DATETIME VALIDADO"""
    año_actual = date.today().year
    while True: 
        fecha_hora = input("ingrese la fecha y la hora de la reserva (dd/mm/aaaa/hh:mm): ")
        try:
            fecha_hora = datetime.strptime(fecha_hora, "%d/%m/%Y/%H:%M")
            if int(fecha_hora.year) >= año_actual and int(fecha_hora.year) <= año_actual + 1:
                if fecha_hora.hour >= 10 and fecha_hora.hour <= 18:
                    return fecha_hora
                else:
                    print("El horario de reservas es entre las 10:00 y las 18:00")
            else:
                print("La fecha ingresada es anterior a la actual o es más de un año posterior")
                continue
        except ValueError:
            print("Fecha invalida, ingresarla con formato (dd/mm/aaaa/hh:mm)")
            continue
    