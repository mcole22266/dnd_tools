from models.Character import Character
from utils.dice import rollDice

class Zombie(Character):

    def __init__(self, name='Zombie'):
        super().__init__(
            name=name,
            str=1,
            dex=-2,
            con=3,
            int=-4,
            wis=-2,
            cha=-3,
            ac=8,
            hp=rollDice(8, 3, 9),
            initiative=-2
        )
        self.attacks = [self.attackSlam]

    def attackSlam(self):
        toHit = rollDice(20, 1, 3)
        damage = rollDice(6, 1, 1)

        # Critical
        if toHit == 20+3:
            damage += rollDice(6)

        attack = {
            'Name': 'Slam',
            'To Hit': toHit,
            'Damage': damage,
            'Flavor': 'slammed'
        }

        return attack
