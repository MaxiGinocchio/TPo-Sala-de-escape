from random import choice
### Garcia Tomas - Saponaro Ignacio

def sala_1():
    print("""
============================================================
                       SALA 1
                 EL MENSAJE OCULTO
============================================================

Después de varios meses encerrado en Alcatraz, comenzaste a observar
cada detalle de tu celda buscando una posible forma de escapar.

Una noche, mientras revisabas una grieta detrás de tu cama,
encontraste un pequeño papel escondido por un antiguo prisionero.

En el papel hay una palabra incompleta y una advertencia:

"Si lográs descubrir la palabra, encontrarás la pista necesaria
para salir de esta celda."

Pero no tenés demasiado tiempo.

Los guardias realizan sus recorridas constantemente y podrían
descubrirte en cualquier momento.

Tu objetivo será descubrir la palabra secreta ingresando una letra
por turno.

Cada letra correcta revelará parte del mensaje oculto.

Si ingresás una letra incorrecta, perderás uno de tus intentos.

Las letras repetidas o los ingresos inválidos no consumirán intentos.

Si lográs completar la palabra antes de quedarte sin intentos,
descubrirás cómo abrir la salida de tu celda y podrás continuar
con tu fuga.

Si agotás todos tus intentos, los guardias descubrirán tu plan
y el intento de escape habrá terminado.

============================================================
                 COMIENZA EL AHORCADO
============================================================
""")
while True:
    seguir = input("¿Comenzamos? Y / N: ")

    if seguir == "Y":
        print("inicia")
        break
    else:
        break  
                 
                 

palabras = [
    "CELDA",
    "PRISION",
    "GUARDIA",
    "ESCAPE",
    "ALCATRAZ",
    "REJA",
    "LLAVE",
    "TUNEL",
    "PATIO",
    "ALARMA"
]

palabra_secreta = choice(palabras)

palabra_oculta = "_ " * len(palabra_secreta)
letra_en_palabra = []

intentos = 4
letras_usadas = []

while intentos > 0 and "_ " in palabra_oculta:

    letra = input("Ingrese una letra para completar la palabra: ").upper()

    # Validar que sea una sola letra
    if len(letra) != 1 or not letra.isalpha():
        print("Debe ingresar solamente una letra.")
        continue

    # Validar que no esté repetida
    if letra in letras_usadas:
        print("Esa letra ya fue ingresada.")
        continue

    letras_usadas.append(letra)

    # Si la letra está en la palabra
    if letra in palabra_secreta:
        print("¡Letra correcta!")

        palabra_oculta = ""

        for letra_palabra in palabra_secreta:
            if letra_palabra in letras_usadas:
                palabra_oculta += letra_palabra + " "
            else:
                palabra_oculta += "_ "

    # Si la letra NO está
    else:
        intentos -= 1
        print("Letra incorrecta.")
        print("Intentos restantes:", intentos)

    print("Palabra:", palabra_oculta)
    print("Letras utilizadas:", letras_usadas)


if "_ " not in palabra_oculta:
    print("¡Ganaste!")
    print("La palabra era:", palabra_secreta)
else:
    print("Perdiste.")
    print("La palabra era:", palabra_secreta)
    