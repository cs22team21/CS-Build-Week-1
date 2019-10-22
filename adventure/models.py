from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()

class Character(Player):
    def __init__(self, name):
        self.level = 1
        self.inventory = []
        self.name = name

class Cyborg_Warrior(Character):
    def __init__(self, name):
        self.strength = 5
        self.stamina = 5
        self.max_HP = 5 * self.stamina
        self.HP = 5 * self.stamina
        self.rage = 0
        super().__init__(name)
    
    def basic_attack(self, target):
        self.rage += self.strength*2
        target.HP -= self.strength + 2
        print(f"Cyborg Warrior swings at {target.name} and does {self.strength + 2} damage.")
    
    def slam(self, target):
        if self.rage >= 20:
            self.rage -= 20
            print(f"Cyborg Warrior winds up and performs an overhead slam on {target.name} dealing {self.strength * 4 + 1} damage")
            target.HP -= self.strength * 4 + 1

class Tech_Mage(Character):
    pass

class Enemy:
    def __init__(self, name):
        self.name = name

class Rat(Enemy):
    def __init__(self, name):
        self.level = 1
        self.max_HP = 15
        self.HP = 15
        self.strength = 3
        super().__init__(name)
    
    def bite(self, target):
        target.HP -= self.strength
        print(f"Rat bites deep into {target}'s skin and deals {self.strength} damage.")




