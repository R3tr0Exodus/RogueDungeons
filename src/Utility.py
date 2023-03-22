import pygame
import GameObject as Objects
import WindowRenderer as WR
from enum import Enum


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


def toggle_inv(player, invButton, invBackground):
    player.usingInv = not player.usingInv
    buttons = [obj for obj in Objects.GameObject.instancelist
               if 'UiButton' in obj.__class__.__name__]

    for button in buttons:
        if button != invButton:
            button.visible = not button.visible

    invBackground.visible = not invBackground.visible
