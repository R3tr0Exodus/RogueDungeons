
import pygame
import GameObject
from WindowRenderer import WindowRenderer
from Utility import check_button_press


def test_func():
    print('This was printed from a test')


if __name__ == "__main__":
    window = WindowRenderer(50, 50)
    window.set_background_color(255, 0, 255)

    Jeffrey = GameObject.Player(50, 0, pygame.Rect(50, 50, 500, 500))

    # Create UI buttons
    buttons = {
        'InvButton': GameObject.UiButton(test_func, pygame.Rect(750, 550, 100, 100)),
        'AttackButton': GameObject.UiButton(test_func(), pygame.Rect(200, 550, 450, 100))

    }

    running = True
    while running:
        window.draw_game_object(Jeffrey.sprite, Jeffrey.rect)
        window.draw_game_object(buttons['InvButton'].sprite, buttons['InvButton'].rect)
        window.draw_game_object(buttons['AttackButton'].sprite, buttons['AttackButton'].rect)
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
                    check_button_press(buttons, mousePos=pygame.mouse.get_pos())


pygame.quit()
