import pygame


class GameObject(object):
    instancelist = []  # keep track of all gameobjects

    def __init__(self, xPos, yPos, scale, layer: int, spritePath="../sprites/Error_Placeholder.png", visible: bool=True):
        self.sprite = pygame.image.load(spritePath)
        self.layer = layer
        self.visible = visible

        self.sprite = pygame.transform.scale(self.sprite,
                                             (self.sprite.get_rect().width * scale,
                                              self.sprite.get_rect().height * scale))

        self.rect = pygame.Rect(xPos * scale, yPos * scale, self.sprite.get_rect().width, self.sprite.get_rect().height)

        GameObject.instancelist.append(self)
        GameObject.instancelist.sort(key=lambda gameOBJ: gameOBJ.layer, reverse=True)

    def __del__(self):
        GameObject.instancelist.remove(self)

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name


class Buff(GameObject):
    pass


class Entity(GameObject):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png", visible=True):
        super().__init__(xPos, yPos, scale, layer, spritePath, visible)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("ouchie!")


class Player(Entity):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png", visible=True):
        super().__init__(baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath, visible)

        self.__inventory: list[Item] = []
        self.attackItem: Item = Item()
        self.defensiveItem: Item = Item()
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

    def on_press(self):
        self.__buttonFunc()
