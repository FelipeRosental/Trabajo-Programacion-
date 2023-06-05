from clases import * ### CLASES

### CUANDO COMIENZA EL PROGRAMA, SE LEEN LAS BASES DE DATOS:
usuarios_guardados = Usuario.leer_usuarios("Usuarios.txt")
reservas_guardadas = Reserva.leer_reservas("Reservas.txt")
canchas_guardadas = Cancha.leer_canchas("Canchas.txt")
### CUANDO FINALIZA, SE ACTUALIZAN

def menuPrincipal():
    while True:
        print("MENU PRINCIPAL")
        menu = input("1. Registrarse \n2. Iniciar sesión \n3. Soy administrador \n4. Salir \nIngrese una opción: ")
        if menu == "1":
            user = Usuario()
            user.registrar_usuario(usuarios_guardados)
                
        elif menu == "2":
            usuario = input("Ingrese su usuario: ")    
            contraseña = input("Ingrese su contraseña: ")
            Usuario.iniciar_sesion(usuarios_guardados, usuario, contraseña, menuUsuarios)
        
        elif menu == "3":       
            contraseña = input("Ingrese su contraseña: ")
            Administrador.iniciar_sesion(usuarios_guardados, "admin", contraseña, menuAdmins)
            
        elif menu == "4":
            Archivo.reescribir_baseusuarios(usuarios_guardados,"Usuarios.txt")
            break
        else: 
            print("Opcion no valida")

def menuUsuarios(user):
    while True:
        print("DATOS Y RESERVAS")
        menu = input("1. Ver mis datos \n2. Modificar mis datos \n3. Borrar mi cuenta \n4. Ver mis reservas \n5. Hacer reserva \n6. Modificar reserva \n7. Cancelar reserva \n8. Cerrar sesion \nIngrese una opción: ")
        if menu == "1": 
            print(user) 
            
        elif menu == "2": 
            Usuario.cambiar_usuario(user,usuarios_guardados)
        
        elif menu == "3":
            Usuario.eliminar_usuario(user,usuarios_guardados)
            break
        
        elif menu == "4":
            Usuario.ver_mis_reservas(user,reservas_guardadas)
        ### FALTARIA ENCONTRAR UNA FORMA DE QUE SI UN USUARIO NO TIENE RESERVAS, SALTE UN ERROR
                
        elif menu == "5": 
            codcancha = Reserva.elegir_cancha(canchas_guardadas)
            if codcancha is not None:
                reserva = Reserva(cliente=user.usuario,cancha=codcancha)
                Reserva.hacer_reserva(reserva,reservas_guardadas)
                print("Reserva realizada con exito")
            else: 
                print("Error")
                
        elif menu == "6":
            Usuario.ver_mis_reservas(user, reservas_guardadas)
            codigo = input("Ingrese el codigo de la reserva a modificar: ")
            for reserva in reservas_guardadas.values():
                if reserva.codigo == codigo:
                    reserva.cambiar_reserva(reservas_guardadas)
        
        elif menu == "7":
            Usuario.ver_mis_reservas(user, reservas_guardadas)
            Reserva.eliminar_reserva(reservas_guardadas)
            
        elif menu == "8":
            Archivo.reescribir_basereservas(reservas_guardadas,"Reservas.txt")
            Archivo.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            break
    
        else:
            print("Opcion no disponible")
           
def menuAdmins(admin):
    while True:
        print("ADMINISTRACION")
        menu = input("1. Ver canchas\n2. Agregar cancha\n3. Modificar cancha\n4. Eliminar cancha\n5. Ver usuarios\n6. Ver reservas\n7. Ver mis datos\n8. Modificar mis datos\n9. Borrar mi cuenta\n10. Salir \nIngrese una opción: ")
        if menu == "1":
            Administrador.ver_canchas(admin,canchas_guardadas)
            
        elif menu == "2":
            cancha = Cancha()
            cancha.agregar_cancha(canchas_guardadas)
            
        elif menu == "3":
            codigo = input("Ingrese el codigo de la cancha a modificar: ")
            cancha = Cancha.buscar_cancha(canchas_guardadas,codigo)
            if cancha is not None:
                cancha.cambiar_cancha(canchas_guardadas)
        
        elif menu == "4":
            Cancha.eliminar_cancha(canchas_guardadas)
        
        elif menu == "5":
            Administrador.ver_usuarios(admin,usuarios_guardados)    
        
        elif menu == "6": 
            Administrador.ver_reservas(admin,reservas_guardadas)
                  
        elif menu == "7": 
            print(admin) 
            
        elif menu == "8": 
            Administrador.cambiar_usuario(admin,usuarios_guardados)
        
        elif menu == "9":
            Administrador.eliminar_usuario(admin,usuarios_guardados)
            break
            
        elif menu == "10":
            Archivo.reescribir_basecanchas(canchas_guardadas,"Canchas.txt")
            break
        
        else: 
            print("Opcion no disponible") 
          
menuPrincipal()
   
### PARA CORRER EL PROGRAMA, EJECUTAR ESTE ARCHIVO 