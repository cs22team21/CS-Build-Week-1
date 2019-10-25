import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.strength = strength
        self.stamina = stamina
        self.max_HP = 5 * stamina
        self.HP = self.max_HP
        self.drops = []
    
    def health(self):
        if self.HP <= 0:
            print(f"{self.name} has 0 HP and fades into the wasteland.")
        else:
            print(f"{self.name} has {self.HP} HP remaining.")


class Rat(Enemy):
    def __init__(self, name):
        super().__init__(name, stamina = 3, strength = 3)
    
    def attack(self, target):
        damage = self.strength
        target.HP -= damage
        print(f"Rat bites deep into {target}'s skin and deals {damage} damage.")
        target.health()

class Apocalypse_Prepper(Enemy):
    def __init__(self, name):
        super().__init__(name = "Apocalypse Prepper", stamina = 4, strength = 4)
    
    def attack(self, target):
        damage = self.strength + random.randint(0,2)
        target.HP -= damage
        print(f"The Apocalypse Prepper grabs a can of black beans and tosses it at {target.name}'s head causing {damage}.")
        target.health()

class Swarm_Of_Bees(Enemy):
    def __init__(self, name):
        super().__init__(name = "Swarm of Bees", stamina = 2, strength = 3)
    
    def attack(self, target):
        hit_chance = random.randint(1,10)
        if hit_chance > 8:
            print(f"The bees fly away satisfied with the damage their lack of pollination has left behind.")
            target.HP = 0
        elif hit_chance > 2:
            target.HP -= 3
            self.HP -= 3
            print(f"The bees attack in unison, leaving their stingers in {target.name} and their bodies on the floor. *cue Drowning Pool*")
        else:
            target.HP -= 1
            self.HP -= 1
            print("The bees lose sight of their target and only a few land blows!")
        target.health()

class Toxic_Avenger(Enemy):
    def __init__(self, name):
        super().__init__(name = "Toxic Avenger", stamina = 15, strength = 5)

    def attack(self, target):
        hit_chance = random.randint(1, 10)
        if hit_chance > 7:
            damage = self.strength * 2
            target.HP += damage
            print(f"The Toxic Avenger splits into two and the twins swing repeatedly at {target.name} dealing {damage} damage! Toxic Avenger recombines after the barrage.")
            target.health()
        elif hit_chance > 2:
            damage = self.strength
            target.HP += damage
            print(f"The Toxic Avenger punches {target.name} in the face with both fists causing {damage} damage.")
            target.health()
        else:
            print(f"The Toxic Avenger misses their attack!")