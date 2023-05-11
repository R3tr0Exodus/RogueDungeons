import GameObject as Objects
import GameObject
from WindowRenderer import WindowRenderer
import pygame
import random
import LootTables
import Utility
from Utility import coords


class Room:
    def __init__(self):
        self.enemies: list[Objects.Enemy] = []
        self.hasTreasure: bool = False
        self.loot: list[Objects.Item] = []
        self.isCleared: bool = False


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

    # Player
    player: GameObject.Player

    # Buttons
    nextLvlButton: GameObject.UiButton

    @staticmethod
    def init(player: GameObject.Player):
        DungeonManager.player = player

    @staticmethod
    def advance_dungeon():
        for enemy in DungeonManager.currentRoom.enemies:
            enemy.visible = False
        DungeonManager.chestButton.visible = False
        DungeonManager.roomIndex += 1

        # TODO: THIS IS BAD REMOVE WHEN MAKING AN ACTUAL END
        # If there are no more rooms, print something and stop instead of error:
        if DungeonManager.roomIndex > len(DungeonManager.roomList)-1:
            pygame.quit()
            print("Sorry no more rooms big sad")
            exit()

        DungeonManager.currentRoom = DungeonManager.roomList[DungeonManager.roomIndex]
        TurnManager.turnIndex = 0

    @staticmethod
    def add_rnd_room(num: int):
        chest_sprite_path = "../sprites/Chest_sprite.png"
        DungeonManager.chestButton = Objects.UiButton(DungeonManager.loot, coords.CENTER[0]+30, coords.CENTER[1]-20,
                                                      10, Utility.Layers.OBJECTS,
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
                new_room.enemies.append(Objects.Skeleton(new_room, coords.CENTER[0] + 5, coords.CENTER[1] - 20,
                                                         10, Utility.Layers.ENTITIES))
            elif enemy_number <= sum([DungeonManager.skeletonPct, DungeonManager.goblinPct]):
                new_room.enemies.append(Objects.Goblin(new_room, coords.CENTER[0] + 5, coords.CENTER[1] - 20,
                                                       10, Utility.Layers.ENTITIES))
            else:
                new_room.enemies.append(Objects.Witch(new_room, coords.CENTER[0] + 5, coords.CENTER[1] - 20,
                                                      10, Utility.Layers.ENTITIES))

            DungeonManager.roomList.append(new_room)
        DungeonManager.currentRoom = DungeonManager.roomList[0]

    @staticmethod
    def loot():
        print(f'looted {len(DungeonManager.currentRoom.loot)} item(s)')


class TurnManager:
    # Objects
    player: Objects.Player
    enemies: list[Objects.Enemy]
    __screen: WindowRenderer

    # Turn manager
    turnIndex: int = 0
    playerToMove: bool = True

    # Healthbar
    __pixelSize = 7
    __barPixelLength = 52
    __healthBarSprite = pygame.image.load("../sprites/HealthBar_sprite.png")
    __healthBarSprite = pygame.transform.scale(__healthBarSprite,
                                               (__barPixelLength * __pixelSize,
                                                4 * __pixelSize))

    @staticmethod
    def init(player: GameObject.Player, screen: WindowRenderer):
        TurnManager.player = player
        TurnManager.__screen = screen

        TurnManager.turnIndex = 0

    @staticmethod
    def next_turn():
        if DungeonManager.currentRoom.enemies[0].health >= 1:
            TurnManager.turnIndex += 1
            TurnManager.playerToMove = TurnManager.turnIndex % 2 == 0

            if not TurnManager.playerToMove:
                TurnManager.attack_player()

        else:
            DungeonManager.currentRoom.isCleared = True

    @staticmethod
    def attack_player():
        for enemy in DungeonManager.currentRoom.enemies:
            enemy.attack(TurnManager.player)
        TurnManager.next_turn()

    @staticmethod
    def attack_enemy():
        if DungeonManager.currentRoom.enemies[0].health >= 1:
            current_enemy: Objects.Enemy = DungeonManager.currentRoom.enemies[0]
            player_dmg = DungeonManager.player.baseDmg
            current_enemy.take_damage(player_dmg)
            TurnManager.next_turn()


    @staticmethod
    def draw_hp(player: GameObject.Player, enemy: GameObject.Entity):

        def draw_bar(entity: GameObject.Entity, pos: tuple):
            health_pct = entity.health / entity.baseHealth * (TurnManager.__barPixelLength-2)
            text = f"{entity.name}: {entity.health} / {entity.baseHealth}"

            # bar
            TurnManager.__screen.draw.sprite(TurnManager.__healthBarSprite, pygame.Rect(pos[0], pos[1],
                                                                          TurnManager.__barPixelLength, 4))
            text_rect = pygame.Rect(pos[0], pos[1] - 30, TurnManager.__barPixelLength, 4)
            TurnManager.__screen.draw.text(text, text_rect)

            # bar fill
            TurnManager.__screen.draw.rect((255, 0, 0), pygame.Rect(pos[0] + TurnManager.__pixelSize,
                                                                    pos[1] + TurnManager.__pixelSize,
                                                                    health_pct * TurnManager.__pixelSize,
                                                                    2 * TurnManager.__pixelSize))

        left_pos = (coords.LEFT_BOTTOM[0] * 10 + 100,
                    coords.LEFT_BOTTOM[1] * 10 - 200)
        right_pos = (coords.RIGHT_TOP[0] * 10 - TurnManager.__pixelSize * TurnManager.__barPixelLength - 100,
                     coords.RIGHT_TOP[1] * 10 + 4 + 100)

        draw_bar(player, left_pos)
        draw_bar(enemy, right_pos)


class UI:
    class MainMenu:
        startButton: Objects.UiButton
        quitButton: Objects.UiButton
        isShowing: bool

        @staticmethod
        def show():
            UI.MainMenu.isShowing = True
            UI.MainMenu.startButton = Objects.UiButton(UI.MainMenu.start_game, 1, coords.CENTER[1]-10, 10,
                                                       Utility.Layers.UI)
            UI.MainMenu.quitButton = Objects.UiButton(UI.MainMenu.quit_game, 1, coords.CENTER[1]+10, 10,
                                                      Utility.Layers.UI)

        @staticmethod
        def hide():
            UI.MainMenu.isShowing = False
            UI.MainMenu.startButton.remove()
            UI.MainMenu.quitButton.remove()

        @staticmethod
        def start_game():
            UI.MainMenu.isShowing = False

        @staticmethod
        def quit_game():
            pygame.quit()

