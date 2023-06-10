from string import *
from datetime import *

def validacion_numeros (dato_numerico):
    if dato_numerico.isdigit() == False :
        return False
    else:
        return True

def validacion_string (dato_string):
    if dato_string.isalpha() == False:
        if  " " in dato_string: 
            return True
        else: 
            return False       
    else:
        return True
           
def validacion_DNI (dni):
    if len(dni)==8:
        return validacion_numeros(dni)
    return False

def validacion_Codigo (codigo):
    if len(codigo)==4:
        return validacion_numeros(codigo)
    return False 
        
def validacionTechada (techada):
    if  techada not in {"si", "no", "Si", "No"}:
        return False
    else:
        return True
    
def validacionPiso (piso):
    if  piso not in {"cesped", "polvo de ladrillo", "cemento", "Cesped", "Polvo de ladrillo", "Cemento"}:
        return False
    else:
        return True

def validacionEstado (estado):
    if  estado not in {"bueno", "malo", "intermedio", "Bueno", "Malo", "Intermedio"}:
        return False
    else:
        return True
    
def validacionEmail (email):
    if "@" not in email:
        return False
    else:
        return True

def validacion_fecha_hora ():
    """DEVUELVE UNA FECHA Y HORA CON FORMATO DATETIME VALIDADO"""
    while True: 
        fecha_hora = input("ingrese la fecha y la hora de la reserva (dd/mm/aaaa/hh:mm): ")
        try:
            fecha_hora = datetime.strptime(fecha_hora, "%d/%m/%Y/%H:%M")
        except ValueError:
            print("Fecha invalida, ingresarla con formato (dd/mm/aaaa/hh:mm)")
            continue
        else: 
            break  
    return fecha_hora
