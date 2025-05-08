from tablero import obtener_tableros
from modos import modo_juego
tablero_jug, tablero_cpu = obtener_tableros()
modo_juego(tablero_jug, tablero_cpu)