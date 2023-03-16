import pygame
import GameObject
import WindowRenderer as WR
from enum import Enum


class Layers(Enum):
    UI = 0
    VFX = 1
    ENTITIES = 2
    OBJECTS = 3
    FOREGROUND = 4
    BACKGROUND = 5


def check_button_press(buttons: list[GameObject.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos):
            button.on_press()


def update_gameobjects(gameobjects: list[GameObject.GameObject], window: WR.WindowRenderer):
    gameobjects.sort(key=lambda x: x.layer)
    for gameObj in gameobjects:
        gameObj.update()
        window.draw_gameobject(gameObj)
