import pygame
import GameObject as Objects
from WindowRenderer import WindowRenderer
from Utility import check_button_press, Layers, update_gameobjects, Coords, toggle_inv, check_item_select,\
                    check_change_item, update_InvPos
import manager
from manager import DungeonManager, TurnManager


# Button functions
def open_inv():
    print('opened inventory')


def start_attack():
    if TurnManager.playerToMove:
        TurnManager.attack_enemy()


def continue_dungeon():
    if DungeonManager.currentRoom.isCleared:
        print('continued in dungeon')
        DungeonManager.advance_dungeon()
    else:
        print("!!ACCESS DENIED!!")


def use_item():
    print('used item')


def start_main_menu():
    manager.UI.MainMenu.show()

    while manager.UI.MainMenu.isShowing:
        update_gameobjects(window)
        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                manager.UI.MainMenu.isShowing = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttons = [obj for obj in Objects.GameObject.instancelist
                               if 'UiButton' in obj.__class__.__name__]  # gets a list of all classes named 'UiButton'

                    check_button_press(buttons, pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            manager.UI.MainMenu.isShowing = False
            pygame.quit()
    manager.UI.MainMenu.hide()


def run_game():
    running = True

    # Entities
    Jeffrey = Objects.Player("Jeffrey", 50, 10, center[0] - 15, center[1] + 5, Layers.ENTITIES)
    Jeffrey.baseHealth = 250
    Jeffrey.health = 250

    Jeffrey.add_inventory(Objects.Item(0, 'attack', 0, '../sprites/Item/Attack/Temp_Sword.png', False))
    Jeffrey.add_inventory(Objects.Item(0, 'defence', 0, '../sprites/Item/Defence/Temp_Shield.png', False))
    Jeffrey.add_inventory(Objects.Item(0, 'attack', 0, '../sprites/Item/Attack/Temp_Sword.png', False))
    # Managers
    DungeonManager.init(Jeffrey)
    DungeonManager.add_rnd_room(10)
    TurnManager.init(Jeffrey, window)

    # UI Elements
    invBackground = Objects.GameObject(center[0] - 40, center[1] - 15, Layers.UI,
                                       '../sprites/UI/Inventroy_backdrop.png', False)
    attInvSlot = Objects.GameObject(center[0] - 20, center[1] - 28, Layers.UI, '../sprites/UI/Inventroy_tile_gold.png',
                                    False)
    defInvSlot = Objects.GameObject(center[0] + 10, center[1] - 28, Layers.UI, '../sprites/UI/Inventroy_tile_gold.png',
                                    False)

    invSlots: list[Objects.GameObject] = []
    for row in range(3):
        for column in range(4):
            invSlots.append(Objects.GameObject(center[0] - 29 + 16 * column, center[1] - 12 + 16 * row, Layers.UI,
                                               '../sprites/UI/Inventroy_tile_brown.png', False))

    # Buttons
    invButton = Objects.UiButton(lambda: toggle_inv(Jeffrey, invButton,
                                                    tuple([invBackground, attInvSlot, defInvSlot] + invSlots)),
                                 center[0] + 30, Coords.RIGHT_BOTTOM[1] - 15, Layers.UI)
    attButton = Objects.UiButton(start_attack, center[0] - 45, Coords.RIGHT_BOTTOM[1] - 15, Layers.UI)
    nxtLvlButton = Objects.UiButton(continue_dungeon, center[0] - 7, Coords.RIGHT_TOP[1] + 3, Layers.UI)

    selectedItem = 0
    update_InvPos(Jeffrey, [attInvSlot, defInvSlot] + invSlots)
    while running:
        window.draw.background('../sprites/Misc/Cobble_Wall.png', 10)
        window.draw.room(manager.DungeonManager)
        update_gameobjects(window)
        TurnManager.draw_hp(Jeffrey, DungeonManager.currentRoom.enemies[0])

        window.update()
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    buttons = Objects.GameObject.buttonList

                    check_button_press(buttons, pygame.mouse.get_pos())

                    if selectedItem != -1:
                        slotPressed = check_change_item(attInvSlot, defInvSlot, pygame.mouse.get_pos())

                        if slotPressed == 'attack' and Jeffrey.get_inventory()[selectedItem].type == 'attack':
                            Jeffrey.set_attack_item(selectedItem)
                            update_InvPos(Jeffrey, [attInvSlot, defInvSlot] + invSlots)

                        elif slotPressed == 'defence' and Jeffrey.get_inventory()[selectedItem].type == 'defence':
                            Jeffrey.set_def_item(selectedItem)
                            update_InvPos(Jeffrey, [attInvSlot, defInvSlot] + invSlots)

                    selectedItem = check_item_select(Jeffrey.get_inventory(), pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False


if __name__ == "__main__":
    pygame.init()

    window = WindowRenderer((pygame.SHOWN | pygame.FULLSCREEN))
    window.set_background_color(255, 0, 255)
    Coords.set_coords(window)
    center = Coords.CENTER

    start_main_menu()
    run_game()

pygame.quit()
