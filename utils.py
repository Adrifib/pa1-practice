import pygame
from constants import *  # Importar constantes definidas en otro archivo
import sys

def draw_winner_board(winner):  # Función para mostrar una pantalla que anuncia al ganador
    # Si el script se ejecuta en modo texto ('main_txt' está en el nombre del archivo)
    if 'main_txt' in sys.argv[0]:
        draw_winner_txt(winner)  # Llama a la función que muestra el ganador en texto
        return  # Sale de la función después de mostrar el texto
    
    # Inicializar Pygame si aún no está inicializado
    if not pygame.get_init():
        pygame.init()
    
    # Dimensiones de la ventana
    w_width = 400
    w_height = 400
    screen = pygame.display.set_mode((w_width, w_height))  # Crear la ventana con el tamaño especificado
    pygame.display.set_caption("Winner")  # Título de la ventana

    reloj = pygame.time.Clock()  # Reloj para controlar la tasa de actualización
    font = pygame.font.Font(None, 74)  # Definir la fuente y el tamaño del texto
    # Determinar el texto ganador basado en el valor de 'winner'
    winner_text = "Blue Wins!" if winner == 0 else "Red Wins!"
    # Renderizar el texto con el color correspondiente
    text = font.render(winner_text, True, BLUISH if winner == 0 else REDDISH)
    # Centrar el texto en la pantalla
    text_rect = text.get_rect(center=(w_width/2, w_height/2))

    # Bucle principal para mantener la ventana abierta hasta que se cierre
    while True:
        for event in pygame.event.get():
            # Cerrar la ventana si se detecta un evento de salida (clic en la 'X')
            if event.type == pygame.QUIT:
                pygame.quit()  # Cierra Pygame correctamente
                return  # Sale de la función
        
        screen.fill(BLACK)  # Rellena la pantalla con color negro
        screen.blit(text, text_rect)  # Dibuja el texto en la pantalla en la posición calculada
        pygame.display.flip()  # Actualiza la pantalla para mostrar los cambios
        reloj.tick(60)  # Limita la velocidad de fotogramas a 60 FPS

def draw_winner_txt(winner):  # Función para mostrar el ganador en modo texto (consola)
    # Determinar el texto ganador basado en el valor de 'winner'
    winner_text = "Circles Wins!" if winner == 0 else "Crosses Wins!"
    # Imprimir el resultado formateado en la consola
    print("\n" + "=" * 20)
    print(f"\t{winner_text}")
    print("=" * 20 + "\n")

def show_menu():
    """Muestra un menú principal atractivo y retorna el modo de juego seleccionado"""
    if not pygame.get_init():
        pygame.init()
        
    menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Three in a Row - Menu")
    clock = pygame.time.Clock()
    
    # Definir fuentes para diferentes elementos
    title_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 48)
    subtitle_font = pygame.font.Font(None, 36)
    
    # Título del juego
    title_text = title_font.render("Three in a Row", True, BLUISH)
    title_rect = title_text.get_rect(center=(WIDTH/2, HEIGHT/4))
    
    # Subtítulo
    subtitle_text = subtitle_font.render("Select Game Mode", True, BLACK)
    subtitle_rect = subtitle_text.get_rect(center=(WIDTH/2, HEIGHT/4 + 50))
    
    # Botones
    button_padding = 20
    button_margin = 40
    button_width = 200
    button_height = 60
    
    # Crear rectángulos para los botones
    normal_rect = pygame.Rect(0, 0, button_width, button_height)
    misery_rect = pygame.Rect(0, 0, button_width, button_height)
    
    # Centrar los botones
    normal_rect.center = (WIDTH/2, HEIGHT/2)
    misery_rect.center = (WIDTH/2, HEIGHT/2 + button_height + button_margin)
    
    # Textos de los botones
    normal_text = button_font.render("Normal", True, WHITE)
    misery_text = button_font.render("Misery", True, WHITE)
    normal_text_rect = normal_text.get_rect(center=normal_rect.center)
    misery_text_rect = misery_text.get_rect(center=misery_rect.center)
    
    # Variables para efectos de hover
    normal_hover = False
    misery_hover = False
    
    while True:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
                
            # Detectar posición del mouse para hover
            mouse_pos = pygame.mouse.get_pos()
            normal_hover = normal_rect.collidepoint(mouse_pos)
            misery_hover = misery_rect.collidepoint(mouse_pos)
            
            # Detectar clics
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_hover:
                    return "normal"
                if misery_hover:
                    return "misery"
        
        # Dibujar fondo
        menu_screen.fill(WHITE)
        
        # Dibujar título y subtítulo
        menu_screen.blit(title_text, title_rect)
        menu_screen.blit(subtitle_text, subtitle_rect)
        
        # Dibujar botones con efectos de hover
        # Botón Normal
        button_color = BLUISH if normal_hover else REDDISH
        pygame.draw.rect(menu_screen, button_color, normal_rect, border_radius=10)
        pygame.draw.rect(menu_screen, BLACK, normal_rect, 2, border_radius=10)  # Borde
        menu_screen.blit(normal_text, normal_text_rect)
        
        # Botón misery
        button_color = BLUISH if misery_hover else REDDISH
        pygame.draw.rect(menu_screen, button_color, misery_rect, border_radius=10)
        pygame.draw.rect(menu_screen, BLACK, misery_rect, 2, border_radius=10)  # Borde
        menu_screen.blit(misery_text, misery_text_rect)
        
        # Dibujar un pequeño mensaje al pie
        footer_text = subtitle_font.render("Press ESC to quit", True, GRAY)
        footer_rect = footer_text.get_rect(center=(WIDTH/2, HEIGHT - 50))
        menu_screen.blit(footer_text, footer_rect)
        
        # Actualizar pantalla
        pygame.display.flip()
        clock.tick(60)