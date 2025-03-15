import pygame
import sys
import random
import time
from config import WIDTH, HEIGHT, BLACK, GREEN, WHITE, RED, FPS, BLOCK_SIZE
from snake import crear_culebra, mover_culebra, detectar_colision, dibujar_culebra
from elements import generar_comida, generar_enemigos, dibujar_elementos
from menu import mostrar_menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    while True:
        # Mostrar menú y obtener opción seleccionada
        opcion = mostrar_menu(screen)
        
        if opcion == "jugar":
            jugar(screen, clock)

def jugar(screen, clock):
    """Función principal del juego."""
    pygame.display.set_caption("Snake Game")
    
    # Inicializar variables del juego
    snake = crear_culebra()
    dx, dy = BLOCK_SIZE, 0  # Dirección inicial: derecha
    
    # Generar comida inicial
    enemigos = []
    comida = generar_comida(snake, enemigos)
    
    # Configuración de enemigos
    max_enemigos = 5
    tiempo_ultimo_cambio = time.time()
    intervalo_cambio = 2.0  # Segundos entre cambios de enemigos
    
    # Puntuación
    puntuacion = 0
    font = pygame.font.Font(None, 36)
    
    # Bucle principal del juego
    running = True
    game_over = False
    
    while running:
        tiempo_actual = time.time()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Control de la culebra
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_RETURN:
                        return  # Volver al menú
                else:
                    if event.key == pygame.K_UP and dy == 0:
                        dx, dy = 0, -BLOCK_SIZE
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dx, dy = 0, BLOCK_SIZE
                    elif event.key == pygame.K_LEFT and dx == 0:
                        dx, dy = -BLOCK_SIZE, 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = BLOCK_SIZE, 0
                    elif event.key == pygame.K_ESCAPE:
                        running = False  # Volver al menú
        
        if not game_over:
            # Mover la culebra
            comio = mover_culebra(snake, dx, dy, comida)
            
            # Si comió, generar nueva comida y aumentar puntuación
            if comio:
                puntuacion += 10
                comida = generar_comida(snake, enemigos)
                
                # Reubicar todos los enemigos cuando come
                enemigos = []
                num_enemigos = random.randint(5, max_enemigos)
                for _ in range(num_enemigos):
                    nuevo_enemigo = generar_comida(snake, enemigos + [comida])
                    enemigos.append(nuevo_enemigo)
            
            # Cambiar enemigos periódicamente
            if tiempo_actual - tiempo_ultimo_cambio >= intervalo_cambio:
                # Decidir qué hacer con los enemigos
                accion = random.choice(["agregar", "quitar", "mover"])
                
                if accion == "agregar" and len(enemigos) < max_enemigos:
                    # Agregar un nuevo enemigo
                    nuevo_enemigo = generar_comida(snake, enemigos + [comida])
                    enemigos.append(nuevo_enemigo)
                
                elif accion == "quitar" and len(enemigos) > 3:
                    # Quitar un enemigo aleatorio
                    indice = random.randint(0, len(enemigos) - 1)
                    enemigos.pop(indice)
                
                elif accion == "mover" and len(enemigos) > 0:
                    # Mover un enemigo aleatorio
                    indice = random.randint(0, len(enemigos) - 1)
                    nuevo_enemigo = generar_comida(snake, enemigos + [comida])
                    enemigos[indice] = nuevo_enemigo
                
                tiempo_ultimo_cambio = tiempo_actual
            
            # Verificar colisiones
            if detectar_colision(snake, enemigos):
                game_over = True
        
        # Dibujar elementos
        screen.fill(BLACK)
        
        # Dibujar culebra, comida y enemigos
        dibujar_culebra(screen, snake, GREEN)
        dibujar_elementos(screen, comida, enemigos)
        
        # Dibujar puntuación
        texto_puntuacion = font.render(f"Puntuación: {puntuacion}", True, WHITE)
        screen.blit(texto_puntuacion, (10, 10))
        
        # Si es game over, mostrar mensaje
        if game_over:
            game_over_font = pygame.font.Font(None, 72)
            texto_game_over = game_over_font.render("¡GAME OVER!", True, RED)
            texto_rect = texto_game_over.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
            screen.blit(texto_game_over, texto_rect)
            
            instruccion_font = pygame.font.Font(None, 36)
            texto_instruccion = instruccion_font.render("Presiona ENTER para volver al menú", True, WHITE)
            texto_rect = texto_instruccion.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
            screen.blit(texto_instruccion, texto_rect)
            
            # Mostrar puntuación final
            texto_final = instruccion_font.render(f"Puntuación final: {puntuacion}", True, WHITE)
            texto_rect = texto_final.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
            screen.blit(texto_final, texto_rect)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()