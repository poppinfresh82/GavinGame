import random

class Player:
    def __init__(self):
        self.grand_position = 'Cabin'
        self.sub_position = 11
        self.inventory = []
        self.health = 100
        self.effects = []

class Assassin:
    # assassins spawn at level 1
    # with empty inventory and random position in the wilderness
    def __init__(self):
        self.level = 1
        self.health = 60
        self.inventory = []
        self.grand_position = 'Wilderness'
        self.sub_position = random.randint(0,9)

