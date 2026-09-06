### Garcia Tomas - Saponaro Ignacio

import instrucciones, seguridad, sala1, sala2


def main():
    print("\n----------------------------------------")
    print("Bienvenido al escape de prisión\n")
    
    while True:
        print("Opciones: 0- Instrucciones / 1- Jugar / 2- Cambiar contraseña / 3- Cerrar sesión")
        opcion = int(input("Ingrese la opcion elejida: "))
        
        if opcion == 0 :
            instrucciones.mostrar()
            ###función instrucciones
        
        elif opcion == 1 :
            print("Elegiste la opcion de Jugar")
            ###función jugar
        elif opcion == 2 :
            print("Elegiste la opcion de Cambiar contraseña")
            ###función cambiar_contraseña
        elif opcion == 3 :
            print("Saliendo...")
            ###terminar el programa
            break
            
        else :
            print("Opción invalida")
            ###ingrese otra opción, no se encunetra dentro de las disponibles
        
        
        
if __name__ == "__main__":
    main()
