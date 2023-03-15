
import pygame
from WindowRenderer import WindowRenderer
import GameObject
from Utility import check_button_press

def testFunc():
    print('This was printed from a test')


if __name__ == "__main__":
    window = WindowRenderer(50, 50)
    window.set_background_color(255, 0, 255)

    Jeffrey = GameObject.Player(50, 0, pygame.Rect(50, 50, 500, 500))
    testButton = GameObject.UiButton(testFunc, pygame.Rect(500, 200, 250, 50))

    running = True
    while running:
        window.draw_game_object(Jeffrey.sprite, Jeffrey.rect)
        window.draw_game_object(testButton.sprite, testButton.rect)
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
                    check_button_press(buttons=[testButton], mousePos=pygame.mouse.get_pos())


pygame.quit()
