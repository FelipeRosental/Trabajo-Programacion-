from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES
from principal import * ### PRINCIPAL

def menu2():
    while True:
        print("ADMINISTRACION DE CANCHAS")
        menu = input("1. Agregar canchas\n2. Eliminar canchas\n3. Salir \nIngrese una opción: ")
        if menu == "1":
            club1.agregar_canchas()
        elif menu == "2":
            club1.eliminar_canchas()
        elif menu == "3":
            break
        else: 
            print("Opcion no disponible")
            
menu2()