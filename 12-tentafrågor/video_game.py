class Player:
    def __init__(self, name, health=100, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def get_health(self):
        return self.health

    def get_attack_damage(self):
        return self.attack_power

    def attack(self, enemy):
        enemy.take_damage(self.get_attack_damage())

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0 # returns true/false

def main():
    # Create two player instances
    player1 = Player("Baldwin", health=100, attack_power=15)
    player2 = Player("Geoffrey", health=100, attack_power=12)

    print(player2.get_health())
    player1.attack(player2)
    print(player2.get_health())
    print(player2.is_alive())
    player1.attack(player2)
    player1.attack(player2)
    player1.attack(player2)
    player1.attack(player2)
    player1.attack(player2)
    player1.attack(player2)
    print(player2.is_alive())

if __name__ == "__main__":
    main()

