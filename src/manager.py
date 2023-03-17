import GameObject
from WindowRenderer import WindowRenderer
import pygame


class Room:
    enemies: list[GameObject.Entity] = None
    hasTreasure: bool = False
    loot: list[GameObject.Item] = []


class DungeonManager:
    roomIndex: int = 0
    rooms: list = []

    def __init__(self):
        pass
        #   Generate random rooms

    def advance_dungeon(self):
        self.roomIndex += 1


class TurnManager:
    turnIndex: int = 0
    player: GameObject.Player = None
    enemies: list[GameObject.Entity] = None
    __healthBarSprite = pygame.image.load("../sprites/HealthBar_sprite.png")
    __pixelSize: int = 7

    __screen: WindowRenderer = None

    def __init__(self, player: GameObject.Player, enemy_list: list[GameObject.Entity], screen: WindowRenderer):
        self.player = player
        self.enemies = enemy_list
        self.__screen = screen

        self.__healthBarSprite = pygame.transform.scale(self.__healthBarSprite,
                                                        (50 * self.__pixelSize, 4 * self.__pixelSize))

    def next_turn(self):
        self.turnIndex += 1

    def draw_hp(self, player: GameObject.Player, enemy: GameObject.Entity):
        self.__screen.draw_game_object(self.__healthBarSprite, pygame.Rect(600, 50, 50, 50))
        self.__screen.draw_rect((255, 0, 0), pygame.Rect(600 + self.__pixelSize, 50 + self.__pixelSize,
                                                         player.health * self.__pixelSize, 2 * self.__pixelSize))
        self.__screen.draw_game_object(self.__healthBarSprite, pygame.Rect(50, 500, 50, 50))
        self.__screen.draw_rect((255, 0, 0), pygame.Rect(50 + self.__pixelSize, 500 + self.__pixelSize,
                                                         enemy.health * self.__pixelSize, 2 * self.__pixelSize))


