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
        coords.CENTER = (window.get_center()[0] / 10, window.get_center()[1] / 10)
        coords.LEFT_TOP = (0, 0)
        coords.RIGHT_TOP = (window.w / 10, 0)
        coords.LEFT_BOTTOM = (0, window.h / 10)
        coords.RIGHT_BOTTOM = (window.w / 10, window.h / 10)


class Layers:
    UI = 0
    VFX = 1
    ENTITIES = 2
    OBJECTS = 3
    FOREGROUND = 4
    BACKGROUND = 5


def check_button_press(buttons: list[Objects.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos) and button.visible:
            button.on_press()


def update_gameobjects(window: WR.WindowRenderer):
    for obj in Objects.GameObject.instancelist:
        obj.update()
        if obj.visible:
            window.draw.gameobject(obj)


def toggle_inv(player, invButton, invBackground: tuple):
    player.usingInv = not player.usingInv
    buttons = [obj for obj in Objects.GameObject.instancelist
               if 'UiButton' in obj.__class__.__name__]

    for button in buttons:
        if button != invButton:
            button.visible = not button.visible

    for obj in invBackground:
        obj.visible = not obj.visible

