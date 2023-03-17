import pygame
from GameObject import GameObject


class WindowRenderer:
    def __init__(self, width=1024, height=768):
        self.w = width
        self.h = height
        self.__screen = pygame.display.set_mode((self.w, self.h))
        self.__backgroundColor = (255, 255, 255)

    def update(self):
        pygame.display.flip()
        self.clear()

    def draw_gameobject(self, gameObj: GameObject):
        self.__screen.blit(gameObj.sprite, gameObj.rect)

    def draw_rect(self, color: tuple, rect: pygame.rect):
        pygame.draw.rect(self.__screen, color, rect)

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)