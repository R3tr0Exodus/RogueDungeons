import pygame


class GameObject(object):
    instancelist = []  # keep track of all gameobjects

    def __init__(self, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 visible: bool = True):
        self._sprite = pygame.image.load(spritePath)
        self._layer = layer
        self.visible = visible

        self._sprite = pygame.transform.scale(self._sprite,
                                              (self._sprite.get_rect().width * scale,
                                               self._sprite.get_rect().height * scale))

        self.rect = pygame.Rect(xPos * scale, yPos * scale, self._sprite.get_rect().width, self._sprite.get_rect().height)

        GameObject.instancelist.append(self)
        GameObject.instancelist.sort(key=lambda gameOBJ: gameOBJ.layer, reverse=True)

    @property
    def sprite(self):
        return self._sprite

    @property
    def layer(self):
        return self._layer

    def remove(self):
        GameObject.instancelist.remove(self)

    def __del__(self):
        if self in GameObject.instancelist:
            self.remove()

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    def __init__(self, weight: int, type: str, value: int):
        self.weight = weight
        self.type = type
        self.value = value


class Buff(GameObject):
    pass


class Entity(GameObject):
    def __init__(self, name: str, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 visible=True):
        super().__init__(xPos, yPos, scale, layer, spritePath, visible)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg
        self.name = name

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        self.remove()


class Enemy(Entity):
    def __init__(self, name: str, room, baseHealth, baseDmg, debuff, xPos, yPos, scale, layer: int,
                 spritePath="../sprites/Jerry_sprite.png", visible=True):
        super().__init__(name, baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath, visible)
        self.__debuff: Buff = debuff
        self.__room = room

    @property
    def debuff(self):
        return self.__debuff

    def attack(self, player: Entity):
        attack_dmg = self.baseDmg
        player.health -= attack_dmg

    def die(self):
        self.remove()
        # Sets the enemy to the back of the list
        self.__room.enemies.remove(self)
        self.__room.enemies.append(self)


class Skeleton(Enemy):
    spritePath = "../sprites/Skeleton_sprite.png"
    baseHealth = 30
    baseDmg = 2
    debuff = 10

    def __init__(self, room, xPos, yPos, scale, layer: int):
        super().__init__("skeleton", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, scale, layer,
                         self.spritePath, visible=False)


class Goblin(Enemy):
    spritePath = "../sprites/Goblin_sprite.png"
    baseHealth = 20
    baseDmg = 20
    debuff = 10

    def __init__(self, room, xPos, yPos, scale, layer: int):
        super().__init__("goblin", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, scale, layer,
                         self.spritePath, visible=False)


class Witch(Enemy):
    spritePath = "../sprites/Goblin_sprite.png"
    baseHealth = 25
    baseDmg = 5
    debuff = 10

    def __init__(self, room, xPos, yPos, scale, layer: int):
        super().__init__("witch", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, scale, layer,
                         self.spritePath, visible=False)


class Player(Entity):
    def __init__(self, name: str, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 visible=True):
        super().__init__(name, baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath, visible)

        self.__inventory: list[Item] = []
        for i in range(0, 11):
            self.__inventory.append(Item(0, 'empty', 0))

        self.attackItem: Item = Item(1, 'bob', 1)
        self.defensiveItem: Item = Item(2, 'dick', 1)
        self.attackBuffs: list[Buff]
        self.defensiveBuffs: list[Buff]
        self.usingInv = False

    def update(self):
        pass

    def get_inventory(self):
        return self.__inventory

    def add_inventory(self, item: Item):
        self.__inventory.append(item)

    def use_item(self):
        pass

    def set_attack_item(self, index):
        self.__inventory.insert(index, self.attackItem)
        self.attackItem = self.__inventory.pop(index+1)

    def set_def_item(self, index):
        self.__inventory.insert(index, self.defensiveItem)
        self.defensiveItem = self.__inventory.pop(index+1)


class UiButton(GameObject):

    def __init__(self, buttonFunc, xPos, yPos, scale, layer: int, sprite=None, visible=True):
        if sprite is None:
            super().__init__(xPos, yPos, scale, layer, visible=visible)
        else:
            super().__init__(xPos, yPos, scale, layer, sprite, visible)

        self.__buttonFunc = buttonFunc
        self.isActive = True

    def on_press(self):
        if self.isActive:
            self.__buttonFunc()
