"""Objetivo
Para superar la segunda sala, el jugador deberá localizar y hundir una pequeña flota oculta.
El campo de batalla estará representado mediante una matriz de 5 × 5.
Generación de la flota
El tablero contendrá 3 barcos.
Cada barco ocupará una única posición de la matriz y sus coordenadas deberán generarse
aleatoriamente cada vez que comienza la sala.
La generación deberá respetar las siguientes reglas:
• los tres barcos deberán ocupar posiciones diferentes;
• dos barcos no podrán estar juntos;
• se considerarán juntos si se encuentran en posiciones consecutivas horizontal, vertical o
diagonalmente;
• las posiciones de los barcos deberán permanecer ocultas para el jugador.
Por lo tanto, no será suficiente con generar tres coordenadas aleatorias. El programa deberá
determinar si cada posición generada es válida antes de ubicar allí un barco.
Desarrollo del juego
El jugador dispondrá de una cantidad limitada de disparos, que deberá ser definida por el
equipo.
En cada turno deberá ingresar las coordenadas de la posición que desea atacar.
El programa deberá validar que:
• las coordenadas ingresadas sean válidas;
• correspondan a una posición existente dentro del tablero;
• la posición no haya sido atacada anteriormente.
Un ingreso inválido no deberá consumir un disparo.
Tampoco deberá permitirse disparar nuevamente sobre una posición que ya fue utilizada.
Resultado del disparo
Después de cada disparo, el programa deberá determinar si la posición seleccionada contiene
un barco.
Si contiene un barco deberá informar:
¡IMPACTO! Barco hundido.
Si no contiene un barco deberá informar:
AGUA
El tablero visible deberá actualizarse para identificar las posiciones que ya fueron exploradas.
Las posiciones de los barcos que todavía no hayan sido encontrados deberán permanecer
ocultas.
Después de cada jugada deberá informarse:
• cantidad de barcos hundidos;
• cantidad de barcos restantes;
• cantidad de disparos disponibles.
Finalización
El jugador superará la sala si consigue encontrar los 3 barcos antes de agotar sus disparos.
Si agota todos los disparos sin encontrar la flota completa, habrá perdido el desafío.
El equipo deberá definir el comportamiento del juego ante una derrota y aplicarlo
consistentemente."""

