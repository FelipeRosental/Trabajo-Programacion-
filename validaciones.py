from random import *
from datetime import *
from string import *

def validacionDNI (dni):
    while len(dni)==8:
        if dni.isdigit() == False:
            return False
        else:
            return True
    return False
def validacionUsuario(dni):
    with open("Usuarios.txt", 'r') as archivo:
        lista_lineas = archivo.readlines()
        archivo.close()
    with open("Usuarios.txt","r"):
        for linea in lista_lineas:
            if str(dni) in linea:
                return True               
            else:
                return False
        archivo.close()
              

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