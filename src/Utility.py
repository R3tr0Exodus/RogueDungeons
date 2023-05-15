import math
import GameObject as Objects
import WindowRenderer as WR


class Coords:
    CENTER: tuple
    LEFT_TOP: tuple
    RIGHT_TOP: tuple
    LEFT_BOTTOM: tuple
    RIGHT_BOTTOM: tuple

    @staticmethod
    def set_coords(window):
        Coords.CENTER = (math.floor(window.get_center()[0] / 10), math.floor(window.get_center()[1] / 10))
        Coords.LEFT_TOP = (0, 0)
        Coords.RIGHT_TOP = (math.floor(window.w / 10), 0)
        Coords.LEFT_BOTTOM = (0, math.floor(window.h / 10))
        Coords.RIGHT_BOTTOM = (math.floor(window.w / 10), math.floor(window.h / 10))


class Layers:
    ITEM = 0
    UI = 1
    VFX = 2
    ENTITIES = 3
    OBJECTS = 4
    FOREGROUND = 5
    BACKGROUND = 6


def check_button_press(buttons: list[Objects.UiButton], mousePos):
    for button in buttons:
        if button.rect.collidepoint(mousePos) and button.visible:
            button.on_press()


def check_item_select(inventory: list[Objects.Item], mousePos):
    for i, item in enumerate(inventory):
        if item.rect.collidepoint(mousePos):
            return i

    return -1


def check_change_item(atkItemSlot, defItemSlot, mousePos):
    if atkItemSlot.rect.collidepoint(mousePos):
        return "attack"
    if defItemSlot.rect.collidepoint(mousePos):
        return "defence"


def update_gameobjects(window: WR.WindowRenderer):
    for obj in Objects.GameObject.instancelist:
        obj.update()
        if obj.visible:
            window.draw.gameobject(obj)


def update_InvPos(player: Objects.Player, InvPos: list[Objects.GameObject]):
    inventory = player.get_inventory()

    for i, item in enumerate(inventory):
        item.move(InvPos[i + 2].rect.x + 10, InvPos[i + 2].rect.y + 10)

    player.attackItem.move(InvPos[0].rect.x + 10, InvPos[0].rect.y + 10)
    player.defensiveItem.move(InvPos[1].rect.x + 10, InvPos[1].rect.y + 10)


def toggle_inv(player: Objects.Player, invButton, invBackground: tuple):
    playerInv = player.get_inventory()
    player.usingInv = not player.usingInv
    buttons = [obj for obj in Objects.GameObject.instancelist
               if 'UiButton' in obj.__class__.__name__]

    for button in buttons:
        if button != invButton:
            button.visible = not button.visible

    for obj in invBackground:
        obj.visible = not obj.visible

    for i, item in enumerate(playerInv):
        # Move items inside the item spots on screen
        item.visible = not item.visible

    player.attackItem.visible = not player.attackItem.visible
    player.defensiveItem.visible = not player.defensiveItem.visible
