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
            Cancha.ver_canchas("Canchas.txt")
        elif menu == "2":
            cancha = Cancha()
            cancha.actualizar_canchas("Canchas.txt") 
        elif menu == "3":
            cancha = Cancha()
            cancha.eliminar_canchas("Canchas.txt")
        elif menu == "4":
            break
        else: 
            print("Opcion no disponible")
          
menuCanchas()
### NO FUNCIONA BIEN (CUANDO AGREGO UNA CANCHA QUE YA ESTÁ INGRESADA NO ME SALTA ERROR Y ME AGREGA CUALQUIER COSA)
### ADEMAS, CUANDO INGRESO OPCIONES REITERATIVAMENTE EL ACTUALIZAR ANDA MAL
