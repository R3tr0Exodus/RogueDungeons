import pygame
import GameObject as Objects
import WindowRenderer as WR
from enum import Enum


class Layers:
    ITEM = 0
    UI = 1
    VFX = 2
    ENTITIES = 3
    OBJECTS = 4
    FOREGROUND = 5
    BACKGROUND = 6


def check_button_press(buttons: list[Objects.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos) and button.visible:
            button.on_press()


def update_gameobjects(window: WR.WindowRenderer):
    for obj in Objects.GameObject.instancelist:
        obj.update()
        if obj.visible:
            window.draw.gameobject(obj)


def toggle_inv(player: Objects.Player, invButton, invBackground: tuple[Objects.GameObject]):
    player.usingInv = not player.usingInv
    buttons = [obj for obj in Objects.GameObject.instancelist
               if 'UiButton' in obj.__class__.__name__]

    for button in buttons:
        if button != invButton:
            button.visible = not button.visible

    for obj in invBackground:
        obj.visible = not obj.visible

    for i, item in enumerate(player.get_inventory()):
        # Move items inside the item spots on screen
        item.move(invBackground[i + 3].rect.x + 10, invBackground[i + 3].rect.y + 10)
        item.visible = not item.visible
