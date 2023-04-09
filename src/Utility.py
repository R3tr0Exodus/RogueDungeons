import pygame
import GameObject as Objects
import WindowRenderer as WR
from enum import Enum


class coords:
    CENTER: tuple
    LEFT_TOP: tuple
    RIGHT_TOP: tuple
    LEFT_BOTTOM: tuple
    RIGHT_BOTTOM: tuple

    @staticmethod
    def set_coords(window):
        coords.CENTER = window.get_center()
        coords.LEFT_TOP = (0, 0)
        coords.RIGHT_TOP = (window.w, 0)
        coords.LEFT_BOTTOM = (0, window.h)
        coords.RIGHT_BOTTOM = (window.w, window.h)


class Layers:
    UI = 0
    VFX = 1
    ENTITIES = 2
    OBJECTS = 3
    FOREGROUND = 4
    BACKGROUND = 5


def check_button_press(buttons: list[Objects.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos):
            button.on_press()


def update_gameobjects(window: WR.WindowRenderer):
    for obj in Objects.GameObject.instancelist:
        obj.update()
        if obj.visible:
            window.draw.gameobject(obj)
