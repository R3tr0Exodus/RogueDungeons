from GameObject import Item
from Utility import ItemType

common = [
    Item(3, ItemType.DEFENCE, 11, '../sprites/Item/Defence/Cursed_Armor.png'),
    Item(2, ItemType.ATTACK, 24, '../sprites/Item/Attack/Cleaver.png'),
]

epic = [
    Item(2, ItemType.ATTACK, 21, '../sprites/Item/Attack/Cleaver_Poison.png'),
    Item(3, ItemType.DEFENCE, 19, '../sprites/Item/Defence/Cursed_Armor2.png'),
]

legendary = [
    Item(3, ItemType.DEFENCE, 27, '../sprites/Items/Defence/Cursed_Armor3.png'),

]

ascended = [
    Item(3, ItemType.DEFENCE, 48, '../sprites/Items/Defence/Cursed_Armor4.png'),

]