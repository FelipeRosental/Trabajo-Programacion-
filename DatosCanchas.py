from random import *
from datetime import *
from string import *

from validaciones import * ### VALIDACIONES
from clases import * ### CLASES

def menuAdmins(admin):
    while True:
        print("ADMINISTRACION")
        menu = input("1. Ver canchas\n2. Agregar canchas\n3. Eliminar canchas\n4. Ver mis datos\n5. Cambiar mis datos\n6. Borrar mi cuenta\n7. Salir \nIngrese una opción: ")
        if menu == "1":
            Cancha.ver_canchas("Canchas.txt")
            
        elif menu == "2":
            cancha = Cancha()
            cancha.actualizar_canchas("Canchas.txt") 
            
        elif menu == "3":
            cancha = Cancha()
            cancha.eliminar_canchas("Canchas.txt")
        
        if menu == "4": 
            Usuario.ver_datos(admin.usuario,"Usuarios.txt")
        
        elif menu == "5": 
            admin.cambiar_usuario("Usuarios.txt")    
        
        elif menu == "6":
            admin.eliminar_usuario("Usuarios.txt") 
            break
        
        elif menu == "7":
            break
        else: 
            print("Opcion no disponible")
          

### NO FUNCIONA BIEN (CUANDO AGREGO UNA CANCHA QUE YA ESTÁ INGRESADA NO ME SALTA ERROR Y ME AGREGA CUALQUIER COSA)
### ADEMAS, CUANDO INGRESO OPCIONES REITERATIVAMENTE EL ACTUALIZAR ANDA MAL
