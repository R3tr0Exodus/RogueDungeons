import pygame
import GameObject


def check_button_press(buttons: list[GameObject.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos):
            button.buttonFunc()
