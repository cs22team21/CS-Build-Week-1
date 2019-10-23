from .models import Player
import random

class Character(Player):
    def __init__(self, name, stamina, strength):
        self.level = 1
        self.xp = 0
        self.inventory = []
        self.name = name
        self.strength = strength
        self.stamina = stamina
        self.max_HP = 5 * self.stamina
        self.HP = self.max_HP

    def health(self):
        if self.HP <= 0:
            print(f"{self.name} has 0 HP and fades into the wasteland.")
        else:
            print(f"{self.name} has {self.HP} HP remaining.")

class Cyborg_Warrior(Character):
    def __init__(self, name):
        self.rage = 0
        super().__init__(name, stamina = 5, strength = 5)
    
    def basic_attack(self, target):
        damage = self.strength
        self.rage += damage * 2
        target.HP -=  damage
        print(f"Cyborg Warrior swings at {target.name} and does {damage} damage.")
    
    def slam(self, target):
        if self.rage >= 20:
                damage = self.strength * 3 + random.randint(0,3)
                self.rage -= 20
                target.HP -= damage
                print(f"Cyborg Warrior winds up and performs an overhead slam on {target.name} dealing {damage} damage.")
        else:
            print(f"Need more rage!")
    
    def attack(self, spell, target):
        hit_chance = random.randint(1, 10)
        spells = ["basic_attack", "slam"]
        try:
            if hit_chance > 2:
                cast = getattr(self, spells[spell])
                cast(target)
                target.health()
            else:
                print("Your attack has missed!")
        except:
            print("I have not learned this ability yet!")


class Tech_Mage(Character):
    def __init__(self, name):
        self.max_mana = 5 * self.strength
        self.mana = self.max_mana
        super().__init__(name, strength = 6, stamina = 4)

    def shoot_wand(self, target):
        damage = self.strength
        target.HP -= damage
        print(f"Tech Mage shoots a spark out of their wand at {target.name} and deals {damage} damage.")
    
    def fireworks(self, target):
        if self.mana >= 20:
            self.mana -= 20
            damage = self.strength * 4 + random.randint(1,5)
            target.HP -= damage
            print(f"{self.name} casts an explosion of light and color at {target.name} dealing {damage} damage.")
        else:
            print(f'I need more mana!')

    def attack(self, spell, target):
        hit_chance = random.randint(1, 10)
        spells = ["shoot_wand", "fireworks"]
            if hit_chance > 2:
                cast = getattr(self, spells[spell])
                cast(target)
                target.health()
            else:
                print("Your attack has missed!")
        else:
            print("I have not yet learned that ability.")
        if spell == "basic_attack":
            regen = 10
            self.mana += regen
            print(f"{self.name} has gained {regen} mana and now has {self.mana} mana.")
