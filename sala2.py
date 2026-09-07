from random import randint

FILAS = 5
COLUMNAS = 5
CANTIDAD_BARCOS = 3
DISPAROS_INICIALES = 20


def crear_tablero():
    """Devuelve una matriz de 5x5 llena de '~' (agua sin explorar)."""
    tablero = []
    for fila in range(FILAS):
        fila_nueva = []
        for columna in range(COLUMNAS):
            fila_nueva.append("~")
        tablero.append(fila_nueva)
    return tablero


def posicion_valida(barcos, fila, columna):
    """La posicion sirve si no hay otro barco pegado (ni en diagonal).
       Como la distancia 0 tambien entra, tampoco deja repetir posiciones."""
    for barco in barcos:
        if abs(barco[0] - fila) <= 1 and abs(barco[1] - columna) <= 1:
            return False
    return True


def generar_barcos():
    """Ubica los 3 barcos en posiciones aleatorias y separadas entre si."""
    barcos = []
    while len(barcos) < CANTIDAD_BARCOS:
        fila = randint(0, FILAS - 1)
        columna = randint(0, COLUMNAS - 1)
        if posicion_valida(barcos, fila, columna):
            barcos.append([fila, columna])
    return barcos


def mostrar_tablero(tablero):
    """Muestra el tablero visible. Los barcos no encontrados siguen ocultos."""
    print("\n    1   2   3   4   5")
    for fila in range(FILAS):
        linea = str(fila + 1) + " "
        for columna in range(COLUMNAS):
            linea += "  " + tablero[fila][columna] + " "
        print(linea)
    print("\n  ~ = sin explorar   O = agua   X = barco hundido")


def pedir_coordenada(mensaje, maximo):
    """Pide un numero entre 1 y el maximo. Si esta mal, vuelve a pedir."""
    while True:
        valor = input(mensaje)
        if not valor.isdigit():
            print("Debe ingresar un numero.")
            continue
        valor = int(valor)
        if valor < 1 or valor > maximo:
            print("La coordenada esta fuera del tablero (1 a", str(maximo) + ").")
            continue
        return valor - 1


def sala2():
    def sala2():
    print("""
============================================================
                       SALA 2
                    BATALLA NAVAL
============================================================

Lograste salir de tu celda y llegaste hasta el muelle de
la prisión donde hay una lancha y un cañón. Sabés que en 
el mar hay tres botes policiales buscandote.

La niebla no te deja ver nada, asi que vas a tener que buscarlos
a ciegas sobre el sector, dividido en una cuadricula de 5 x 5.

En cada turno vas a elegir una fila y una columna. Si acertas,
encontraste uno de los botes. Si no, solamente encontras agua.

Tenes """ + str(DISPAROS_INICIALES) + """ balas de cañón para 
encontrar los 3 botes. Si se te acaban, los guardias van a 
llegar antes de que puedas escapar.

============================================================
                COMIENZA LA BATALLA NAVAL
============================================================
    """)

    tablero = crear_tablero()
    barcos = generar_barcos()
    disparos = DISPAROS_INICIALES
    hundidos = 0

    while disparos > 0 and hundidos < CANTIDAD_BARCOS:
        mostrar_tablero(tablero)
        print("\nDisparos disponibles:", disparos)

        fila = pedir_coordenada("Ingrese la fila (1 a 5): ", FILAS)
        columna = pedir_coordenada("Ingrese la columna (1 a 5): ", COLUMNAS)

        # Si la posicion ya fue atacada no se descuenta el disparo
        if tablero[fila][columna] != "~":
            print("Esa posicion ya fue atacada. Elegi otra.")
            continue

        disparos -= 1

        if [fila, columna] in barcos:
            tablero[fila][columna] = "X"
            hundidos += 1
            print("\n¡IMPACTO! Barco hundido.")
        else:
            tablero[fila][columna] = "O"
            print("\nAGUA")

        print("Barcos hundidos:", hundidos)
        print("Barcos restantes:", CANTIDAD_BARCOS - hundidos)
        print("Disparos disponibles:", disparos)

    mostrar_tablero(tablero)

    if hundidos == CANTIDAD_BARCOS:
        print("""
    ============================================================
    Encontraste los tres botes. Ya podés subir a la lancha e
    irte de la prisión.

                    ¡ESCAPASTE DE ALCATRAZ!
    ============================================================
    """)
        return True
    else:
        print("""
    ============================================================
    Se te acabaron las balas. Los guardias detectaron tu 
    posición y te atraparon.

                           GAME OVER
    ============================================================
    """)


if __name__ == "__main__":
    sala2()
