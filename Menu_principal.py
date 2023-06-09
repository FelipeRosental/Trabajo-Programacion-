from Clase_club import *

"""CUANDO COMIENZA EL PROGRAMA, SE LEEN LAS BASES DE DATOS 
Y SE GUARDAN 3 DICCIONARIOS CON LOS USUARIOS (Y ADMINISTRADORES), LAS CANCHAS Y LAS RESERVAS.
CUANDO FINALIZA EL PROGRAMA, SE ACTUALIZAN LAS BASES DE DATOS"""

club = Club("ITBA", "Lavardén 315", "10:00 a 18:00")

usuarios_guardados = club.usuarios_y_admins
reservas_guardadas = club.reservas
canchas_guardadas = club.canchas

def menu_Principal():    
    """input: nada\n
    funcion: ES EL MENU PRINCIPAL DEL PROGRAMA (DONDE SE INICIA SESION Y SE REGISTRAN TANTO USUARIOS COMO ADMINISTRADORES), 
    DE ESTE MENU SE REDIRIGE AL USUARIO A OTRO MENU QUE VARIA SEGUN SI EL QUE INICIÓ SESION ES UN USUARIO O UN ADMINISTRADOR\n
    output: nada"""
    while True:
        print("MENU PRINCIPAL")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Soy administrador \n4. Sobre el club \n5. Salir \nIngrese una opción: ")
        if menu == "1": 
            """SE REGISTRAN USUARIOS Y ADMINISTRADORES, LOS ADMINISTRADORES TIENEN USUARIO: "admin" Y CONTRASEÑA ÚNICA"""
            user = Usuario()
            Usuario.registrar_usuario(user, usuarios_guardados)
                
        elif menu == "2":    
            """SE INICIA SESION COMO USUARIO""" 
            usuario = input("Ingrese su usuario: ")   
            if usuario == "admin":
                es_admin =  input("Es usted un administrador (si/no) ? ")
                if es_admin in ["si", "Si", "SI"]:
                    contraseña = input("Ingrese su contraseña: ")
                    Administrador.iniciar_sesion(usuarios_guardados, "admin", contraseña, menu_Admins)
                else:
                    print("Entonces no puede tener usuario: admin")
            else:
                contraseña = input("Ingrese su contraseña: ")
                Usuario.iniciar_sesion(usuarios_guardados, usuario, contraseña, menu_Usuarios)
        
        elif menu == "3":  
            """SE INICIA SESION COMO ADMINISTRADOR"""
            contraseña = input("Ingrese su contraseña: ")
            Administrador.iniciar_sesion(usuarios_guardados, "admin", contraseña, menu_Admins)
        
        elif menu == "4":
            """SE MUESTRAN LOS DATOS DEL CLUB"""
            print(club)
            
        elif menu == "5":
            """SE REESCRIBE LA BASE USUARIOS Y SALE DEL PROGRAMA"""   
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
        
        else: 
            print("Opcion no valida")

def menu_Usuarios(user):    
    """input: objeto user (usuario que inició sesión)\n
    funcion: ES EL MENU DE LOS USUARIOS (LO ACCEDEN SOLO AQUELLOS QUE INICIARON SESION COMO USUARIOS)\n
    output: nada"""
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
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
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
            """SE REESCRIBEN LAS BASES DE DATOS DE CANCHAS, RESERVAS Y USUARIOS. LUEGO SE CIERRA LA SESION DEL USUARIO"""
            Reserva.reescribir_basereservas(reservas_guardadas,"Reservas.txt")
            Cancha.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
    
        else:
            print("Opcion no disponible")
           
def menu_Admins(admin):  
    """input: objeto admin (administrador que inició sesion)\n
    ES EL MENU DE LOS ADMINISTRADORES (SOLO TIENEN ACCESO AQUELLOS QUE INICIARON SESION COMO ADMINISTRADORES)\n
    output: nada"""
    while True:
        print("ADMINISTRACION")
        menu = input("1. Ver canchas\n2. Agregar cancha\n3. Modificar cancha\n4. Eliminar cancha\n5. Ver usuarios\n6. Ver reservas\n7. Ver ingresos del club\n8. Ver mis datos\n9. Modificar mis datos\n10. Borrar mi cuenta\n11. Cerrar sesion \nIngrese una opción: ")
        if menu == "1":    
            """SE MUESTRAN LAS CANCHAS DEL CLUB"""
            Administrador.ver_datos(canchas_guardadas)
            
        elif menu == "2":   
            """SE AGREGAN CANCHAS"""
            cancha = Cancha()
            cancha.agregar_cancha(canchas_guardadas)
            
        elif menu == "3":  
            """SE MODIFICAN CANCHAS"""
            Administrador.ver_datos(canchas_guardadas)
            codigo = input("Ingrese el codigo de la cancha a modificar: ")
            cancha = Cancha.buscar_cancha(canchas_guardadas,codigo)
            if cancha is not None:
                Cancha.cambiar_cancha(cancha, canchas_guardadas)
        
        elif menu == "4":   
            """SE ELIMINAN CANCHAS"""
            Administrador.ver_datos(canchas_guardadas)
            Cancha.eliminar_cancha(canchas_guardadas)
        
        elif menu == "5":   
            """SE MUESTRAN LOS USUARIOS GUARDADOS EN LA BASE DE DATOS"""
            Administrador.ver_datos(usuarios_guardados)    
        
        elif menu == "6":   
            """SE MUESTRAN LAS RESERVAS REALIZADAS POR LOS USUARIOS"""
            Administrador.ver_datos(reservas_guardadas)
                  
        elif menu == "7": 
            """SE MUESTRAN LOS INGRESOS DEL CLUB"""
            Club.ver_ingresos_del_mes(club)
        
        elif menu == "8":  
            """SE MUESTRAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.ver_mis_datos(admin,usuarios_guardados)
            
        elif menu == "9":  
            """SE CAMBIAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.cambiar_usuario(admin,usuarios_guardados)
        
        elif menu == "10":  
            """SE ELIMINAN LOS DATOS DEL ADMINISTRADOR"""
            Administrador.eliminar_usuario(admin,usuarios_guardados)
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
            
        elif menu == "11":  
            """SE REESCRIBE LA BASE DE DATOS DE CANCHAS Y USUARIOS, LUEGO CIERRA LA SESION COMO ADMIN"""
            Cancha.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            Usuario.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
        
        else: 
            print("Opcion no disponible") 

menu_Principal()
""" PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO """