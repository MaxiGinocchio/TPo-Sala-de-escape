### Garcia Tomas - Saponaro Ignacio

import instrucciones
while True:
    print(" elija alguna de estas opciones : 0-Instrucciones / 1-Jugar / 2-cambiar_contraseña / 3-cerrar_sesion")
    opcion = int(input("ingrese la opcion elejida :"))
    
    if opcion == 0 :
        instrucciones.mostrar()
        ###funcion instrucciones
    
    elif opcion == 1 :
        print("elegiste la opcion de Jugar")
        ###funcion jugar
    elif opcion == 2 :
        print("elegiste la opcion de Cambiar_contraseña")
        ###funcion cambiar-contrasenas
    elif opcion == 3 :
        print("saliendo...")
        ###funcion saliendo
        break
        
    else :
        print("opcion invalida")
        ###ingrese otra opcion, no se encunetra dentro de las disponibles
        
        
        
