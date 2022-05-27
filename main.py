import pygame

from config import *
from debug import debug

from src.level import Level
from src.tile import Tile
from src.player import Player


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MAN KIND")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('#669900')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':

    game = Game()
    game.run()
