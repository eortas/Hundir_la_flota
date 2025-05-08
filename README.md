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
* [Contacto](#contact)

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

## Estado
Funcional 100%

# ¿Qué he aprendido con este proyecto?

* Lo primero y más importante: Persigue la simplicidad sobre la complejidad.
* Lo segundo: El trabajo duro excesivo es algo que la sociedad valora mucho. Largas jornadas delante del ordenador, gran esfuerzo para aprender primero una gran cantidad de información en poco tiempo, la frustración que puede venir a llamar a tu puerta cuando no alcanzas a comprender como plasmar esa nueva información en código práctico e incluso sufrimiento parecen ser medios para alcanzar la gloria en muchos escenarios. He intentado hacer siempre hasta donde he podido y un paso más. Hasta que he visto dónde no era seguro seguir caminando, no abandonando el proyecto sino con un cartel de nos volveremos a ver en el futuro, amigo.
* Efectividad justo después de simplicidad. Si puede que el código no sea el más optimizado pero funciona, y a partir de ahí se puede ir avanzando. De una función puedes reutilizarla para otras, otra vez lo mismo pero si la primera la has realizado bien, has comprobado que funciona a la perfección, ¿por qué no ibas a aprovecharlo?

¡Nos vemos en el siguiente proyecto!

## Resumen gráfico del proceso de desarrollo desde el día 1 al día 3
Primer día, todo eran muros infranqueables, arenas movedizas y tropiezos. Hasta que dejas de ver a la piedra como una más que te encontrarás con ella y la saludas mientras intentas esquivarla.
![31e8b0cd-f2ea-48d4-90a3-c8b710fb63e3](https://github.com/user-attachments/assets/3c94865c-63ba-4fe6-8d5d-58e1bbc02f2a)

He dejado bastantes ideas por el camino, que seguro que volveré a andar para añadirlas, y también mejorar partes del código que sé que podría haber hecho de otra manera, no sé si mejor, porque a mí por mi experiencia aunque ajena al mundo de la programación el resultado final me ha dejado contento. Creando un armazón robusto sobre el que he ido añadiendo más capas sin que rompieran lo anterior y cuando algo rompía poder volver atrás y saber cuando desechar una idea para que el conjunto no se resienta por invertir demasiado en otras partes.
![ChatGPT Image 1 may 2025, 02_13_51](https://github.com/user-attachments/assets/1ea5d5e5-6b5a-4f7f-9009-a9fff7531780)



## Contacto
Puedes contactarme por GitHub si se te ocurre alguna otra característica que te gustaría añadir al juego.
Será un placer para mí implementarla para ti! 
