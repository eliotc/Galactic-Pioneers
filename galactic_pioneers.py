import random

class SpaceShip:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.fuel = 100
        self.ammo = 20
    
    def travel(self, distance):
        if self.fuel >= distance:
            self.fuel -= distance
            print(f"{self.name} travels {distance} light years.")
        else:
            print(f"{self.name} does not have enough fuel to travel.")
    
    def shoot(self, target):
        if self.ammo > 0:
            self.ammo -= 1
            damage = random.randint(5, 20)
            target.take_damage(damage)
            print(f"{self.name} shoots {target.name} for {damage} damage.")
        else:
            print(f"{self.name} is out of ammo!")

class EnemyShip:
    def __init__(self, name):
        self.name = name
        self.health = 50
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} has {self.health} health left.")
        else:
            print(f"{self.name} has been destroyed!")

def encounter_enemy(ship):
    enemy = EnemyShip("Enemy Cruiser")
    while enemy.health > 0 and ship.health > 0:
        ship.shoot(enemy)
        if enemy.health > 0:
            # Enemy retaliation
            enemy_attack = random.randint(5, 15)
            ship.health -= enemy_attack
            print(f"{enemy.name} retaliates for {enemy_attack} damage.")
            if ship.health <= 0:
                print(f"{ship.name} has been destroyed!")
                break

def main():
    ship = SpaceShip("Star Voyager")
    # Simulate travel and combat
    ship.travel(10)
    encounter_enemy(ship)

if __name__ == "__main__":
    main()
