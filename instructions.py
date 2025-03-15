import pygame
import sys
from config import WIDTH, HEIGHT, BLACK, WHITE, BLUE, GRAY, GREEN, RED

def mostrar_instrucciones(screen):
    """Muestra la pantalla de instrucciones."""
    pygame.display.set_caption("Snake Game - Instrucciones")
    
    # Fuentes
    titulo_font = pygame.font.Font(None, 60)
    texto_font = pygame.font.Font(None, 36)
    volver_font = pygame.font.Font(None, 30)
    
    instrucciones = [
        "Controla la culebra con las flechas del teclado",
        "Come los cuadros verdes para crecer",
        "Evita los cuadros rojos (enemigos)",
        "Los enemigos aparecen, desaparecen y se mueven",
        "No choques contra los bordes ni contra ti mismo"
    ]
    
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    esperando = False
        
        # Dibujar fondo
        screen.fill(BLACK)
        
        # Dibujar título
        titulo = titulo_font.render("INSTRUCCIONES", True, BLUE)
        titulo_rect = titulo.get_rect(center=(WIDTH//2, 80))
        screen.blit(titulo, titulo_rect)
        
        # Dibujar instrucciones
        for i, linea in enumerate(instrucciones):
            texto = texto_font.render(linea, True, WHITE)
            texto_rect = texto.get_rect(center=(WIDTH//2, 180 + i * 50))
            screen.blit(texto, texto_rect)
        
        # Dibujar ejemplos visuales
        pygame.draw.rect(screen, GREEN, (WIDTH//2 - 150, 430, 20, 20))
        texto = texto_font.render("Comida - ¡Cómela!", True, WHITE)
        screen.blit(texto, (WIDTH//2 - 120, 430))
        
        pygame.draw.rect(screen, RED, (WIDTH//2 - 150, 460, 20, 20))
        texto = texto_font.render("Enemigo - ¡Evítalo!", True, WHITE)
        screen.blit(texto, (WIDTH//2 - 120, 460))
        
        # Dibujar instrucción para volver
        volver = volver_font.render("Presiona ESC o ENTER para volver al menú", True, GRAY)
        volver_rect = volver.get_rect(center=(WIDTH//2, HEIGHT - 50))
        screen.blit(volver, volver_rect)
        
        pygame.display.flip()