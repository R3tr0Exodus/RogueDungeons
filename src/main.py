
import pygame
from WindowRenderer import WindowRenderer
import GameObject


if __name__ == "__main__":
    window = WindowRenderer(50, 50)

    window.set_background_color(255, 0, 255)
    running = True

    Jeffrey = GameObject.Player(50, 0, (50, 50, 500, 500))

    while running:
        window.draw_game_object(Jeffrey.sprite, Jeffrey.rect)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

pygame.quit()

