import GameObject


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

    def __init__(self, player: GameObject.Player, enemy_list: list[GameObject.Entity]):
        self.player = player
        self.enemies = enemy_list

    def next_turn(self):
        self.turnIndex += 1

