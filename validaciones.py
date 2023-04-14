from random import *
from datetime import *
from string import *

### VALIDACIONES ###

def validacionDNIyTelefono (dni, telefono):
    while len(dni)==8:
        if dni.isdigit() == False or telefono.isdigit() == False :
            return False
        else:
            return True
    return False

def validacionEdad (edad):
    if edad.isdigit() == False:
        return False
    else:  
        return True  
    
def validacionCodigo (codigo):
    while len(codigo)==4:
        if codigo.isdigit() == False:
            return False
        else:
            return True
    return False

""" def validacionFecha (fechareserva, horareserva):
    if fechareserva != datetime.date or horareserva != datetime.time:
        return False
    else:
        return True """
### NO USAMOS ESTA VALIDACION (LA DEJAMOS POR LAS DUDAS) ###
    
def validacionStringUsuario (nombre, apellido):
    if nombre.isalpha() == False or apellido.isalpha() == False:
        return False
    else:
        return True
    
def validacionStringCancha (techada, piso, estado):
    if techada.isalpha() == False or piso.isalpha() == False or estado.isalpha() == False:
        return False
    else:
        return True
    
def validacionEmail (email):
    if "@" not in email:
        return False
    else:
        return True