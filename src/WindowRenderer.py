import pygame
from GameObject import GameObject


class WindowRenderer:
    w: int = None
    h: int = None
    __screen = None
    __backgroundColor = (255, 255, 255)

    def __init__(self, width=1024, height=763):
        self.w = width
        self.h = height
        self.__screen = pygame.display.set_mode((self.w, self.h))
        self.__screen.fill(self.__backgroundColor)

    def update(self):
        pygame.display.flip()
        self.clear()

    def draw_game_object(self, img: pygame.Surface, rect: pygame.Rect=None):
        if rect is None:
            self.__screen.blit(img, img.get_rect())
        else:
            self.__screen.blit(img, rect)

    def draw_rect(self, color: tuple, rect: pygame.rect):
        pygame.draw.rect(self.__screen, color, rect)

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)