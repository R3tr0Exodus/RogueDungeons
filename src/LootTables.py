from GameObject import Item
from Utility import ItemType



useables = [

]

common = [
    Item(2, ItemType.DEFENCE, 22, '../sprites/Item/Defence/Cursed_Armor.png'),
    Item(1, ItemType.ATTACK, 23, '../sprites/Item/Attack/Cleaver.png'),
    Item(1, ItemType.DEFENCE, 25, '../sprites/Item/Attack/ItemHere(Sword)'),
    Item(2, ItemType.DEFENCE, 22, '../Sprites/Item/Defence/ItemHere(Leather)'),
    Item(1, ItemType.ATTACK, 26, '../sprites/Item/Attack/ItemHere(WoodenClub)'),
    Item(1, ItemType.ATTACK, 27, '../sprites/Item/Attack,ItemHere(TeddyBear)')
]

epic = [
    Item(1, ItemType.ATTACK, 31, '../sprites/Item/Attack/Cleaver_Poison.png'),
    Item(2, ItemType.DEFENCE, 37, '../sprites/Item/Defence/Cursed_Armor_2.png'),
    Item(1, ItemType.ATTACK, 32, '../sprites/Item/Attack/ItemHere(Mace)'),
    Item(1, ItemType.ATTACK, 39, '../sprites/Item/Attack/ItemHere(IcePike)'),
    Item(2, ItemType.DEFENCE, 35, '../sprites/Item/Defence/ItemHere(PoisonArmor)')
]

legendary = [
    Item(2, ItemType.DEFENCE, 44, '../sprites/Item/Defence/Cursed_Armor_3.png'),
    Item(2, ItemType.DEFENCE, 45, '../sprites/Item/Defence/ItemHere(Nokia)'),
    Item(1, ItemType.ATTACK, 42, '../sprites/Item/Attack/ItemHere(DirtBlock)'),
    Item(1, ItemType.ATTACK, 51, '../sprites/Item/Attack/ItemHere(HolyMace)'),
    Item(2, ItemType.DEFENCE, 49, '../sprites/Item/Defence/ItemHere(HolyArmor)')

]

ascended = [
    Item(2, ItemType.DEFENCE, 48, '../sprites/Item/Defence/Cursed_Armor_4.png'),
    Item(1, ItemType.ATTACK, 62, '../sprites/Item/Attack/ItemHere(JeffreyStick)'),
    Item(2, ItemType.DEFENCE, 65, '../sprites/Item/Defence/ItemHere(JeffreyShield)')
]
