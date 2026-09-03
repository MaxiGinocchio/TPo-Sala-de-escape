"""TPo Programación 1 - Escape de prisión de Alcatraz"""
print("Integrantes: Ignacio Saponaro, Tomás García, Lautaro Denis, Máximo Ginocchio")


def inicio_sesion(usuario_inicial, contraseña_inicial):
    while True:
        usuario_ingresado = input("Ingrese su usuario: ")
        contraseña_ingresada = input("Ingrese su contraseña: ")
        contraseña_ingresada = encriptar(contraseña_ingresada)

        if usuario_ingresado == usuario_inicial and contraseña_ingresada == contraseña_inicial:
            print("Inicio de sesión exitoso. ¡Bienvenido al juego!\n")
            break
        if usuario_ingresado != usuario_inicial:
            print("Usuario incorrecto. Intente nuevamente.")
        if contraseña_ingresada != contraseña_inicial:
            print("Contraseña incorrecta. Intente nuevamente.")


def encriptar(contraseña, corrimiento=2):
    return ''.join(chr(ord(c) + corrimiento) for c in contraseña)


def cambiar_contraseña(contraseña_encriptada):
    while True:
        contraseña_actual = input("Ingrese su contraseña actual: ")
        contraseña_actual = encriptar(contraseña_actual)
        nueva_contraseña = input("Ingrese su nueva contraseña: ")
        nueva_contraseña = validar_contraseña(nueva_contraseña, contraseña_encriptada)
        if nueva_contraseña:
            return nueva_contraseña


def validar_contraseña(contraseña, contraseña_encriptada):
def validar_contraseña(contraseña, contraseña_encriptada):
    if contraseña != contraseña_encriptada:
        print("La nueva contraseña no puede ser igual a la anterior.")
    if len(contraseña) < 8:
        print("La nueva contraseña debe tener al menos 8 caracteres.")
    if not any(i.isdigit() for i in contraseña):
        print("La nueva contraseña debe contener al menos un número.")
    if not any(i.isupper() for i in contraseña):
        print("La nueva contraseña debe contener al menos una letra mayúscula.")
    if not any(i.islower() for i in contraseña):
        print("La nueva contraseña debe contener al menos una letra minúscula.")
    if not any(i in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for i in contraseña):
        print("La nueva contraseña debe contener al menos un carácter especial.")
    if any(i.isspace() for i in contraseña):
        print("La nueva contraseña no puede contener espacios.")
    else:
        print("Contraseña cambiada exitosamente.")
        contraseña = encriptar(contraseña)
        return contraseña

def main():
    print("----------------------------------------------------------------")
    print("Bienvenido al juego Escape de prisión de Alcatraz\n")


    usuario_inicial = "jugador1"
    contraseña_encriptada = "W6FGncdu?" #Contraseña encriptada con un corrimiento de 2 caracteres (U4DElabs=)

    inicio_sesion(usuario_inicial, contraseña_encriptada)

    contraseña_encriptada = cambiar_contraseña(contraseña_encriptada)



if __name__ == "__main__": 
    main()
