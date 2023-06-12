from Clase_usuario import *
from Clase_cancha import *
from Clase_reserva import *

"""CUANDO COMIENZA EL PROGRAMA, SE LEEN LAS BASES DE DATOS 
Y SE GUARDAN 3 DICCIONARIOS CON LOS USUARIOS (Y ADMINISTRADORES), LAS CANCHAS Y LAS RESERVAS.
CUANDO FINALIZA EL PROGRAMA, SE ACTUALIZAN LAS BASES DE DATOS"""

usuarios_guardados = Usuario.leer_usuarios("Usuarios.txt")
reservas_guardadas = Reserva.leer_reservas("Reservas.txt")
canchas_guardadas = Cancha.leer_canchas("Canchas.txt")

def menuPrincipal():    
    """ES EL MENU PRINCIPAL DE PROGRAMA (DONDE SE INICIA SESION Y SE REGISTRAN TANTO USUARIOS COMO ADMINISTRADORES)"""
    while True:
        print("MENU PRINCIPAL")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Soy administrador \n4. Salir \nIngrese una opción: ")
        if menu == "1": 
            """SE REGISTRAN USUARIOS Y ADMINISTRADORES, LOS ADMINISTRADORES TIENEN USUARIO: "admin" Y CONTRASEÑA ÚNICA"""
            user = Usuario()
            user.registrar_usuario(usuarios_guardados)
                
        elif menu == "2":    
            """SE INICIA SESION COMO USUARIO""" 
            usuario = input("Ingrese su usuario: ")    
            contraseña = input("Ingrese su contraseña: ")
            Usuario.iniciar_sesion(usuarios_guardados, usuario, contraseña, menuUsuarios)
        
        elif menu == "3":  
            """SE INICIA SESION COMO ADMINISTRADOR"""
            contraseña = input("Ingrese su contraseña: ")
            Administrador.iniciar_sesion(usuarios_guardados, "admin", contraseña, menuAdmins)
            
        elif menu == "4":   
            """SE REESCRIBE LA BASE DE DATOS DE USUARIOS"""
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
        else: 
            print("Opcion no valida")

def menuUsuarios(user):    
    """ES EL MENU DE LOS USUARIOS (LO ACCEDEN SOLO AQUELLOS QUE INICIARON SESION COMO USUARIOS)"""
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Modificar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Modificar reserva \n7. Cancelar reserva \n8. Cerrar sesion \nIngrese una opción: ")
        if menu == "1":     
            """SE MUESTRAN LOS DATOS DEL USUARIO"""
            Usuario.ver_mis_datos(user,usuarios_guardados) 
            
        elif menu == "2":   
            """SE CAMBIAN LOS DATOS DEL USUARIO"""
            Usuario.cambiar_usuario(user,usuarios_guardados)
        
        elif menu == "3":   
            """SE ELIMINAN LOS DATOS DEL USUARIO"""
            Usuario.eliminar_usuario(user,usuarios_guardados)
            break
        
        elif menu == "4":   
            """SE MUESTRAN LAS RESERVAS DEL USUARIO"""
            Usuario.ver_mis_reservas(user,reservas_guardadas)
                
        elif menu == "5":   
            """SE REGISTRA UNA RESERVA DEL USUARIO"""
            Reserva.hacer_reserva(reservas_guardadas,canchas_guardadas,user)       
               
        elif menu == "6":  
            """SE MODIFICA UNA RESERVA DEL USUARIO"""
            Usuario.ver_mis_reservas(user, reservas_guardadas)
            codigo = input("Ingrese el codigo de la reserva a modificar: ")
            for reserva in reservas_guardadas.values():
                if str(reserva.codigo) == codigo:
                    Reserva.cambiar_reserva(reserva, reservas_guardadas, canchas_guardadas)
                    break
            else: 
                print("Error en el codigo ingresado")
        
        elif menu == "7":   
            """SE CANCELA UNA RESERVA DEL USUARIO"""
            Usuario.ver_mis_reservas(user, reservas_guardadas)
            Reserva.eliminar_reserva(reservas_guardadas)
            
        elif menu == "8":  
            """SE REESCRIBEN LAS BASES DE DATOS DE CANCHAS Y RESERVAS"""
            Reserva.reescribir_basereservas(reservas_guardadas,"Reservas.txt")
            Cancha.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            break
    
        else:
            print("Opcion no disponible")
           
def menuAdmins(admin):  
    """ES EL MENU DE LOS ADMINISTRADORES (SOLO TIENEN ACCESO AQUELLOS QUE INICIARON SESION COMO ADMINISTRADORES)"""
    while True:
        print("ADMINISTRACION")
        menu = input("1. Ver canchas\n2. Agregar cancha\n3. Modificar cancha\n4. Eliminar cancha\n5. Ver usuarios\n6. Ver reservas\n7. Ver mis datos\n8. Modificar mis datos\n9. Borrar mi cuenta\n10. Cerrar sesion \nIngrese una opción: ")
        if menu == "1":    
            """SE MUESTRAN LAS CANCHAS DEL CLUB"""
            Administrador.ver_datos(admin,canchas_guardadas)
            
        elif menu == "2":   
            """SE AGREGAN CANCHAS"""
            cancha = Cancha()
            cancha.agregar_cancha(canchas_guardadas)
            
        elif menu == "3":  
            """SE MODIFICAN CANCHAS"""
            Administrador.ver_datos(admin,canchas_guardadas)
            codigo = input("Ingrese el codigo de la cancha a modificar: ")
            cancha = Cancha.instanciar_cancha(canchas_guardadas,codigo)
            if cancha is not None:
                Cancha.cambiar_cancha(cancha, canchas_guardadas)
        
        elif menu == "4":   
            """SE ELIMINAN CANCHAS"""
            Administrador.ver_datos(admin,canchas_guardadas)
            Cancha.eliminar_cancha(canchas_guardadas)
        
        elif menu == "5":   
            """SE MUESTRAN LOS USUARIOS GUARDADOS EN LA BASE DE DATOS"""
            Administrador.ver_datos(admin,usuarios_guardados)    
        
        elif menu == "6":   
            """SE MUESTRAN LAS RESERVAS REALIZADAS POR LOS USUARIOS"""
            Administrador.ver_datos(admin,reservas_guardadas)
                  
        elif menu == "7":  
            """SE MUESTRAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.ver_mis_datos(admin,usuarios_guardados)
            
        elif menu == "8":  
            """SE CAMBIAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.cambiar_usuario(admin,usuarios_guardados)
        
        elif menu == "9":  
            """SE ELIMINAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.eliminar_usuario(admin,usuarios_guardados)
            break
            
        elif menu == "10":  
            """SE REESCRIBE LA BASE DE DATOS DE CANCHAS"""
            Cancha.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            break
        
        else: 
            print("Opcion no disponible") 

menuPrincipal()
""" PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO """