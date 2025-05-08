# Hundir la flota
Un juego simple funcionando en terminal basado en Hundir la flota, realizado con Python.

![PantallaCarga](https://github.com/user-attachments/assets/f3bbb110-bfa5-4881-9539-6ba7e33396d0)

> A simple terminal based battleship game made with Python.

## Tabla de contenidos
* [Información general](#general-info)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Programa mínimo](#features)
* [Estado](#status)
* [Contact](#contact)

## Información general
Este proyecto fue iniciado como un reto personal como mi primera aproximación a Python y con un tiempo para que fuera funcional de apenas 3 días a modo de desafío.

## Screenshots
![image](https://github.com/user-attachments/assets/da3fd16d-cb33-4450-86fa-61db30011fdc)

![image](https://github.com/user-attachments/assets/cb28a1fd-deda-4914-83ad-4ed37379f733)


## Setup
Guarda todos los archivos en la misma carpeta. Probado con Python 3.11.x . Para ejecutarlo, desde la carpeta donde guardaste los archivos ejecuta:
```console
    python juego.py
```

## Programa mínimo 
* Crear un tablero de 10x10 relleno del carácter "_" con numpy.
* Crear una serie de barcos generados de forma aleatoria (6 barcos en total (3 barcos de eslora 2, 2 de eslora 3 y 1 eslora 4)) 
  dos barcos la misma casilla) o barcos que se salgan del tablero!
* ¡Mucho ojo con barcos que estén superpuestos (no pueden ocupar la misma casilla)
* Crear la dinámica de turnos y funcionalidades necesarios para jugar contra la máquina que disparará a nuestro tablero de forma aleatoria.
* Informar de cuando un barco ha sido tocado, cambiando su representación en el tablero por una X, hacer lo mismo para cuando le das al agua sustituyendo por •.
* Terminar el juego cuando uno de los dos jugadores no tenga más barcos en pie.


## Mejoras añadidas
 * Se representan los tableros del jugador y del rival en la misma linea para mejorar la legibilidad.
 * Los tableros se han reducido a 2, pero con las funcionalidades de 4. En el primer tablero del jugador se mostrarán sus barcos y los disparos del rival. En el tablero, a la derecha del
   del jugador, se mostrarán los barcos enemigos que hayamos acertado así como todos los disparos fallidos.
 * Modo Demo, en este modo los barcos enemigos también se mostrarán, para que a efectos prácticos podamos terminar una partida rápidamente y comprobar como el código FLUYE.
 * Función de solapamiento mejorada. Tal como indican las reglas del juego los barcos no pueden ocupar posiciones que sean colindantes a otros barcos ya colocados. Se ha establecido esta mejora tanto para el jugador como para el ordenador.
 *  Todos los datos que se requiere que introduzca el jugador son validados impidiendo así que se introduzcan valores incorrectos.

Lista de mejoras pendientes de implementar:
* En cada turno se podría mostrar información sobre los barcos restantes del enemigo.
* Cambiar la representación de los barcos hundidos con flechas que indiquen su comienzo y final
Flecha arriba: ↑
Flecha abajo: ↓
Flecha izquierda: ←
Flecha derecha: →
Cuerpo vertical del barco: │
Cuerpo horizontal del barco: ─

Un barco horizontal de eslora 3 hundido quedaría representado así:
```console
    → - ←
```
Un barco vertical de eslora 2 hundido quedaría representado así:
```console
    ↓
    ↑
```
* Sistema de disparo del rival mejorado, cuando acierte a un barco que sus siguientes disparos sean en el eje x o y hasta que acierte.
* Sistema de disparo del rival aún más optimizado, barrer el tablero en diagonales dejando un espacio entre ellas porque al ser la longitud mínima de los barcos 2 así se reduciría mucho la cantidad de turnos necesarios para terminar la partida.

## Status
Funcional 100%


## Contacto
Puedes contactarme por GitHub si se te ocurre alguna otra característica que te gustaría añadir al juego.

# Será un placer para mí implementarla para ti! 
