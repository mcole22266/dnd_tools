from math import floor


class Scores:

    def __init__(self, scores: list):
        """
        """
        self.scores = scores
        self.buildScores()

    def buildScores(self):
        """
        """
        if not len(self.scores) == 6:
            raise Exception(
                f"{len(self.scores)} scores passed where 6 were expected"
            )

        # Set Scores
        self.str = int(self.scores[0])
        self.dex = int(self.scores[1])
        self.con = int(self.scores[2])
        self.int = int(self.scores[3])
        self.wis = int(self.scores[4])
        self.cha = int(self.scores[5])

        self.scores = [
            self.str,
            self.dex,
            self.con,
            self.int,
            self.wis,
            self.cha
        ]


def getScores() -> Scores:
    """
    """
    scores = input("> Providing ability scores in a space-separated list\n> ")
    scores = scores.strip().split()
    return Scores(scores)


def getModifier(score: int) -> int:
    """
    """
    mod = (score - 10) / 2
    return floor(mod)


def getModifierString(score: int) -> str:
    """
    """
    modifier = getModifier(score)

    if modifier < 0:
        return modifier

    return f"+{modifier}"


def buildTable(scores: Scores) -> str:
    """
    """
    # Build header
    table = "|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|"
    table += "\n|-|-|-|-|-|-|\n"

    # Fill Row
    for score in scores.scores:
        table += f"| {score} ({getModifierString(score)}) "

    table += "|"

    return table


def main() -> None:
    """
    """
    scores = getScores()
    print(buildTable(scores))


if __name__ == '__main__':
    main()
