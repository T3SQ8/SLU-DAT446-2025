from random import randint

class Item():
    def __init__(self, name, rarity, weight, model):
        self.name = name
        self.rarity = rarity
        self.weight = weight
        self.model = model
        self.owner = None

    def __repr__(self):
        return f"{self.name}, {self.rarity} item: {self.weight} kg, Model: {self.model}, Owner: {self.owner}"

class Food(Item):
    def __init__(self, name, rarity, weight, model, eating_time, health_gain):
        super().__init__(name, rarity, weight, model)
        self.eating_time = eating_time
        self.health_gain = health_gain

        def __repr__(self):
            return super().__repr__() + f", Type: Food, HP Gain: {self.health_gain}, Eating Time: {self.eating_time}"

class Weapon(Item):
    def __init__(self, name, rarity, weight, model, range, min_damage, max_damage):
        super().__init__(name, rarity, weight, model)
        self.range = range
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self) -> int:
        return randint(self.min_damage, self.max_damage)
    
    def __repr__(self):
        # Skulle gå att skriva om den helt från början istället men det är mer "skalbart"
        return super().__repr__() + f", Type: Weapon, Range: {self.range}, Minimum Damage: {self.min_damage}, Maximum Damage: {self.max_damage}"
    
class Armour(Item): 
    def __init__(self, name, rarity, weight, model, absorption_chance, durability):
        super().__init__(name, rarity, weight, model)

        self.absorption_chance = absorption_chance
        self.max_durability = durability
        self.current_durability = durability

    def hit(self, incoming_damage: int) -> int:
        chance_roll = randint(1, 100)
        
        if chance_roll < self.absorption_chance:
            self.current_durability -= 1
            return 0

        return incoming_damage

    def __repr__(self):
        return super().__repr__() + f", Type: Armour, Absorption chance: {self.absorption_chance}%, Max Durability: {self.max_durability}, Current Durability: {self.current_durability}"

# Endast för testning
if __name__ == "__main__":
    testItem = Item("Test", "Common", 5, "path.jpg")

    print(testItem)

    testWeapon = Weapon("Test", "Rare", 5, "path.jpg", 50, 100, 200)

    print(testWeapon)