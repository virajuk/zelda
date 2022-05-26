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

        # tile_count, player_count = 0, 0
        # for sprite in self.level.visible_sprites:
        #     if isinstance(sprite, (Tile, )):
        #         tile_count += 1
        #     if isinstance(sprite, (Player, )):
        #         player_count += 1
        #
        # print(f"tile_count {tile_count}, player_count {player_count}")

        running = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('#53c653')
            print(type(self.level.visible_sprites))
            print(self.level.visible_sprites[0])

            # debug(f"WIDTH {WIDTH}, HEIGHT {HEIGHT}")
            # self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':

    game = Game()
    game.run()
