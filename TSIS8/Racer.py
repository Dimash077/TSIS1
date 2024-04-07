import pygame
import sys
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
CARS_PASSED = 0
COINS_COLLECTED = 0

font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")

# Load sounds
coin_sound = pygame.mixer.Sound('coin.wav')
crash_sound = pygame.mixer.Sound('crash.wav')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)  


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global CARS_PASSED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            CARS_PASSED += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 380), 0)
        self.dx = 1.5
        self.dy = 1.5

    def move(self):
        if self.rect.top < SCREEN_HEIGHT:
            self.rect.move_ip(0, SPEED)
        else:
            self.rect.center = (random.randint(30, 380), 0)


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

game_over_flag = False

while not game_over_flag:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    cars_passed_text = font.render("Cars Passed: " + str(CARS_PASSED), True, BLACK)
    coins_collected_text = font.render("Coins: " + str(COINS_COLLECTED), True, BLACK)
    DISPLAYSURF.blit(cars_passed_text, (10, 10))
    DISPLAYSURF.blit(coins_collected_text, (SCREEN_WIDTH - coins_collected_text.get_width() - 10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        game_over_flag = True

    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        coin_sound.play()
        C1.rect.top = 0
        C1.rect.center = (random.randint(30, 380), 0)

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.mixer.music.stop()  
DISPLAYSURF.blit(game_over, (150, 200))
pygame.display.update()
time.sleep(2)
pygame.quit()
sys.exit()