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