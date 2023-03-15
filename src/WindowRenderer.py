import pygame
from GameObject import GameObject


class WindowRenderer:
    __x = __y = 0
    __w = __h = 0
    __screen = None
    __backgroundColor = (255, 255, 255)

    def __init__(self, x, y, width=1024, height=768):
        self.__x = x
        self.__y = y
        self.__w = width
        self.__h = height
        self.__screen = pygame.display.set_mode((self.__w, self.__h))
        self.__screen.fill(self.__backgroundColor)

    def update(self):
        pygame.display.flip()
        self.clear()

    def draw_game_object(self, img: pygame.Surface, rect: pygame.Rect=None):
        if rect is None:
            self.__screen.blit(img, img.get_rect())
        else:
            self.__screen.blit(img, rect)

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)