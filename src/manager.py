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
                                                        (52 * self.__pixelSize, 4 * self.__pixelSize))

    def next_turn(self):
        self.turnIndex += 1

    def draw_hp(self, player: GameObject.Player, enemy: GameObject.Entity):

        playerPct = player.health / player.baseHealth * 50
        playerBarPos = (50, self.__screen.h - 100 - 2 * self.__pixelSize)
        self.__screen.draw_game_object(self.__healthBarSprite, pygame.Rect(playerBarPos[0], playerBarPos[1], 52, 4))
        self.__screen.draw_rect((255, 0, 0), pygame.Rect(playerBarPos[0] + self.__pixelSize, playerBarPos[1] + self.__pixelSize,
                                                         playerPct * self.__pixelSize, 2 * self.__pixelSize))

        enemyPct = enemy.health / enemy.baseHealth * 50
        enemyBarPos = (self.__screen.w - 50 - 52 * self.__pixelSize, 50)
        self.__screen.draw_game_object(self.__healthBarSprite, pygame.Rect(enemyBarPos[0], enemyBarPos[1], 52, 4))
        self.__screen.draw_rect((255, 0, 0), pygame.Rect(enemyBarPos[0] + self.__pixelSize, enemyBarPos[1] + self.__pixelSize,
                                                         enemyPct * self.__pixelSize, 2 * self.__pixelSize))


