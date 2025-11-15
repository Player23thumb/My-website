import pygame
import sys
import random
import math

pygame.init()

# --- Window ---
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game Starter")

CLOCK = pygame.time.Clock()
TILE_SIZE = 40

# --- Colours ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (60, 60, 60)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# --- Simple Map Layout ---
# 1 = wall, 0 = empty floor
ROOM_MAP = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# --- Player Class ---
class Charater:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.color = BLACK

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def is_colliding(self, a, b):
        return self.rect.collidepoint(a, b)

class Player(Charater):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GREEN
        self.speed = 4

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
    
    def move_down(self):
        self.rect.y -= self.speed

class Monster(Charater):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = RED
        self.speed = 2 
    
    def move_mon(self):
        n = random.random() * 10
        if math.floor(n) > 8:
            self.rect.y -= self.speed
        if math.floor(n) < 3:
            self.rect.y += self.speed
        if math.floor(n) > 2 and math.floor(n) < 5:
            self.rect.x -= self.speed
        if math.floor(n) == 7:
            self.rect.x += self.speed

class Wall():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.color = GREY
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
class door(Wall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = BLUE
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

player = Player(60, 60)
monster = Monster(40, 100)
n = []

# --- Draw the map ---
def draw_room():
    for row_index, row in enumerate(ROOM_MAP):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile == 2:
                door(x, y).draw(SCREEN)
            elif tile == 1:
                Wall(x, y).draw(SCREEN)
                r = [(x, y)]
                n.extend(r)
            else:
                pygame.draw.rect(SCREEN, BLACK, (x, y, TILE_SIZE, TILE_SIZE))


# --- Main Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    player.handle_input()
    monster.move_mon()
    if  player.rect.colliderect(monster.rect):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw
    SCREEN.fill(BLACK)
    draw_room()
    player.draw(SCREEN)
    monster.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(60)
