import pygame


class GameObject(object):
    sprite: pygame.Surface
    rect: pygame.Rect

    def __init__(self, rect: pygame.Rect, spritePath="../sprites/Error_Placeholder.png"):
        self.sprite = pygame.image.load(spritePath)
        self.sprite = pygame.transform.scale(self.sprite, (rect.width, rect.height))
        self.rect = rect

    def update(self):
        pass

    def start(self):
        pass


class Item(GameObject):
    pass


class Buff(GameObject):
    pass


class Entity(GameObject):
    health: int = 0
    baseHealth: int = 0
    dmg: int = 0
    baseDmg: int = 0
    sprite: pygame.Surface = None
    rect: pygame.Rect = None

    def __init__(self, baseHealth, baseDmg, rect, spritePath="../sprites/Jerry_sprite.png"):
        super().__init__(rect, spritePath)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print("ouchie!")


class Player(Entity):
    __inventory: list = []
    attackItem: Item = None
    defensiveItem: Item = None
    attackBuffs: Buff = []
    defensiveBuffs: Buff = []

    def get_inventory(self) -> list:
        return self.__inventory

    def add_inventory(self, item: Item):
        self.__inventory.append(item)

    def use_item(self):
        pass


class UiButton(GameObject):
    buttonFunc = None

    def __init__(self, buttonFunc, rect, sprite=None):
        if sprite is None:
            super().__init__(rect)
        else:
            super().__init__(rect, sprite)

        self.buttonFunc = buttonFunc

    def on_press(self):
        self.buttonFunc()
