import pygame
from GameObject import GameObject


class WindowRenderer:
    def __init__(self, width=1024, height=768):
        self.w = width
        self.h = height
        self.__screen = pygame.display.set_mode((self.w, self.h))
        self.__backgroundColor = (255, 255, 255)

        # Reference to inner class
        self.draw = WindowRenderer.Draw(self.__screen)

    def update(self):
        pygame.display.flip()
        self.clear()

    class Draw:
        def __init__(self, screen):
            self.__screen = screen

        def gameobject(self, gameObj: GameObject):
            self.__screen.blit(gameObj.sprite, gameObj.rect)

        def rect(self, color: tuple, rect: pygame.rect):
            pygame.draw.rect(self.__screen, color, rect)

        def sprite(self, sprite: pygame.surface, rect: pygame.rect):
            self.__screen.blit(sprite, rect)

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)