# 🐍 SNAKE GAME EXTREME 🐍

## 🔥 DESCRIPCIÓN

**Snake Game Extreme** es una versión adrenalínica del clásico juego de la serpiente, llevado al siguiente nivel con enemigos dinámicos que aparecen, desaparecen y se mueven por el tablero. ¡Pon a prueba tus reflejos y habilidades mientras intentas sobrevivir en este desafiante entorno!

## ⚡ CARACTERÍSTICAS PRINCIPALES

- 🎮 **Controles intuitivos**: Maneja la serpiente con las flechas del teclado
- 🟢 **Comida nutritiva**: Come cuadros verdes para crecer y ganar puntos
- 🔴 **Enemigos mortales**: Evita los cuadros rojos que aparecen aleatoriamente
- 🌪️ **Dinámica impredecible**: Los enemigos aparecen, desaparecen y se mueven constantemente
- 🏆 **Sistema de puntuación**: Compite contra ti mismo para superar tu récord
- 📱 **Menú navegable**: Interfaz amigable con opciones de juego, instrucciones y salida

## 🚀 INSTALACIÓN

### Requisitos previos
- Python 3.6 o superior
- Pygame 2.0 o superior

### Pasos de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/snake-game-extreme.git
cd snake-game-extreme
```

2. Instala las dependencias:
```bash
pip install pygame
```

3. Ejecuta el juego:
```bash
python main.py
```

## 🎯 CÓMO JUGAR

1. **Inicia el juego** seleccionando "Jugar" en el menú principal
2. **Controla la serpiente** usando las teclas de flecha:
   - ⬆️ Arriba
   - ⬇️ Abajo
   - ⬅️ Izquierda
   - ➡️ Derecha
3. **Come comida verde** para crecer y ganar puntos
4. **Evita los enemigos rojos** que aparecen por el tablero
5. **No choques** contra los bordes ni contra tu propio cuerpo
6. **Presiona ESC** en cualquier momento para volver al menú

## 🧩 ESTRUCTURA DEL PROYECTO
snake-game-extreme/
```│
├── main.py # Punto de entrada principal del juego
├── config.py # Configuraciones y constantes
├── menu.py # Sistema de menú navegable
├── instrucciones.py # Pantalla de instrucciones
├── snake.py # Lógica de la serpiente
├── elementos.py # Generación de comida y enemigos
└── README.md # Este archivo
```

## 🎮 MECÁNICAS DE JUEGO

- **Crecimiento**: La serpiente crece cada vez que come comida verde
- **Puntuación**: Ganas 10 puntos por cada comida consumida
- **Enemigos dinámicos**: Los enemigos rojos:
  - Se reubican completamente cuando comes comida
  - Aparecen, desaparecen y se mueven aleatoriamente cada pocos segundos
  - Aumentan la dificultad a medida que avanza el juego
- **Game Over**: El juego termina si:
  - Chocas contra un borde del tablero
  - Chocas contra tu propio cuerpo
  - Chocas contra un enemigo rojo

## 🛠️ PERSONALIZACIÓN

Puedes personalizar varios aspectos del juego modificando el archivo `config.py`:

- **Tamaño de pantalla**: Ajusta `WIDTH` y `HEIGHT`
- **Velocidad del juego**: Modifica `FPS`
- **Tamaño de los elementos**: Cambia `BLOCK_SIZE`
- **Colores**: Personaliza los colores de la serpiente, comida y enemigos

Para jugadores avanzados, también puedes modificar:
- El número máximo de enemigos en `main.py`
- La frecuencia de cambio de los enemigos
- La lógica de generación de enemigos

## 🏆 DESAFÍOS

¿Crees que eres bueno? Intenta superar estos desafíos:

- 🥉 **Principiante**: Alcanza 100 puntos
- 🥈 **Intermedio**: Alcanza 300 puntos
- 🥇 **Experto**: Alcanza 500 puntos
- 🏅 **Maestro**: Alcanza 1000 puntos
- 👑 **Leyenda**: Llena toda la pantalla con tu serpiente

## 🔧 SOLUCIÓN DE PROBLEMAS

| Problema | Solución |
|----------|----------|
| El juego no inicia | Verifica que tienes Python y Pygame instalados correctamente |
| Pantalla negra | Asegúrate de que todos los archivos están en la misma carpeta |
| Errores de importación | Verifica que todos los archivos tienen la extensión .py |
| Rendimiento lento | Reduce el valor de FPS en config.py |


**¡DIVIÉRTETE JUGANDO SNAKE GAME EXTREME!** 🐍🎮

*¿Puedes convertirte en la serpiente más larga sin ser derrotado por los enemigos?*
