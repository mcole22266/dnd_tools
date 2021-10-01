from models.Character import Character
from utils.dice import rollDice

class Tiaq(Character):

    def __init__(self):
        super().__init__(
            name="Tiaq",
            str=4,
            dex=2,
            con=4,
            int=0,
            wis=1,
            cha=2,
            ac=18,
            hp=27,
            initiative=2
        )
        self.attacks = [self.attackLongsword]
        self.healing = [
            self.secondWind,
            self.cureWounds,
            self.cureWounds,
            self.cureWounds
        ]
        self.fighter_level = 2
        self.proficiency = 2
        self.spell_casting_mod = 0
        self.hard_to_kill_slots = 1
        self.action_surge_slots = 1

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

    def takeDamage(self, amt):
        # Check if would die
        if self.hp - amt <= 0:
            # If would die, check if any hard_to_kill_slots_left
            if self.hard_to_kill_slots > 0:
                # If hard_to_kill_slots then use it to reduce to 1 hp after killed
                self.hp = amt + 1
                self.hard_to_kill_slots -= 1
                if self.log:
                    print(f'{self.name} is hard to kill!')
        # Pass to parent
        super().takeDamage(amt)

    def attackLongsword(self):
        toHit = rollDice(20, 1, self.proficiency+self.str)
        damage = rollDice(8, 1, self.str+self.proficiency)

        # Critical
        if toHit == 20+6:
            damage += rollDice(8)

        attack = {
            'Name': 'Longsword',
            'To Hit': toHit,
            'Damage': damage,
            'Flavor': 'swung longsword'
        }

        return attack

    def attackCrossbowLight(self):
        toHit = rollDice(20, 1, self.proficiency+self.dex)
        damage = rollDice(8, 1, self.dex)

        # Critical
        if toHit == 20+4:
            damage += rollDice(8)

        attack = {
            'Name': 'Light Crossbow',
            'To Hit': toHit,
            'Damage': damage,
            'Flavor': 'fired crossbow'
        }

        return attack

    def cureWounds(self):
        gained = rollDice(8, 1, self.spell_casting_mod)
        self.hp += gained

        attack = {
            'Name': 'Cure Wounds',
            'To Hit': 0,
            'Damage': 0,
            'Flavor': f'healed {gained} hp to {self.hp}hp'
        }

        if self.log:
            print(f'{self.name} {attack["Flavor"]}')

        return attack

    def secondWind(self):
        gained = rollDice(10, 1, self.fighter_level)
        self.hp += gained

        attack = {
            'Name': 'Second Wind',
            'To Hit': 0,
            'Damage': 0,
            'Flavor': f'healed {gained} hp to {self.hp}hp'
        }

        if self.log:
            print(f'{self.name} {attack["Flavor"]}')

        return attack
