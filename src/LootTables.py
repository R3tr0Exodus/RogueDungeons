from GameObject import Item
from Utility import ItemType

'''
Item name		    ItemType    Power	    Type
Jeffrey On Stick 	2 		    77	        Ascended
Sword			    2		    8	        Common
Dirt Block		    2		    32	        Legendary
Holy Mace		    2		    57	        Ascended
Ice pike		    2		    28	        Epic
Teddy Bear		    2		    7	        Common
Poison Armor		3		    31	        Epic
Holy Armor		    3		    61	        Ascended
Jeffrey on shield	3		    77	        Ascended
Nokia			    3		    78	        Ascended
Mace			    2		    25	        Epic
Wooden Club		    2		    9	        Common
Leather			    3		    12	        Common
'''

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