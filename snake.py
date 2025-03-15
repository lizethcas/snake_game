from config import WIDTH, HEIGHT, BLOCK_SIZE

def crear_culebra():
    """Crea una culebra inicial."""
    x_inicial = (WIDTH // BLOCK_SIZE // 2) * BLOCK_SIZE
    y_inicial = (HEIGHT // BLOCK_SIZE // 2) * BLOCK_SIZE
    return [(x_inicial, y_inicial), 
            (x_inicial - BLOCK_SIZE, y_inicial), 
            (x_inicial - BLOCK_SIZE * 2, y_inicial)]

def mover_culebra(snake, dx, dy, comida):
    """Mueve la culebra y crece si come comida."""
    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    if new_head == comida:  # Si come comida, crece
        snake.insert(0, new_head)
        return True  # Indica que se comió la comida
    else:
        snake.insert(0, new_head)
        snake.pop()  # No crece, solo se mueve
        return False  # No se comió la comida

def detectar_colision(snake, enemigos):
    """Detecta si la culebra choca consigo misma, con los bordes o con enemigos."""
    # Colisión con los bordes
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or 
        snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        return True
    
    # Colisión consigo misma
    if snake[0] in snake[1:]:
        return True
    
    # Colisión con enemigos
    if snake[0] in enemigos:
        return True
    
    return False

def dibujar_culebra(screen, snake, color):
    """Dibuja la culebra en la pantalla."""
    import pygame
    
    # Dibujar cuerpo
    for segmento in snake[1:]:
        pygame.draw.rect(screen, color, 
                        (segmento[0], segmento[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Dibujar cabeza (con un color ligeramente diferente)
    cabeza = snake[0]
    pygame.draw.rect(screen, color, 
                    (cabeza[0], cabeza[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Dibujar ojos
    ojo_size = BLOCK_SIZE // 5
    pygame.draw.rect(screen, (0, 0, 0), 
                    (cabeza[0] + BLOCK_SIZE//4, cabeza[1] + BLOCK_SIZE//4, 
                     ojo_size, ojo_size))
    pygame.draw.rect(screen, (0, 0, 0), 
                    (cabeza[0] + BLOCK_SIZE - BLOCK_SIZE//4 - ojo_size, 
                     cabeza[1] + BLOCK_SIZE//4, ojo_size, ojo_size))