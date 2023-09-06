import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
pygame.display.set_caption("Prosta Gra Pygame")

clock = pygame.time.Clock()

def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))



        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
