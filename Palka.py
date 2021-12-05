import pygame


class Palka:
    def __init__(self, x , y):
        self.x = x
        self.y  = y
        self.width = 100
        self.height = 10
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)

