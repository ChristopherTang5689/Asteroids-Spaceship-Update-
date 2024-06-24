import pygame 
import math
import random

from scripts.settings import *

#Enemy class 
class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.ship_image = 'assets/sprites/spaceship.png'
            self.image = pygame.image.load(self.ship_image).convert_alpha()



            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(0, WIDTH)
            self.rect.y = random.randrange(0, HEIGHT)
            self.angle = (0, 45)
            self.direction = random.uniform(1, 3)

        def update(self):
        #Movememnt for enemy 
            if self.rect.x > WIDTH / 4: # moves in a slanted height after reach a treshold in the x position
                self.rect.y += self.direction * math.sin(self.direction)

            self.rect.x +=  self.direction * self.direction # Moves straight in an x position

            if self.rect.right < 0:
                self.rect.left = WIDTH
            elif self.rect.left > WIDTH:
                self.rect.right = 0
            if self.rect.bottom < 0:
                self.rect.top = HEIGHT
            elif self.rect.top > HEIGHT:
                self.rect.bottom = 0
