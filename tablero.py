import numpy as np
import os

def crear_tablero():
    return np.full((10, 10), "~")  # ~ para representar el agua

def obtener_tableros():
    
    tablero_jug = crear_tablero()
    tablero_cpu = crear_tablero()
    return tablero_jug, tablero_cpu

def limpiar_pantalla():
    return os.system('cls')

def colocar_barcos_jug(tablero_jug, lista_barcos_jug):
    #Marca los barcos del jugador en el tablero de juego
    for (x, y) in lista_barcos_jug:
        tablero_jug[y][x] = "O"

def colocar_barcos_cpu(tablero_cpu, lista_barcos_cpu):
    #Marca los barcos del jugador en el tablero de juego, mientras lo comentaba podría haber
    #referenciado las dos funciones en una sola, la de jugador y la de cpu con un argumento más
    for (x, y) in lista_barcos_cpu:
        tablero_cpu[y][x] = "O"

def imprimir_tablero_con_coordenadas_jug(tablero):
    filas, columnas = tablero.shape #al principio solo había puesto que lo hiciera la iteracion por range 10
                                        #pero así es más escalable a futuro y más claro lo que hace el bucle.
    print(f"TABLERO JUGADOR")
    print("    " + " ".join(f"{i}" for i in range(columnas))) # Concatenamos los números de columnas con un espacio entre ellos
    print("    " + " ".join("↓" for _ in range(columnas)))
    for y in range(filas):
        fila = f"{y:1} | " + " ".join(tablero[y])
        print(fila)

def imprimir_tablero_con_coordenadas_cpu(tablero_cpu):
    # Lo mismo que con la función de los barcos, podría haber usado solo una pero me ha resultado más
    # sencillo y lógico de primeras reutilizar código que había probado que funciona.
    filas, columnas = tablero_cpu.shape 
    print(f"TABLERO CPU:")
    print("    " + " ".join(f"{i}" for i in range(columnas)))
    print("    " + " ".join("↓" for _ in range(columnas)))
    for y in range(filas):
        fila = f"{y:1} | " + " ".join(tablero_cpu[y])
        print(fila)

def imprimir_tablero_con_coordenadas_cpu_oculto(tablero_cpu):
    #Más tarde me di cuenta que podría haber resumido estas 4 funciones en una sola, solo pasandole 
    #argumentos
    filas, columnas = tablero_cpu.shape
    print("TABLERO CPU (solo se muestran disparos):")
    print("    " + " ".join(f"{i}" for i in range(columnas)))
    print("    " + " ".join("↓" for _ in range(columnas)))
    
    for y in range(filas):
        fila = f"{y:1} | "
        for x in range(columnas):
            celda = tablero_cpu[y][x]
            if celda == "X":  # si es un impacto se muestra como tal
                fila += "X "
            elif celda == "•":  # si es agua pues se muestra como agua
                fila += "• "
            else:
                fila += "~ "  # y si no es ni agua, ni impacto, entonces es un barco y lo cambia por el símbolo de agua 
                              # para enmascarar la posición del barco
        print(fila)

def imprimir_tableros_lado_a_lado(tablero_jug, tablero_cpu, mostrar_barcos_cpu=True): #La condición por defecto la dejo en True
                                                                                      #para jugar al modo demo, y False sería el modo Normal
    filas, columnas = tablero_jug.shape #Igual que antes para colocar los índices al tablero.
    print(" " * 6 + "TABLERO JUGADOR" + " " * 15 + "TABLERO CPU") #Aquí poco que explicar he ido probando hasta que han cuadrado los títulos
                                                                  #con los tableros
    
    # Encabezado columnas números y flechas
    encabezado = "    " + " ".join(f"{i}" for i in range(columnas))
    print(encabezado + "     " + encabezado)
    flechas = "    " + " ".join("↓" for _ in range(columnas))
    print(flechas + "     " + flechas)

    for y in range(filas):
        # Tablero del jugador
        fila_jug = f"{y:1} | " + " ".join(tablero_jug[y])
        fila_cpu = f"{y:1} | "
        for x in range(columnas):
            celda = tablero_cpu[y][x]
            if mostrar_barcos_cpu: #es un poco enrevesada la lógica pero ha funcionado
                fila_cpu += f"{celda} "
            else:
                if celda == "X":
                    fila_cpu += "X "
                elif celda == "•":
                    fila_cpu += "• "
                else:
                    fila_cpu += "~ "

        # Mostrar los dos tableros en la misma línea
        print(fila_jug + "     " + fila_cpu)