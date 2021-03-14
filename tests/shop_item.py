from abc import ABC, abstractmethod, abstractproperty

class ShopItem(ABC):
    @abstractproperty
    def price(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def change(self, hero):
        pass

    def __str__(self):
        return f"{self.name} ({self.price} gold)"

#inherit from the Shopietm
class BigHealingPotion(ShopItem):
    name = "big healing potion"
    price = 3
    def change(self, hero):
        hero.health = hero.health + 50

#inherit from the Shopietm
class SmallHealingPotion(ShopItem):
    name = "small healing potion"
    price = 1
    def change(self, hero):
        hero.health = hero.health + 10

#inherit from the Shopietm
class WeaponUpgrade(ShopItem):
    name = "weapon upgrade"
    price = 1
    def change(self, hero):
        hero.power = round(hero.power * 1.05, 2)

