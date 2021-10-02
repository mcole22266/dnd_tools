from models.Character import Character
from utils.dice import rollDice

class SirElliotRoland(Character):

    def __init__(self):
        super().__init__(
            name="Sir Elliot Roland",
            str=2,
            dex=2,
            con=2,
            int=0,
            wis=1,
            cha=1,
            ac=17,
            hp=33,
            initiative=2
        )
        self.attacks = [self.attackLongsword]
        self.healing = [
            self.drinkPotion,
        ]
        self.action_surge_slots = 3

    def attack(self):
        if self.hp <= self.hp_max/2 and len(self.healing) > 0:
            attack = self.healing.pop(0)()
            if self.action_surge_slots > 0:
                attack = super().attack()
                self.action_surge_slots -= 1
                if self.log:
                    print(f'{self.name} ACTION SURGED!')
        else:
            attack = super().attack()

        return attack

    def attackLongsword(self):
        toHit = rollDice(20, 1, 4)
        damage = rollDice(10, 1, 2)

        # Critical
        if toHit == 20+4:
            damage += rollDice(10)

        attack = {
            'Name': 'Longsword',
            'To Hit': toHit,
            'Damage': damage,
            'Flavor': 'swung longsword'
        }

        return attack

    def shortBow(self):
        toHit = rollDice(20, 1, 4)
        damage = rollDice(6, 1, 2)

        # Critical
        if toHit == 20+4:
            damage += rollDice(6)

        attack = {
            'Name': 'Short Bow',
            'To Hit': toHit,
            'Damage': damage,
            'Flavor': 'fired shortbow'
        }

        return attack

    def drinkPotion(self):
        gained = rollDice(4, 2, 2)
        self.hp += gained

        attack = {
            'Name': 'Potion of Healing',
            'To Hit': 0,
            'Damage': 0,
            'Flavor': f'healed {gained} hp to {self.hp}hp'
        }

        if self.log:
            print(f'{self.name} {attack["Flavor"]}')

        return attack
