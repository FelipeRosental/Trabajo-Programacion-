from random import *
from datetime import *
from string import *

### VALIDACIONES ###

def validacionDNI (dni):
    while len(dni)==8:
        if dni.isdigit() == False:
            return False
        else:
            return True
    return False

def validacionTelefono (telefono):
        if telefono.isdigit() == False :
            return False
        else:
            return True

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
    
def validacionNombre (nombre):
    if nombre.isalpha() == False:
        return False
    else:
        return True
    
def validacionApellido (apellido):
    if apellido.isalpha() == False:
        return False
    else:
        return True

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