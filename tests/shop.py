from hero import Hero
from shop_item import SmallHealingPotion, WeaponUpgrade, BigHealingPotion

class Shop:
    def __init__(self,filename):
        self.filename=filename
        f = open(filename)
        lines = f.readlines()
        self.items=list()
        for line in lines:
            line=line.strip('\n')
            self.items.append(line)

    #print the items in the shop 
    def __str__(self):
        message=list()
        message.append('Welcome to the shop. The following items are available:')
        for itemIdex in range(len(self.items)):
            if self.items[itemIdex] == SmallHealingPotion.name:
                message.append(f'{itemIdex+1} - {SmallHealingPotion()}')
            elif self.items[itemIdex] == BigHealingPotion.name:
                message.append(f'{itemIdex+1} - {BigHealingPotion()}')
            elif self.items[itemIdex] == WeaponUpgrade.name:
                message.append(f'{itemIdex+1} - {WeaponUpgrade()}')
        return '\n'.join(message)

    #give the number of items in the shop
    def __len__(self):
        return len(self.items)
        


    @property
    def available_items(self):
        return self.items

    #buy function
    def buy(self,index):
        #test the index whether exceed the range
        if 0 <= index and index <= len(self.items)-1:
            #delete the item after buy it
            if self.items[index] == BigHealingPotion.name:
                del self.items[index]
                return BigHealingPotion()
            #delete the item after buy it
            elif self.items[index] == SmallHealingPotion.name:
                del self.items[index]
                return SmallHealingPotion()
            #Weaponupgrade will not keep this time
            elif self.items[index] == WeaponUpgrade.name:
                del self.items[index]
                return WeaponUpgrade()
        else:
            raise IndexError('out of range')

    

if __name__=='__main__':
    shop=Shop('tests/test_shop.txt')
    benny = Hero('benny')
    message = '\n'.join([
        "Welcome to the shop. The following items are available:",
        "1 - small healing potion (1 gold)",
        "2 - big healing potion (3 gold)",
        "3 - small healing potion (1 gold)",
        "4 - small healing potion (1 gold)",
        "5 - weapon upgrade (1 gold)",
    ])
    print(shop.items[0][0])

    


