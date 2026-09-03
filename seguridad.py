def inicio_sesion(usuario_inicial, contraseña_inicial):
    while True:
        usuario_ingresado = input("Ingrese su usuario: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")
        contraseña_ingresada = comparar_contraseña(contraseña_ingresada, contraseña_inicial)

        if usuario_ingresado == usuario_inicial and contraseña_ingresada == True:
            print("Inicio de sesión exitoso. ¡Bienvenido al juego!\n")
            break
        if usuario_ingresado != usuario_inicial:
            print("Usuario incorrecto. Intente nuevamente.")


def comparar_contraseña(contraseña_ingresada, contraseña_encriptada):
    contraseña_ingresada = encriptar(contraseña_ingresada)
    if contraseña_ingresada == contraseña_encriptada:
        return True
    else:
        print("Contraseña incorrecta. Intente nuevamente.")
        
    
def encriptar(contraseña, corrimiento=2):
    return ''.join(chr(ord(c) + corrimiento) for c in contraseña)


def desencriptar(contraseña, corrimiento=-2):
    return ''.join(chr(ord(c) + corrimiento) for c in contraseña)


def cambiar_contraseña(contraseña_encriptada):
    print("\nLa nueva contraseña debe cumplir con los siguientes requisitos:")
    print("- Tener al menos 8 caracteres")
    print("- Contener al menos un número")
    print("- Contener al menos una letra mayúscula")
    print("- Contener al menos una letra minúscula")
    print("- Contener al menos un carácter especial")
    print("- No contener espacios\n")
    while True:
        contraseña_actual = input("Ingrese su contraseña actual: ")
        contraseña_actual = comparar_contraseña(contraseña_actual, contraseña_encriptada)
        while contraseña_actual != True:
            contraseña_actual = input("Ingrese su contraseña actual: ")
            contraseña_actual = comparar_contraseña(contraseña_actual, contraseña_encriptada)
        nueva_contraseña = input("Ingrese su nueva contraseña: ")
        nueva_contraseña = validar_contraseña(nueva_contraseña, contraseña_encriptada)
        while nueva_contraseña == None:
            nueva_contraseña = input("Ingrese su nueva contraseña: ")
            nueva_contraseña = validar_contraseña(nueva_contraseña, contraseña_encriptada)
        return nueva_contraseña


def validar_contraseña(contraseña, contraseña_encriptada):
    contraseña_encriptada = desencriptar(contraseña_encriptada)
    valida = True
    if contraseña == contraseña_encriptada:
        print("La nueva contraseña no puede ser igual a la anterior.")
        valida = False
    if len(contraseña) < 8:
        print("La nueva contraseña debe tener al menos 8 caracteres.")
        valida = False
    if not any(i.isdigit() for i in contraseña):
        print("La nueva contraseña debe contener al menos un número.")
        valida = False
    if not any(i.isupper() for i in contraseña):
        print("La nueva contraseña debe contener al menos una letra mayúscula.")
        valida = False
    if not any(i.islower() for i in contraseña):
        print("La nueva contraseña debe contener al menos una letra minúscula.")
        valida = False
    if not any(i in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for i in contraseña):
        print("La nueva contraseña debe contener al menos un carácter especial.")
        valida = False
    if any(i.isspace() for i in contraseña):
        print("La nueva contraseña no puede contener espacios.")
        valida = False
    if valida == True:
        print("\nContraseña cambiada exitosamente.")
        contraseña = encriptar(contraseña)
        return contraseña


usuario_inicial = "jugador1"
contraseña_encriptada = "W6FGncdu?" #Contraseña encriptada con un corrimiento de 2 caracteres (U4DElabs=)
inicio_sesion(usuario_inicial, contraseña_encriptada)
