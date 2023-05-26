import pygame


class GameObject(object):
    scale = 10
    instanceList = []  # keep track of all gameobjects
    buttonList = []  # Keep track of all buttons

    def __init__(self, xPos, yPos, layer: int, spritePath: str, visible: bool = True):
        if spritePath is None:
            self._sprite = pygame.image.load('../sprites/Entity/Jerry_sprite.png')
        else:
            self._sprite = pygame.image.load(spritePath)

        # spritePath variable necessary for copying
        self._spritePath = spritePath
        self._layer = layer
        self.visible = visible

        self._sprite = pygame.transform.scale(self._sprite,
                                              (self._sprite.get_rect().width * GameObject.scale,
                                               self._sprite.get_rect().height * GameObject.scale))

        self.rect = pygame.Rect(xPos * GameObject.scale, yPos * GameObject.scale,
                                self._sprite.get_rect().width, self._sprite.get_rect().height)

        GameObject.instanceList.append(self)
        GameObject.instanceList.sort(key=lambda gameOBJ: gameOBJ.layer, reverse=True)

    def move_pos(self, xPos, yPos):
        self.rect.x = xPos
        self.rect.y = yPos

    @property
    def sprite(self):
        return self._sprite

    @property
    def layer(self):
        return self._layer

    def remove(self):
        GameObject.instanceList.remove(self)

    def __del__(self):
        if self in GameObject.instanceList:
            self.remove()

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    def __init__(self, weight: int, itemType: int, power: int,
                 spritePath: str = '../sprites/Item/Empty_Item.png', visible: bool = False):
        super().__init__(0, 0, 0, spritePath, visible)
        self.weight = weight
        self.itemType = itemType
        self.power = power

    def __copy__(self):
        return Item(self.weight, self.itemType, self.power, self._spritePath, self.visible)


class Buff(GameObject):
    pass


class Entity(GameObject):
    def __init__(self, name: str, baseHealth, baseDmg, xPos, yPos, layer: int,
                 spritePath: str=None, visible=True):
        super().__init__(xPos, yPos, layer, spritePath, visible)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg
        self.armor = 0
        self.name = name

    def take_damage(self, damage):
        self.health -= round(damage - self.armor/100 * damage)
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        self.remove()


class Enemy(Entity):
    def __init__(self, name: str, room, baseHealth, baseDmg, debuff, xPos, yPos, layer: int,
                 spritePath: str=None, visible=True):
        super().__init__(name, baseHealth, baseDmg, xPos, yPos, layer, spritePath, visible)
        self.__debuff: Buff = debuff
        self.__room = room

    @property
    def debuff(self):
        return self.__debuff

    def die(self):
        self.remove()
        # Sets the enemy to the back of the list
        self.__room.enemies.remove(self)
        self.__room.enemies.append(self)


class Skeleton(Enemy):
    spritePath = "../sprites/Entity/Skeleton_sprite.png"
    baseHealth = 30
    baseDmg = 2
    debuff = 10

    def __init__(self, room, xPos, yPos, layer: int):
        super().__init__("skeleton", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, layer,
                         self.spritePath, visible=False)
        self.dmg = Skeleton.baseDmg
        self.health = Skeleton.baseHealth


class Goblin(Enemy):
    spritePath = "../sprites/Entity/Goblin_sprite.png"
    baseHealth = 20
    baseDmg = 20
    debuff = 10

    def __init__(self, room, xPos, yPos, layer: int):
        super().__init__("goblin", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, layer,
                         self.spritePath, visible=False)
        self.health = Goblin.baseHealth
        self.dmg = Goblin.baseDmg


class Witch(Enemy):
    spritePath = "../sprites/Entity/Goblin_sprite.png"
    baseHealth = 25
    baseDmg = 5
    debuff = 10

    def __init__(self, room, xPos, yPos, layer: int):
        super().__init__("witch", room, self.baseHealth, self.baseDmg, self.debuff, xPos, yPos, layer,
                         self.spritePath, visible=False)
        self.health = Witch.baseHealth
        self.dmg = Witch.baseDmg


class Player(Entity):
    def __init__(self, name: str, baseHealth, baseDmg, xPos, yPos, layer: int,
                 spritePath: str=None, visible=True):
        super().__init__(name, baseHealth, baseDmg, xPos, yPos, layer, spritePath, visible)

        self.__inventory: list[Item] = []
        for i in range(12):
            self.__inventory.append(Item(0, 0, 0, visible=False))

        self.attackItem: Item = Item(0, 0, 0, visible=False)
        self.defensiveItem: Item = Item(0, 0, 0, visible=False)
        self.attackBuffs: list[Buff]
        self.defensiveBuffs: list[Buff]
        self.usingInv = False

    def update(self):
        pass

    def get_inventory(self):
        return self.__inventory

    def add_item(self, newItem: Item):
        for i, item in enumerate(self.__inventory):
            # itemType 0 is an empty slot
            if item.itemType == 0:
                self.__inventory[i] = newItem
                break

    def use_item(self):
        pass

    def set_attack_item(self, index):
        self.__inventory.insert(index, self.attackItem)
        self.attackItem = self.__inventory.pop(index+1)

        # Update attack stat
        self.dmg = self.baseDmg + self.attackItem.power

    def set_def_item(self, index):
        self.__inventory.insert(index, self.defensiveItem)
        self.defensiveItem = self.__inventory.pop(index+1)

        # Update defence stat
        self.armor = self.defensiveItem.power


class UiButton(GameObject):

    def __init__(self, buttonFunc, xPos, yPos, layer: int, sprite: str=None, visible=True):
        super().__init__(xPos, yPos, layer, sprite, visible)
        self.__buttonFunc = buttonFunc
        GameObject.buttonList.append(self)

    def on_press(self):
        self.__buttonFunc()
