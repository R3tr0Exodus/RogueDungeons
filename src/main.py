import pygame
from pygame.locals import *
import GameObject as Objects
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects, toggle_inv
import manager


def open_inv():
    print('opened inventory')


def start_attack():
    print('ATTAAACK')


def continue_dungeon():
    print('continued in dungeon')


def use_item():
    print('used item')


if __name__ == "__main__":
    pygame.init()

    window = WindowRenderer((pygame.SHOWN | pygame.FULLSCREEN), 2560, 1440)
    window.set_background_color(255, 0, 255)
    centerPX = window.get_center()
    center = tuple([coord/10 for coord in centerPX])

    # Entities
    Jeffrey = Objects.Player(50, 0, center[0] - 100, center[1] + 100, 10, Layers.ENTITIES)
    Jeffrey.baseHealth = 25
    Jeffrey.health = 1

    # Managers
    turnManager = manager.TurnManager(Jeffrey, [], window)

    # Buttons
    invButton = Objects.UiButton(lambda: toggle_inv(Jeffrey, invButton, (invBackground, attInvSlot, defInvSlot)), center[0] + 40, center[1] + 16, 10, Layers.UI, "../sprites/Backpack.png")
    attButton = Objects.UiButton(start_attack, center[0] - 450, center[1] + 200, 0.2, Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, center[0] - 75, center[1] - 300, 0.2, Layers.UI)

    # UI Elements
    invBackground = Objects.GameObject(center[0] - 40, center[1] - 15, 10, Layers.UI, '../sprites/Inventroy_backdrop.png', visible=False)
    attInvSlot = Objects.GameObject(center[0] - 20, center[1] - 28, 10, Layers.UI, '../sprites/Inventroy_tile_gold.png', visible=False)
    defInvSlot = Objects.GameObject(center[0] + 10, center[1] - 28, 10, Layers.UI, '../sprites/Inventroy_tile_gold.png', visible=False)

    running = True
    while running:
        window.draw.background('../sprites/Cobble_Wall.png', 10)
        update_gameobjects(window)
        turnManager.draw_hp(Jeffrey, Jeffrey)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttons = [obj for obj in Objects.GameObject.instancelist
                               if 'UiButton' in obj.__class__.__name__]  # gets a list of all classes named 'UiButton'

                    check_button_press(buttons, pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False


pygame.quit()
