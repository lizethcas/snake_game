import pygame
import sys
from config import WIDTH, HEIGHT, BLACK, WHITE, GREEN, RED, GRAY
from instructions import mostrar_instrucciones

def mostrar_menu(screen):
    """Muestra un menú navegable."""
    pygame.display.set_caption("Snake Game - Menú")
    
    # Fuentes
    titulo_font = pygame.font.Font(None, 80)
    opcion_font = pygame.font.Font(None, 50)
    instruccion_font = pygame.font.Font(None, 30)
    
    # Opciones del menú
    opciones = ["Jugar", "Instrucciones", "Salir"]
    seleccion = 0
    
    while True:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if opciones[seleccion] == "Jugar":
                        return "jugar"
                    elif opciones[seleccion] == "Instrucciones":
                        mostrar_instrucciones(screen)
                    elif opciones[seleccion] == "Salir":
                        pygame.quit()
                        sys.exit()
        
        # Dibujar fondo
        screen.fill(BLACK)
        
        # Dibujar título
        titulo = titulo_font.render("SNAKE GAME", True, GREEN)
        titulo_rect = titulo.get_rect(center=(WIDTH//2, HEIGHT//4))
        screen.blit(titulo, titulo_rect)
        
        # Dibujar opciones
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                color = GREEN
                texto = f"> {opcion} <"
            else:
                color = WHITE
                texto = opcion
                
            texto_render = opcion_font.render(texto, True, color)
            texto_rect = texto_render.get_rect(center=(WIDTH//2, HEIGHT//2 + i * 60))
            screen.blit(texto_render, texto_rect)
        
        # Dibujar instrucciones de navegación
        instruccion = instruccion_font.render("Usa las flechas ↑↓ para navegar y ENTER para seleccionar", True, GRAY)
        instruccion_rect = instruccion.get_rect(center=(WIDTH//2, HEIGHT - 50))
        screen.blit(instruccion, instruccion_rect)
        
        pygame.display.flip()