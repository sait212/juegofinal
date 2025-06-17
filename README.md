🛡 Guardians of the Ancient Kingdom - Documentación del Juego
1. Descripción General
Este juego es una batalla entre tres personajes: Guerrero, Mago y Arquero, creado con Python y Tkinter utilizando principios de Programación Orientada a Objetos (POO).
Cada personaje tiene atributos únicos y habilidades especiales. El juego se desarrolla en rondas por turnos hasta que uno de los personajes es el último en pie.

2. Clases y Herencia
Clase Base: Personaje

Atributos privados: vida, ataque y defensa.

Métodos: getters y setters, y un método atacar() (sobrescrito por cada subclase).

Subclases:

Guerrero: Ataque con 20% de daño adicional.

Mago: Su ataque ignora la defensa del enemigo.

Arquero: Si su ataque supera la defensa del enemigo, inflige el doble de daño.

3. Lógica del Juego
Cada personaje ataca por turnos. El ataque se realiza a un enemigo aleatorio entre los personajes que aún estén vivos.
El juego termina cuando queda solo un personaje con vida.
La interfaz muestra el estado actual de vida de cada personaje después de cada ataque, así como el resultado de cada acción.

4. Interfaz Gráfica con Tkinter
La interfaz del juego se construye con Tkinter:

Se muestra una ventana con los personajes y su vida.

Un botón permite avanzar al siguiente turno.

Los resultados de cada ataque se visualizan en un cuadro de texto (Text).

Al finalizar el juego, se anuncia el ganador con una ventana emergente (messagebox).

5. Código Fuente (Resumen)
El código define:

Las clases de personajes, con herencia y polimorfismo.

La clase Juego, que construye la ventana principal, inicializa a los tres personajes y ejecuta el ciclo de combate.

Cada clase hija sobrescribe el método atacar() con su lógica específica.

El ciclo del juego se maneja desde la clase Juego, que también controla la interfaz y los turnos de ataque hasta que un único personaje queda en pie.

