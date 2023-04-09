import pygame
from pygame.locals import *
import GameObject as Objects
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects, coords
import manager
from manager import DungeonManager, TurnManager


# Button functions
def open_inv():
    print('opened inventory')


def start_attack():
    if TurnManager.playerToMove:
        TurnManager.attack_enemy()


def continue_dungeon():
    if DungeonManager.currentRoom.isCleared:
        print('continued in dungeon')
        DungeonManager.advance_dungeon()
    else:
        print("!!ACCESS DENIED!!")


def use_item():
    print('used item')


def start_main_menu():
    manager.UI.MainMenu.show()

    while manager.UI.MainMenu.isShowing:
        update_gameobjects(window)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                manager.UI.MainMenu.isShowing = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttons = [obj for obj in Objects.GameObject.instancelist
                               if 'UiButton' in obj.__class__.__name__]  # gets a list of all classes named 'UiButton'

                    check_button_press(buttons, pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            manager.UI.MainMenu.isShowing = False
            pygame.quit()
    manager.UI.MainMenu.hide()


def run_game():
    running = True

    # Entities
    Jeffrey = Objects.Player("Jeffrey", 50, 10, coords.CENTER[0] - 100, center[1] + 100, 10, Layers.ENTITIES)
    Jeffrey.baseHealth = 250
    Jeffrey.health = 250

    # Managers
    DungeonManager.init(Jeffrey)
    DungeonManager.add_rnd_room(10)
    TurnManager.init(Jeffrey, window)

    # Buttons
    invButton = Objects.UiButton(open_inv, center[0] + 300, center[1] + 300, 0.2, Layers.UI)
    attButton = Objects.UiButton(start_attack, center[0] - 450, center[1] + 300, 0.2, Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, center[0] - 75, center[1] - 300, 0.2, Layers.UI)

    while running:
        window.draw.background('../sprites/Cobble_Wall.png', 10)
        window.draw.room(manager.DungeonManager)
        update_gameobjects(window)
        TurnManager.draw_hp(Jeffrey, DungeonManager.currentRoom.enemies[0])

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


# Main
if __name__ == "__main__":
    pygame.init()

    window = WindowRenderer((pygame.SHOWN | pygame.FULLSCREEN))
    window.set_background_color(255, 0, 255)
    coords.set_coords(window)
    center = coords.CENTER

    start_main_menu()
    run_game()


pygame.quit()
