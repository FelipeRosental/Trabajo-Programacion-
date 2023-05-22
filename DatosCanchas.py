from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES

def menuCanchas():
    while True:
        print("ADMINISTRACION DE CANCHAS")
        menu = input("1. Ver canchas\n2. Agregar canchas\n3. Eliminar canchas\n4. Salir \nIngrese una opción: ")
        if menu == "1":
            ### COMO INSTANCIAMOS ESTO???
            for canchas in Cancha.leer_canchas("Canchas.txt"):
                print (canchas)
        elif menu == "2":
            cancha = Cancha()
            cancha.actualizar_canchas("Canchas.txt")
        elif menu == "3":
            cancha = Cancha()
            cancha.eliminar_canchas()
            cancha.actualizar_canchas("Canchas.txt")
        elif menu == "4":
            break
        else: 
            print("Opcion no disponible")
            
