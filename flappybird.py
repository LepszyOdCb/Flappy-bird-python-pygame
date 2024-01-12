import pygame
import random as r
import sys

# Inicjalizacja Pygame
pygame.init()

font = pygame.font.SysFont('comicsans', 45)

# Załadownie grafik
tower = pygame.image.load("tower.png")
plane = pygame.image.load("plane.png")
loosingscreen = pygame.image.load("loosingscreen.png")
boomboom = pygame.image.load("boomboom.jpg")
none = pygame.image.load("none.png ")
background = pygame.image.load("background.png")
winningscreen = pygame.image.load("winningscreen.png")

# Wymiary ekranu
screen_width = 800
screen_height = 700

# Kolory
yellow = (255, 255, 0)
blue = (0, 255, 255)
lime = (0, 255, 0)
black = (255, 255, 255)

# Wielkość przeszkód
obstacle_size = 100
lenght = 21

# Lista przeszkód
obstacles_empty = []
for x in range(0, lenght, 3):
    random_y = r.randint(1, 5)
    obstacles_empty.append((obstacle_size * x * 1.2 + 800, obstacle_size * random_y))

obstacles = []
for x in range(0, lenght, 3):
    for y in range(0, 7):
        obstacles.append((obstacle_size * x * 1.2 + 800, obstacle_size * y))
#for x in range(24, 26, 2):
#    for y in range(0, 7):
#        obstacles.append((obstacle_size * x * 1.2, obstacle_size * y))

obstacles = [obstacle for obstacle in obstacles if obstacle not in obstacles_empty]
print(obstacles)
# Zmienne duszka
jump_height = 20
movement_speed = 1.2
duszek_size = 50

# Klasa duszka
class Duszek(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = plane
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.centery = screen_height // 2
        self.alive = True

# Inicjalizacja ekranu
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy bird")

# Tworzenie grupy dla duszka
all_sprites = pygame.sprite.Group()
duszek = Duszek()
all_sprites.add(duszek)

# Czas
clock = pygame.time.Clock()

# Główna pętla gry
running = True
game_over = False
game_win = False
start = False
end = False
spacepressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spacepressed = True
            if not game_over and not game_win:
                duszek.rect.y -= jump_height
                start = True
        else:
            spacepressed = False
    if not start:
        screen.blit(background, (0, 0))

    if not game_over and start:
        # Przesuwanie przeszkód i widoku w prawo
        for i, (obstacle_x, obstacle_y) in enumerate(obstacles):
            obstacles[i] = (obstacle_x - movement_speed, obstacle_y)

        screen.blit(background, (0, 0))
        duszek.rect.y += 1.5

        for obstacle_x, obstacle_y in obstacles:
            screen.blit(tower, (obstacle_x, obstacle_y))
            if duszek.rect.centerx >= obstacle_x-duszek_size/2 and duszek.rect.centerx+duszek_size*2 <= obstacle_x+obstacle_size*2 and duszek.rect.centery >= obstacle_y and duszek.rect.centery+duszek_size*2 <= obstacle_y+obstacle_size*2 or duszek.rect.centery > screen_height or duszek.rect.centery <0:
                game_over = True
            elif duszek.rect.centerx > obstacle_x+lenght*obstacle_size+obstacle_size+200:
                game_win = True
    if game_over:
        screen.blit(loosingscreen, (0, 0))
        screen.blit(boomboom, (duszek.rect.x-50, duszek.rect.y-50))
        duszek.alive = False
        duszek.image = none

        end = True
    if game_win:
        screen.blit(winningscreen, (0,0))
        text = "Wygrałeś"
        label = font.render(text, 30, (0, 0, 0))
        screen.blit(label, (0, 0, 0, 0))
        end = True

    if end and spacepressed:
        running = False

    # Odświeżanie ekranu
    if duszek.alive:
        all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(30)

# Po zakończeniu pętli gry
pygame.quit()
sys.exit()
