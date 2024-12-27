import pygame
from constants import *


def draw_winner_board(winner): # Pantalla para el ganador del juego
    w_width = 400
    w_height = 400
    screen = pygame.display.set_mode((w_width, w_height))
    pygame.display.set_caption("Winner")

    reloj = pygame.time.Clock()
    font = pygame.font.Font(None, 74)
    winner_text = "Blue Wins!" if winner == 0 else "Red Wins!"
    text = font.render(winner_text, True, BLUISH if winner == 0 else REDDISH)
    text_rect = text.get_rect(center=(w_width/2, w_height/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill(BLACK)
        screen.blit(text, text_rect)
        pygame.display.flip()
        reloj.tick(60)

    pass