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
    __fullHeartSprite = pygame.image.load("../sprites/Heart_sprite.png")
    __emptyHeartSprite = pygame.image.load("../sprites/EmptyHeart_sprite.png")

    __screen: WindowRenderer = None

    def __init__(self, player: GameObject.Player, enemy_list: list[GameObject.Entity], screen: WindowRenderer):
        self.player = player
        self.enemies = enemy_list
        self.__screen = screen

    def next_turn(self):
        self.turnIndex += 1

    def draw_hp(self):
        for i in range(self.player.health):
            self.__screen.draw_game_object(self.__fullHeartSprite, pygame.Rect(50 * i, 50, 50, 50))


