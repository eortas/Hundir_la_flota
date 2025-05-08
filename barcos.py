import random
from variables import lista_barcos_jug, lista_barcos_cpu, barcos_jugador
from tablero import imprimir_tablero_con_coordenadas_jug, colocar_barcos_jug

def barco_4():
    # Utilizaré esta función como modelo para el resto de funciones de barcos
    print("Comienza colocando un barco de eslora 4")
    print("Debes elegir el punto inicial (X, Y).")
    print("Sentido horizontal: de izquierda a derecha")
    print("Sentido vertical: de arriba hacia abajo")
    
    while True:
        orientacion = input("¿Horizontal o vertical? (h/v): ").lower()
        try:
            x = int(input("Introduce el punto inicial X (0-9): "))
            y = int(input("Introduce el punto inicial Y (0-9): "))
        except ValueError:
            print("Debes introducir un número válido. Inténtalo de nuevo.")
            continue

        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("Las coordenadas deben estar entre 0 y 9")
            continue

        if orientacion == "h":
            if x > 6:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x + i, y) for i in range(4)]
        elif orientacion == "v":
            if y > 6:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x, y + i) for i in range(4)]
        else:
            print("Orientación no válida. Usa 'h' o 'v'.")
            continue
        lista_barcos_jug.extend(posiciones)
        return posiciones

def verificar_colindancia(posiciones_nuevas):
    
    for (x, y) in posiciones_nuevas:
        # Revisa las 8 posiciones adyacentes (en los ejes X y Y)
        for dx in range(-1, 2):  # Esto cubre el rango -1, 0, 1 para el eje X
            for dy in range(-1, 2):  # Esto cubre el rango -1, 0, 1 para el eje Y
                if dx == 0 and dy == 0:
                    continue  
                x_adyacente = x + dx
                y_adyacente = y + dy

                # Verificar si la celda adyacente está dentro de los límites
                if 0 <= x_adyacente < 10 and 0 <= y_adyacente < 10:
                    if (x_adyacente, y_adyacente) in lista_barcos_jug:
                        return True  # Si la celda adyacente ya está ocupada, hay colindancia

    return False  # No hay colindancia

def barco_3():
    
    print("Coloca un barco de eslora 3")
    print("Debes elegir el punto inicial (X, Y).")
    
    while True:
        orientacion = input("¿Horizontal o vertical? (h/v): ").lower()
        try:
            x = int(input("Introduce el punto inicial X (0-9): "))
            y = int(input("Introduce el punto inicial Y (0-9): "))
        except ValueError:
            print("Debes introducir un número válido. Inténtalo de nuevo.")
            continue

        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("Las coordenadas deben estar entre 0 y 9")
            continue

        if orientacion == "h":
            if x > 7:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x + i, y) for i in range(3)]
        elif orientacion == "v":
            if y > 7:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x, y + i) for i in range(3)]
        else:
            print("Orientación no válida. Usa 'h' o 'v'.")
            continue
        #Estos barcos los colocaré después del de eslora 4 por eso necesita llamar a la función de verificar solapamiento/adyacencia
        if not verificar_colindancia(posiciones):
            lista_barcos_jug.extend(posiciones)
            return posiciones
        else:
            print("El barco es colindante con otro. Elige otra posición.")

def barco_2():
    
    print("Coloca un barco de eslora 2")
    print("Debes elegir el punto inicial (X, Y).")
    
    while True:
        orientacion = input("¿Horizontal o vertical? (h/v): ").lower()
        try:
            x = int(input("Introduce el punto inicial X (0-9): "))
            y = int(input("Introduce el punto inicial Y (0-9): "))
        except ValueError:
            print("Debes introducir un número válido. Inténtalo de nuevo.")
            continue

        if not (0 <= x <= 9 and 0 <= y <= 9):
            print("Las coordenadas deben estar entre 0 y 9")
            continue

        if orientacion == "h":
            if x > 8:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x + i, y) for i in range(2)]
        elif orientacion == "v":
            if y > 8:  # Validar que el barco no se salga del tablero
                print("El barco se saldría del tablero. Inténtalo de nuevo.")
                continue
            posiciones = [(x, y + i) for i in range(2)]
        else:
            print("Orientación no válida. Usa 'h' o 'v'.")
            continue
        #Estos barcos los colocaré después del de eslora 4 por eso necesita llamar a la función de verificar solapamiento/adyacencia
        if not verificar_colindancia(posiciones):
            lista_barcos_jug.extend(posiciones)
            return posiciones
        else:
            print("El barco es colindante con otro. Elige otra posición.")

def barco_4_cpu(tablero_cpu):
    # Sigue el mismo esquema usado par jugador pero cambiando los inputs por coordenadas aleatorias.
    while True:
        orientacion_cpu = random.randint(0, 1)
        barco_x_cpu = random.randint(0, 9)
        barco_y_cpu = random.randint(0, 9)
        
        if orientacion_cpu == 0:  # Horizontal
            if barco_x_cpu > 6:
                continue
            posiciones_cpu = [(barco_x_cpu + i, barco_y_cpu) for i in range(4)]
        else:  # Vertical
            if barco_y_cpu > 6:
                continue
            posiciones_cpu = [(barco_x_cpu, barco_y_cpu + i) for i in range(4)]
        
        if verificar_colindancia_cpu(posiciones_cpu):
            continue

        lista_barcos_cpu.extend(posiciones_cpu)
        break

def verificar_colindancia_cpu(posiciones_nuevas):
    
    for (x, y) in posiciones_nuevas:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                x_adyacente = x + dx
                y_adyacente = y + dy
                if 0 <= x_adyacente < 10 and 0 <= y_adyacente < 10:
                    if (x_adyacente, y_adyacente) in lista_barcos_cpu:
                        return True
    return False

def barco_3_cpu(tablero_cpu):
    
    while True:
        orientacion_cpu = random.randint(0, 1)
        
        barco_x_cpu = random.randint(0, 9) 
        barco_y_cpu = random.randint(0, 9) 
        
        if orientacion_cpu == 0:  # Horizontal
            if barco_x_cpu > 7:  # Validar que el barco no se salga del tablero
                continue
            posiciones_cpu = [(barco_x_cpu + i, barco_y_cpu) for i in range(3)]
        else:  # Vertical (orientacion_cpu == 1)
            if barco_y_cpu > 7:  # Validar que el barco no se salga del tablero
                continue
            posiciones_cpu = [(barco_y_cpu, barco_y_cpu + i) for i in range(3)]

        # Verificar colindancia
        if verificar_colindancia_cpu(posiciones_cpu):
            continue

        # Si no hay colindancia, se colocan las posiciones
        lista_barcos_cpu.extend(posiciones_cpu)
        break

def barco_2_cpu(tablero_cpu):
    
    while True:
        orientacion_cpu = random.randint(0, 1)
        
        barco_x_cpu = random.randint(0, 9) 
        barco_y_cpu = random.randint(0, 9) 
        
        if orientacion_cpu == 0:  # Horizontal
            if barco_x_cpu > 8:  # Validar que el barco no se salga del tablero
                continue
            posiciones_cpu = [(barco_x_cpu + i, barco_y_cpu) for i in range(2)]
        else:  # Vertical (orientacion_cpu == 1)
            if barco_y_cpu > 8:  # Validar que el barco no se salga del tablero
                continue
            posiciones_cpu = [(barco_x_cpu, barco_y_cpu + i) for i in range(2)]

        # Verificar colindancia
        if verificar_colindancia_cpu(posiciones_cpu):
            continue

        # Si no hay colindancia, se colocan las posiciones
        lista_barcos_cpu.extend(posiciones_cpu)
        break

def colocar_barcos_jugador():
    
    from tablero import crear_tablero  # Necesito importar aquí porque originalmente lo tenía en el main.py pero por limpiarlo al máximo...
    tablero_jug = crear_tablero()
    
    imprimir_tablero_con_coordenadas_jug(tablero_jug)
    # Barco de eslora 4
    pos_barco = barco_4()
    barcos_jugador.append(pos_barco)  # Guardar posiciones del barco en la lista, que nos servirá para marcar los barcos en el tablero
    colocar_barcos_jug(tablero_jug, lista_barcos_jug)
    print("\nEste es tu tablero después de colocar el barco de eslora 4:")
    imprimir_tablero_con_coordenadas_jug(tablero_jug)
    
    # Barcos de eslora 3
    for i in range(2):
        
        pos_barco = barco_3()
        barcos_jugador.append(pos_barco)  # Guardar posiciones del barco
        colocar_barcos_jug(tablero_jug, lista_barcos_jug)
        print(f"\nEste es tu tablero después de colocar el barco de eslora 3 #{i+1}:")
        imprimir_tablero_con_coordenadas_jug(tablero_jug)
    
    # Barcos de eslora 2
    for i in range(3):
        
        pos_barco = barco_2()
        barcos_jugador.append(pos_barco)  # Guardar posiciones del barco
        colocar_barcos_jug(tablero_jug, lista_barcos_jug)
        print(f"\nEste es tu tablero después de colocar el barco de eslora 2 #{i+1}:")
        imprimir_tablero_con_coordenadas_jug(tablero_jug)
    
    print("¡Bien hecho! Has colocado todos tus barcos.")
    return tablero_jug

def añadir_barcos_cpu(tablero_cpu):
    
    # 1 barco de eslora 4
    barco_4_cpu(tablero_cpu)
    
    # 2 barcos de eslora 3
    for _ in range(2):
        barco_3_cpu(tablero_cpu)
    
    # 3 barcos de eslora 2
    for _ in range(3):
        barco_2_cpu(tablero_cpu)