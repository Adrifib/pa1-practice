import pygame

pygame.init()

width = 400
height = 400
negro = (0, 0, 0)
azul = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Winner")

def main():
    reloj = pygame.time.Clock()
    font = pygame.font.Font(None, 74)
    text = font.render("Blue Winner!", True, azul)
    text_rect = text.get_rect(center=(width/2, height/2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill(negro)
        screen.blit(text, text_rect)
        pygame.display.flip()
        reloj.tick(60)

main()
