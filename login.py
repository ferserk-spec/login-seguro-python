import getpass
nombre_usuario = "python2026" 
contraseña_usuario = "2026"
name = "python2026"

intentos = 3

while intentos > 0:
    
    nombre = getpass.getpass("Ingrese su nombre: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    if  nombre_usuario == nombre and contraseña_usuario == contraseña:
       print(f"Hola Bienvenido {name} ")
       break

    else:
        intentos -= 1
        print(f"Te quedan {intentos} intentos, ingrese sus datos nuevamente")

    if intentos == 0: 
        print("No te quedan intentos, cuenta bloqueada")
        

        
    

   
