import pygame
from math import floor
from GameObject import GameObject


class WindowRenderer:
    def __init__(self, flags, width=1920, height=1080):
        self.w = width
        self.h = height
        self.__screen = pygame.display.set_mode((self.w, self.h), flags=flags)
        self.__backgroundColor = (255, 255, 255)

        # Reference to inner class
        self.draw = WindowRenderer.Draw(self.w, self.h, self.__screen)

    def update(self):
        pygame.display.flip()
        self.clear()

    class Draw:
        def __init__(self, w, h, screen):
            self.w = w
            self.h = h
            self.__screen = screen

            self.blocksX = floor(self.w / 100)
            self.blocksY = floor(self.h / 100)
            print(f'blocksX: {self.blocksX} | blocksY: {self.blocksY}')

        def gameobject(self, gameObj: GameObject):
            self.__screen.blit(gameObj.sprite, gameObj.rect)

        def rect(self, color: tuple, rect: pygame.rect):
            pygame.draw.rect(self.__screen, color, rect)

        def sprite(self, sprite: pygame.surface, rect: pygame.rect):
            self.__screen.blit(sprite, rect)

        def background(self, spritePath: str):
            sprite = pygame.image.load(spritePath)

            for i in range(0, self.blocksX):
                for j in range(0, self.blocksY):
                    self.__screen.blit(sprite, pygame.Rect(i * 100, j * 100, 100, 100))

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)

    def get_center(self):
        return self.__screen.get_rect().center
