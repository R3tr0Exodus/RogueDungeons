from GameObject import Item
from Utility import ItemType

useables = [

]

common = [
    Item(2, ItemType.DEFENCE, 11, '../sprites/Item/Defence/Cursed_Armor.png'),
    Item(2, ItemType.ATTACK, 14, '../sprites/Item/Attack/Cleaver.png'),
]

epic = [
    Item(4, ItemType.ATTACK, 21, '../sprites/Item/Attack/Cleaver_Poison.png'),
    Item(3, ItemType.DEFENCE, 19, '../sprites/Item/Defence/Cursed_Armor_2.png'),
]

legendary = [
    Item(6, ItemType.DEFENCE, 27, '../sprites/Item/Defence/Cursed_Armor_3.png'),

]

ascended = [
    Item(9, ItemType.DEFENCE, 48, '../sprites/Item/Defence/Cursed_Armor_4.png'),

]