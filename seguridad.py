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
