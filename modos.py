import time
from variables import lista_barcos_jug, lista_barcos_cpu
from tablero import crear_tablero, limpiar_pantalla, colocar_barcos_jug, colocar_barcos_cpu, imprimir_tableros_lado_a_lado
from barcos import colocar_barcos_jugador, añadir_barcos_cpu
from disparo_bucle import bucle_juego

def modo_juego(tablero_jug, tablero_cpu):
    
    limpiar_pantalla()
    print("\n¿Qué modo de juego quieres jugar?")
    print("1: Modo DEMO - Puedes ver la posición de los barcos del rival")
    print("2: Modo NORMAL - Los barcos del rival permanecen ocultos")
    print("3: Modo DIFICIL - No verás los barcos del rival y disparará con un patrón optimizado")
    
    while True: #Comprobación de valores correctos para iniciar la función, la he reutilizado en las partes que requieren inputs del usuario
        try:
            seleccion = int(input("\n¿Qué modo eliges? (1/2/3): "))
            if seleccion == 3:
                print("\nEste modo se encuentra en un desarrollo temprano.")
                print("Mientras tanto, puedes disfrutar de una gran experiencia de juego\n en los otros 2 modos de juego disponibles en la versión 0.0.1.")
                # Volver a mostrar el menú de selección de modo si se elige el modo difícil
                return modo_juego(tablero_jug, tablero_cpu)  # Llamamos a modo_juego para volver a la selección de modo
            elif seleccion in [1, 2]:
                # Limpiar pantalla después de elegir el modo
                limpiar_pantalla()
                break
            print("Por favor, introduce 1 o 2 o 3.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    # Generar barcos para CPU
    print("\nColocando barcos aleatoriamente para la CPU...")
    añadir_barcos_cpu(tablero_cpu)
    colocar_barcos_cpu(tablero_cpu, lista_barcos_cpu)
    time.sleep(1)
    
    # Colocar barcos del jugador
    print("\nAhora es tu turno de colocar tus barcos:")
    colocar_barcos_jugador()
    colocar_barcos_jug(tablero_jug, lista_barcos_jug)
    
    # Preparar el juego
    print("\nPreparando el juego...")
    time.sleep(1)
    limpiar_pantalla()
    
    # Definir si se muestran los barcos del CPU según el modo elegido
    mostrar_barcos_cpu = (seleccion == 1)  # Solo en el Modo DEMO (1) se muestran los barcos del CPU
    
    # Mostrar tableros iniciales
    imprimir_tableros_lado_a_lado(tablero_jug, tablero_cpu, mostrar_barcos_cpu)
    input("\nPresiona Enter para comenzar...")
    
    # Iniciar bucle de juego
    bucle_juego(tablero_jug, tablero_cpu, lista_barcos_jug, lista_barcos_cpu, mostrar_barcos_cpu)