import GameObject as Objects


class Room:
    def __init__(self):
        self.enemies: list[Objects.Entity] = None
        self.hasTreasure: bool = False
        self.loot: list[Objects.Item] = []


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

    def __init__(self, player: Objects.Player, enemy_list: list[Objects.Entity]):
        self.player = player
        self.enemies = enemy_list

    def next_turn(self):
        self.turnIndex += 1

