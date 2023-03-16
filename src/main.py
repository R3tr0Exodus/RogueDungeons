
import pygame
import GameObject
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects


def open_inv():
    pass


def start_attack():
    pass


def continue_dungeon():
    pass


def use_item():
    pass


if __name__ == "__main__":
    window = WindowRenderer(50, 50)
    window.set_background_color(255, 0, 255)

    Jeffrey = GameObject.Player(50, 0, pygame.Rect(50, 50, 500, 500), Layers.ENTITIES)

    # Create UI buttons
    buttons = [
        GameObject.UiButton(open_inv, pygame.Rect(750, 550, 100, 100), Layers.UI),         # Inventory button
        GameObject.UiButton(start_attack, pygame.Rect(200, 550, 450, 100), Layers.UI)      # Attack button

    ]

    running = True
    while running:
        update_gameobjects([Jeffrey, buttons], window=window)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                match event:
                    case pygame.K_ESCAPE:
                        running = False

                    # Add more buttons later, perhaps shortcuts?

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    check_button_press(buttons, pygame.mouse.get_pos())


pygame.quit()
