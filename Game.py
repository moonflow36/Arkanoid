import pygame
from Palka import Palka
from Kirpich import Kirpich
class Game:
    def __init__(self):
        pygame.init()
        self. WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.palka = Palka(self.WINDOW_WIDTH // 2-40, self.WINDOW_HEIGHT-30)
        self.kirpich = Kirpich(10, 10)

    def get_keys(self):
       for event in  pygame.event.get():
           if event.type == pygame.QUIT:
               exit()

    def start(self):
        while True:
            self.get_keys()
            self.draw()

    def draw(self):
        self.kirpich.draw(self.screen)
        self.palka.draw(self.screen)
        pygame.display.flip()



game = Game()
game.start()