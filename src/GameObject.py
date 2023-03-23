import pygame


class GameObject(object):
    instancelist = []  # keep track of all gameobjects

    def __init__(self, xPos, yPos, scale, layer: int, spritePath="../sprites/Error_Placeholder.png",
                 visible: bool = True):
        self._sprite = pygame.image.load(spritePath)
        self._layer = layer
        self.visible = visible

        self._sprite = pygame.transform.scale(self._sprite,
                                             (self._sprite.get_rect().width * scale,
                                              self._sprite.get_rect().height * scale))

        self.rect = pygame.Rect(xPos, yPos, self._sprite.get_rect().width, self._sprite.get_rect().height)

        GameObject.instancelist.append(self)
        GameObject.instancelist.sort(key=lambda gameOBJ: gameOBJ.layer, reverse=True)

    @property
    def sprite(self):
        return self._sprite

    @property
    def layer(self):
        return self._layer


    def update(self):
        pass

    def start(self):
        pass

    def remove(self):
        GameObject.instancelist.remove(self)


class Item(GameObject):
    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name


class Buff(GameObject):
    pass


class Entity(GameObject):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 visible=True):
        super().__init__(xPos, yPos, scale, layer, spritePath, visible)
        self.health = self.baseHealth = baseHealth
        self.dmg = self.baseDmg = baseDmg

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print('auuuu')
        self.remove()


class Enemy(Entity):

    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 debuff: Buff = Buff(), visible=True):
        super().__init__(baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath, visible)
        self.__debuff: Buff = debuff

    @property
    def debuff(self):
        return self.__debuff


class Player(Entity):
    def __init__(self, baseHealth, baseDmg, xPos, yPos, scale, layer: int, spritePath="../sprites/Jerry_sprite.png",
                 visible=True):
        super().__init__(baseHealth, baseDmg, xPos, yPos, scale, layer, spritePath, visible)

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

    def __init__(self, buttonFunc, xPos, yPos, scale, layer: int, sprite=None, visible=True):
        if sprite is None:
            super().__init__(xPos, yPos, scale, layer, visible=visible)
        else:
            super().__init__(xPos, yPos, scale, layer, sprite, visible)

        self.__buttonFunc = buttonFunc

    def on_press(self):
        self.__buttonFunc()
