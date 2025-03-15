import random
from config import WIDTH, HEIGHT, BLOCK_SIZE

def generar_comida(snake, enemigos):
    """Genera comida en una posición aleatoria que no coincida con la culebra ni enemigos."""
    while True:
        x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
        posicion = (x, y)
        
        # Verificar que no coincida con la culebra ni con enemigos
        if posicion not in snake and posicion not in enemigos:
            return posicion

def generar_enemigos(cantidad, snake, comida):
    """Genera una lista de enemigos en posiciones aleatorias."""
    enemigos = []
    
    for _ in range(cantidad):
        while True:
            x = random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
            y = random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
            posicion = (x, y)
            
            # Verificar que no coincida con la culebra, la comida u otros enemigos
            if (posicion not in snake and 
                posicion != comida and 
                posicion not in enemigos):
                enemigos.append(posicion)
                break
    
    return enemigos

def dibujar_elementos(screen, comida, enemigos):
    """Dibuja la comida y los enemigos en la pantalla."""
    import pygame
    from config import GREEN, RED
    
    # Dibujar comida (verde)
    pygame.draw.rect(screen, GREEN, 
                    (comida[0], comida[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Dibujar enemigos (rojos)
    for enemigo in enemigos:
        pygame.draw.rect(screen, RED, 
                        (enemigo[0], enemigo[1], BLOCK_SIZE, BLOCK_SIZE))