import random
import time
from tablero import limpiar_pantalla, imprimir_tableros_lado_a_lado

def disparo_jugador(tablero_cpu, disparos_jugador):
    
    while True: #Bucle ya usado antes para validar los datos de entrada
        try:
            x = int(input("Introduce la coordenada X del disparo (0-9): "))
            y = int(input("Introduce la coordenada Y del disparo (0-9): "))
            coordenadas = (x, y) # Guardamos los inputs en una variable para comprobar los datos
        except ValueError:
            print("Coordenadas inválidas. Deben ser números.")
            continue
        # Condiciones para los valores dentro del tablero
        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("Coordenadas fuera de rango. Intenta de nuevo.")
            continue
        # Evita que dispares dos veces a la misma celda
        if coordenadas in disparos_jugador:
            print("Ya disparaste ahí. Elige otra posición.")
            continue

        disparos_jugador.append(coordenadas)

        celda = tablero_cpu[y][x]

        if celda == "O":
            print("¡Impacto!")
            tablero_cpu[y][x] = "X"
            return True
        else:
            print("Agua...")
            tablero_cpu[y][x] = "•"
            return False


def disparo_cpu(tablero_jugador, disparos_cpu):
    # Función adaptada de jugador para que dispare la CPU aleatoriamente
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if (x, y) in disparos_cpu:
            continue

        disparos_cpu.append((x, y))
        celda = tablero_jugador[y][x]

        print(f"El CPU dispara a ({x}, {y})")

        time.sleep(1)

        if celda == "O":
            print("Ha alcanzado un barco")
            tablero_jugador[y][x] = "X"
            return True  # Acierto
        elif celda == "~":
            print("Ha fallado")
            tablero_jugador[y][x] = "•"
            return False  # Fallo
        break


def bucle_juego(tablero_jugador, tablero_cpu, lista_barcos_jug, lista_barcos_cpu, mostrar_barcos_cpu=True):
    # Bucle principal de juego
    disparos_jugador = [] # Creamos 2 listas vacías para guardar los disparos, una para el jugador
    disparos_cpu = []     # la otra para la CPU

    while True:
        limpiar_pantalla()
        print("\n---- Turno del jugador ----")
        imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, mostrar_barcos_cpu)
        
        # Bucle para continuar disparando hasta fallar
        acierto = True
        while acierto:
            acierto = disparo_jugador(tablero_cpu, disparos_jugador)

            if verificar_ganador(tablero_cpu):
                limpiar_pantalla()
                imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, True)
                print(r""" 
  _    _                                          _       _ 
| |  | |                                         | |     | |
| |__| | __ _ ___    __ _  __ _ _ __   __ _  _ __| | ___ | |
|  __  |/ _` / __|  / _` |/ _` | '_ \ / _` |/ _` | |/ _ \| |
| |  | | (_| \__ \ | (_| | (_| | | | | (_| | (_| | | (_) |_|
|_|  |_|\__,_|___/  \__, |\__,_|_| |_|\__,_|\__,_|_|\___/(_)
                     __/ |                                  
                    |___/                                                  
""")  
                print(f"\nHas ganado!\nHas ganado en {len(disparos_jugador)} disparos.\nTu tasa de acierto es {tasa_acierto_final(disparos_jugador)}")
                return  # Termina el juego

            if acierto:
                print("\n¡Buen disparo! Vuelves a disparar.") # Ahora bajando una posición el bucle funciona bien para
                                                              # el último barco
                imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, mostrar_barcos_cpu)
            else:
                break  # Fallo, fin del turno
            

        input("\nPresiona Enter para continuar...")
        limpiar_pantalla()
        
        print("\n--- Turno del CPU ---")
        imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, mostrar_barcos_cpu)
        
        # La CPU dispara hasta que falle, mismo código que para el jugador
        acierto = True
        while acierto:
            acierto = disparo_cpu(tablero_jugador, disparos_cpu)
            
            # Verificar si la CPU ha ganado
            if verificar_ganador(tablero_jugador):
                limpiar_pantalla()
                imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, True)
                print(r"""
  _    _                                       _       _ 
 | |  | |                              | (_)  | |     | |
 | |__| | __ _ ___   _ __   ___ _ __ __|     _| | ___ | |
 |  __  |/ _` / __| | '_ \ / _ \ '__|/ _` | / _` | _ \| |
 | |  | | (_| \__ \ | |_) |  __/ |  | (_| | (_| | (_) |_|
 |_|  |_|\__,_|___/ | .__/ \___|_|   \__,_|\__,_|\___/(_)
                    | |                                   
                    |_|                                   
""")
                print(f"\nHas perdido!\nHas perdido en {len(disparos_cpu)} disparos.\nLa tasa de acierto de la CPU es {tasa_acierto_final_cpu(disparos_jugador)}")
                return
            
            if acierto:
                print("\nLa CPU ha acertado! Vuelve a disparar.")
                imprimir_tableros_lado_a_lado(tablero_jugador, tablero_cpu, mostrar_barcos_cpu)
        
        input("\nPresiona Enter para continuar...")

def verificar_ganador(tablero):
    # Función que llamaremos dentro de los disparos para comprobar si ya no quedan O en el tablero
    # Si ya no hay 'O' (barcos) en el tablero, alguien ha ganado
    for fila in tablero:
        if "O" in fila:
            return False
    return True

def tasa_acierto_final(disparos_jugador): #Pequeña información de aciertos del jugador que se muestra al finalizar
    if len(disparos_jugador) == 0:
        return 0.0
    tasa = 16 / len(disparos_jugador) * 100
    return round(tasa, 2)

def tasa_acierto_final_cpu(disparos_cpu): #Pequeña información de aciertos del jugador que se muestra al finalizar
    if len(disparos_cpu) == 0:
        return 0.0
    tasa = 16 / len(disparos_cpu) * 100
    return round(tasa, 2)