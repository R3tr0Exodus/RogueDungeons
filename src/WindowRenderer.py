import pygame
from GameObject import GameObject


class WindowRenderer:
    def __init__(self, x, y, flags, width=1024, height=768):
        self.__x = x
        self.__y = y
        self.__w = width
        self.__h = height
        self.__screen = pygame.display.set_mode((self.__w, self.__h), flags=flags)
        self.__backgroundColor = (255, 255, 255)

        self.__screen.fill(self.__backgroundColor)

    def update(self):
        pygame.display.flip()
        self.clear()

    def draw_gameobject(self, gameObj: GameObject):
        self.__screen.blit(gameObj.sprite, gameObj.rect)

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)