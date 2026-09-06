import instrucciones, seguridad, sala1, sala2


def main():

    usuario_inicial = "jugador1"
    contraseña_encriptada = "W6FGncdu?" #Contraseña encriptada con un corrimiento de 2 caracteres (U4DElabs=)

    print("\n----------------------------------------")
    print("Bienvenido al escape de prisión\n")

    seguridad.inicio_sesion(usuario_inicial, contraseña_encriptada)
    
    while True:
        print("Opciones: \n0- Instrucciones \n1- Jugar \n2- Cambiar contraseña \n3- Cerrar sesión")
        opcion = int(input("\nIngrese la opcion elejida: "))
        
        if opcion == 0 :
            instrucciones.mostrar()
            ###función instrucciones
        
        elif opcion == 1 :
            print("Elegiste la opcion de Jugar")
            resultado = sala1.sala1()
            if resultado == True:
                resultado = sala2.sala2()
            else:
                break

        elif opcion == 2 :
            print("Elegiste la opcion de Cambiar contraseña\n")
            contraseña_encriptada = seguridad.cambiar_contraseña(contraseña_encriptada)

        elif opcion == 3 :
            print("Saliendo...")
            ###terminar el programa
            break
            
        else :
            print("Opción invalida")
            ###ingrese otra opción, no se encunetra dentro de las disponibles
        
        
        
if __name__ == "__main__":
    main()
