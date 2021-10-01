from random import choice
from utils.dice import rollDice

class Character:

    def __init__(self, name, str, dex, con, int, wis, cha, ac, hp, initiative, log=True):
        self.name = name
        self.log = log

        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

        self.ac = ac
        self.hp = hp
        self.hp_max = hp
        self.initiative = initiative

        self.dead = False
        self.attacks = []

        if self.log:
            print(f'{self.name}: AC: {self.ac}: HP: {self.hp}')

    def attack(self):
        attack = choice(self.attacks)
        attack = attack()

        if self.log:
            print(f'{self.name} {attack["Flavor"]}')

        return attack

    def rollInitiative(self):
        rolled = rollDice(20, 1, self.initiative)

        if self.log:
            print(f'{self.name} rolled {rolled} for initiative')

        return rolled

    def takeDamage(self, amt):
        if self.log:
            print(f'{self.name} takes {amt} damage')

        self.hp -= amt

        if self.hp <= 0:
            self.dead=True
            if self.log:
                print(f'{self.name} has died')
