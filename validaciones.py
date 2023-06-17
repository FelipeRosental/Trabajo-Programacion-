from string import *
from datetime import *

def validacion_numero (dato_numerico):
    """input: dato int (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INT INGRESADO SEA VALIDO\n
    output: True/False """
    if dato_numerico.isdigit() == False :
        return False
    else:
        return True

def validacion_string (dato_string):
    """input: dato string (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO STRING INGRESADO SEA VALIDO\n
    output: True/False """
    if dato_string.isalpha() == False:
        if  " " in dato_string: 
            return True
        else: 
            return False       
    else:
        return True
           
def validacion_DNI (dni):
    """input: dato int (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INT INGRESADO SEA VALIDO Y QUE SEA DE 8 DIGITOS\n
    output: True/False """
    if len(dni)==8:
        return validacion_numero(dni)
    return False

def validacion_Codigo (codigo):
    """input: dato int (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INT INGRESADO SEA VALIDO Y QUE SEA DE 4 DIGITOS\n
    output: True/False """
    if len(codigo)==4:
        return validacion_numero(codigo)
    return False 
        
def validacion_techada (techada):
    """input: dato string (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INGRESADO ESTÉ ENTRE LAS OPCIONES VALIDAS\n
    output: True/False """
    if  techada not in ["si", "no", "Si", "No"]:
        return False
    else:
        return True
    
def validacion_tipo_piso (piso):
    """input: dato string (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INGRESADO ESTÉ ENTRE LAS OPCIONES VALIDAS\n
    output: True/False """
    if  piso not in ["cesped", "polvo de ladrillo", "cemento", "Cesped", "Polvo de ladrillo", "Cemento"]:
        return False
    else:
        return True

def validacion_estado_cancha (estado):
    """input: dato string (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INGRESADO ESTÉ ENTRE LAS OPCIONES VALIDAS\n
    output: True/False """
    if  estado not in ["bueno", "malo", "intermedio", "Bueno", "Malo", "Intermedio"]:
        return False
    else:
        return True
    
def validacion_mail (email):
    """input: dato string (dato ingresado por teclado que se desea validar)\n
    funcion: VERIFICA QUE EL DATO INGRESADO TENGA @\n
    output: True/False """
    if "@" not in email:
        return False
    else:
        return True

def validacion_fecha_hora ():
    """input: nada\n
    funcion: GENERAR UNA FECHA Y HORA CON FORMATO DATETIME VALIDADO\n
    output: Fecha en formato validado con datetime (fecha y hora)"""
    año_actual = date.today().year
    while True: 
        fecha_hora = input("ingrese la fecha y la hora de la reserva (dd-mm-aaaa-hh:mm): ")
        try:
            fecha_hora = datetime.strptime(fecha_hora, "%d-%m-%Y-%H:%M")
            if int(fecha_hora.year) >= año_actual and int(fecha_hora.year) <= año_actual + 1:
                if fecha_hora.hour >= 10 and fecha_hora.hour <= 18:
                    return fecha_hora
                else:
                    print("El horario de reservas es entre las 10:00 y las 18:00")
            else:
                print("La fecha ingresada es anterior a la actual o es más de un año posterior")
                continue
        except ValueError:
            print("Fecha invalida, ingresarla con formato (dd-mm-aaaa-hh:mm)")
            continue

def validacion_mes():
    """input: nada\n
    funcion: GENERAR UN NUMERO DE MES VALIDADO\n
    output: Numero entre 1 y 12"""
    while True:
        dato_mes = input("Ingrese el numero del mes del cual desea ver los ingresos: ")
        try:
            dato_mes = int(dato_mes)
            if 1 <= dato_mes <= 12:
                return dato_mes
            else:
                print ("Debe ingresar un numero de mes (entre 1 y 12)")
        except ValueError:
            print("Debe ingresar un numero de mes (entre 1 y 12)")

