import pygame


class GameObject(object):
    instancelist = []  # keep track of all gameobjects

    def __init__(self, xPos, yPos, scale, layer: int, spritePath="../sprites/Error_Placeholder.png"):
        self.sprite = pygame.image.load(spritePath)
        self.layer = layer

        self.sprite = pygame.transform.scale(self.sprite,
                                             (self.sprite.get_rect().width * scale,
                                              self.sprite.get_rect().height * scale))

        self.rect = pygame.Rect(xPos, yPos, self.sprite.get_rect().width, self.sprite.get_rect().height)

        GameObject.instancelist.append(self)
        GameObject.instancelist.sort(key=lambda gameOBJ: gameOBJ.layer, reverse=True)

    def __del__(self):
        GameObject.instancelist.remove(self)

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    pass


class Buff(GameObject):
    pass


class Entity(GameObject):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png"):
        super().__init__(xPos, yPos, scale, layer, spritePath)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("ouchie!")


class Player(Entity):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png"):
        super().__init__(baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath)

        self.__inventory: list[Item] = []
        self.attackItem: Item
        self.defensiveItem: Item
        self.attackBuffs: list[Buff]
        self.defensiveBuffs: list[Buff]

    def get_inventory(self):
        return self.__inventory

    def add_inventory(self, item: Item):
        self.__inventory.append(item)

    def use_item(self):
        pass


class UiButton(GameObject):

    def __init__(self, buttonFunc, xPos, yPos, scale, layer: int, sprite=None):
        if sprite is None:
            super().__init__(xPos, yPos, scale, layer)
        else:
            super().__init__(xPos, yPos, scale, layer, sprite)

        self.__buttonFunc = buttonFunc

    def on_press(self):
        self.__buttonFunc()
