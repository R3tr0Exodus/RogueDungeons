import pygame
from math import ceil
from GameObject import GameObject


class WindowRenderer:
    def __init__(self, flags, width=1920, height=1080):
        self.w = width
        self.h = height
        self.__screen = pygame.display.set_mode((self.w, self.h), flags=flags)
        self.w, self.h = pygame.display.get_surface().get_size()
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

        def gameobject(self, gameObj: GameObject):
            self.__screen.blit(gameObj.sprite, gameObj.rect)

        def rect(self, color: tuple, rect: pygame.rect):
            pygame.draw.rect(self.__screen, color, rect)

        def sprite(self, sprite: pygame.surface, rect: pygame.rect):
            self.__screen.blit(sprite, rect)

        def text(self, text: str, rect: pygame.rect, centered=False, font_path="../fonts/VT323-Regular.ttf",
                 color=(255, 255, 255), size=25):
            font = pygame.font.Font(font_path, size)
            txt = font.render(text, True, color)
            if centered:
                rect = txt.get_rect(center=(self.w/2, self.h/2))
            self.__screen.blit(txt, rect)

        def background(self, spritePath: str, scale):
            sprite = pygame.image.load(spritePath)
            sprite = pygame.transform.scale(sprite, (sprite.get_rect().width * scale, sprite.get_rect().height * scale))

            sprite_size = sprite.get_rect()
            blocks_x = ceil(self.w / sprite_size.w)
            blocks_y = ceil(self.h / sprite_size.h)

            for i in range(0, blocks_x):
                sprite = pygame.transform.flip(sprite, False, True)
                for j in range(0, blocks_y):
                    sprite = pygame.transform.flip(sprite, True, False)
                    self.__screen.blit(sprite, (i * sprite_size.w, j * sprite_size.h, sprite_size.w, sprite_size.h))

    def set_background_color(self, r, g, b):
        self.__backgroundColor = (r, g, b)

    def clear(self):
        self.__screen.fill(self.__backgroundColor)

    def get_center(self):
        return self.__screen.get_rect().center
