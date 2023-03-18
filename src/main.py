
import pygame
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


def use_item():
    print('used item')


if __name__ == "__main__":
    pygame.init()
    window = WindowRenderer(50, 50, (pygame.FULLSCREEN | pygame.SHOWN))
    window.set_background_color(255, 0, 255)

    # Entities
    Jeffrey = Objects.Player(50, 0, pygame.Rect(425, 455, 100, 100), Layers.ENTITIES)
    Jeffrey.baseHealth = 25
    Jeffrey.health = 1

    # Managers
    turnManager = manager.TurnManager(Jeffrey, [], window)


    # Buttons
    invButton = Objects.UiButton(open_inv, pygame.Rect(700, 550, 100, 100), Layers.UI),
    attButton = Objects.UiButton(start_attack, pygame.Rect(125, 550, 450, 100), Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, pygame.Rect(425, 20, 150, 50), Layers.UI)

    running = True
    while running:
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
