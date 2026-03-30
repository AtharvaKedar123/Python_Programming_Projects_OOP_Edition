from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def use(self, target):
        pass

    def __str__(self):
        return self.name


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def use(self, target):
        print(f"{self.name} deals {self.damage} damage to {target.name}")
        target.take_damage(self.damage)

    def __add__(self, other):
        if isinstance(other, FireGem):
            return Weapon(f"Fire {self.name}", self.damage + 20)
        return self


class Potion(Item):
    def __init__(self, name, heal):
        super().__init__(name)
        self.heal = heal

    def use(self, target):
        print(f"{target.name} uses {self.name} and heals {self.heal}")
        target.heal(self.heal)


class Armor(Item):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense

    def use(self, target):
        print(f"{target.name} equips {self.name} (+{self.defense} defense)")
        target.defense += self.defense


class FireGem(Item):
    def __init__(self):
        super().__init__("Fire Gem")

    def use(self, target):
        print("Cannot use Fire Gem directly")


class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.defense = 0
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print(f"\n{self.name}'s Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i+1}. {item}")

    def use_item(self, index, target=None):
        if index < 0 or index >= len(self.inventory):
            print("Invalid choice")
            return
        if target is None:
            target = self
        self.inventory[index].use(target)

    def take_damage(self, damage):
        reduced = max(damage - self.defense, 0)
        self.health -= reduced
        print(f"{self.name} takes {reduced} damage. Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} health: {self.health}")


if __name__ == "__main__":
    player = Player("Hero")
    enemy = Player("Enemy", 120)

    sword = Weapon("Sword", 25)
    potion = Potion("Potion", 30)
    armor = Armor("Shield", 10)
    gem = FireGem()

    player.add_item(sword)
    player.add_item(potion)
    player.add_item(armor)
    player.add_item(gem)

    player.show_inventory()

    player.use_item(2)
    player.use_item(0, enemy)
    player.use_item(1)

    fire_sword = sword + gem
    print(f"\nCreated: {fire_sword.name}")
    fire_sword.use(enemy)