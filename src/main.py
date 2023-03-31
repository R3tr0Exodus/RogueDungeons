import pygame
from pygame.locals import *
import GameObject as Objects
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects
import manager


def open_inv():
    print('opened inventory')


def start_attack():
    print('ATTAAACK')


def continue_dungeon():
    print('continued in dungeon')
    manager.DungeonManager.advance_dungeon()


def use_item():
    print('used item')


if __name__ == "__main__":
    pygame.init()

    manager.DungeonManager.add_rnd_room(10)

    window = WindowRenderer((pygame.SHOWN | pygame.FULLSCREEN))
    window.set_background_color(255, 0, 255)
    center = window.get_center()

    # Entities
    Jeffrey = Objects.Player(50, 0, center[0] - 100, center[1] + 100, 10, Layers.ENTITIES)
    Jeffrey.baseHealth = 25
    Jeffrey.health = 1

    # Managers
    turnManager = manager.TurnManager(Jeffrey, [], window)

    # Buttons
    invButton = Objects.UiButton(open_inv, center[0] + 300, center[1] + 300, 0.2, Layers.UI)
    attButton = Objects.UiButton(start_attack, center[0] - 450, center[1] + 300, 0.2, Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, center[0] - 75, center[1] - 300, 0.2, Layers.UI)

    running = True
    while running:
        window.draw.background('../sprites/Cobble_Wall.png', 10)
        window.draw.room(manager.DungeonManager)
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
