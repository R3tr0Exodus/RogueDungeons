import GameObject as Objects
import GameObject
from WindowRenderer import WindowRenderer
import pygame
import random
import LootTables
import Utility


class Room:
    def __init__(self):
        self.enemies: list[Objects.Enemy] = []
        self.hasTreasure: bool = False
        self.loot: list[Objects.Item] = []


class DungeonManager:
    treasureRoomPct: float = 0.33

    # Enemy pct must equal exactly 1
    skeletonPct: float = 0.33
    goblinPct: float = 0.33
    witchPct: float = 0.33

    # Room manager
    currentRoom: Room
    roomIndex: int = 0
    roomList: list[Room] = []

    # Treasure
    chestButton: Objects.UiButton

    @staticmethod
    def advance_dungeon():
        for enemy in DungeonManager.currentRoom.enemies:
            enemy.visible = False
        DungeonManager.chestButton.visible = False

        DungeonManager.roomIndex += 1
        DungeonManager.currentRoom = DungeonManager.roomList[DungeonManager.roomIndex]

    @staticmethod
    def add_rnd_room(num: int):
        chest_sprite_path = "../sprites/Chest_sprite.png"
        DungeonManager.chestButton = Objects.UiButton(DungeonManager.loot, 10, 10, 4, Utility.Layers.OBJECTS,
                                                      chest_sprite_path, False)
        for i in range(num):
            new_room: Room = Room()
            # Set room type
            if random.uniform(0, 1) <= DungeonManager.treasureRoomPct:
                new_room.hasTreasure = True

                new_room.loot = LootTables.common[random.randint(0, len(LootTables.common)-1)]
            else:
                new_room.hasTreasure = False

            # Add enemies
            enemy_number = random.uniform(0, 1)
            if enemy_number <= DungeonManager.skeletonPct:
                new_room.enemies.append(Objects.Skeleton(10, 10, 10, Utility.Layers.ENTITIES))
            elif enemy_number <= sum([DungeonManager.skeletonPct, DungeonManager.goblinPct]):
                new_room.enemies.append(Objects.Goblin(10, 10, 10, Utility.Layers.ENTITIES))
            else:
                new_room.enemies.append(Objects.Witch(10, 10, 10, Utility.Layers.ENTITIES))

            DungeonManager.roomList.append(new_room)
        DungeonManager.currentRoom = DungeonManager.roomList[0]

    @staticmethod
    def loot():
        print(f'looted {len(DungeonManager.currentRoom.loot)} item(s)')


class TurnManager:
    def __init__(self, player: GameObject.Player, enemy_list: list[GameObject.Entity], screen: WindowRenderer):
        self.player = player
        self.enemies = enemy_list
        self.__screen = screen

        self.turnIndex: int = 0
        self.__pixelSize: int = 7

        self.__healthBarSprite = pygame.image.load("../sprites/HealthBar_sprite.png")
        self.__healthBarSprite = pygame.transform.scale(self.__healthBarSprite,
                                                        (52 * self.__pixelSize, 4 * self.__pixelSize))

    def next_turn(self):
        self.turnIndex += 1

    def draw_hp(self, player: GameObject.Player, enemy: GameObject.Entity):

        player_pct = player.health / player.baseHealth * 50
        player_bar_pos = (50, self.__screen.h - 100 - 2 * self.__pixelSize)
        self.__screen.draw.sprite(self.__healthBarSprite, pygame.Rect(player_bar_pos[0],
                                                                      player_bar_pos[1], 52, 4))
        self.__screen.draw.rect((255, 0, 0), pygame.Rect(player_bar_pos[0] + self.__pixelSize,
                                                         player_bar_pos[1] + self.__pixelSize,
                                                         player_pct * self.__pixelSize, 2 * self.__pixelSize))

        enemy_pct = enemy.health / enemy.baseHealth * 50
        enemy_bar_pos = (self.__screen.w - 50 - 52 * self.__pixelSize, 50)
        self.__screen.draw.sprite(self.__healthBarSprite, pygame.Rect(enemy_bar_pos[0],
                                                                      enemy_bar_pos[1], 52, 4))
        self.__screen.draw.rect((255, 0, 0), pygame.Rect(enemy_bar_pos[0] + self.__pixelSize,
                                                         enemy_bar_pos[1] + self.__pixelSize,
                                                         enemy_pct * self.__pixelSize, 2 * self.__pixelSize))
