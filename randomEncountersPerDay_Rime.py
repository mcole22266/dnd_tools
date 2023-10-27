from utils.dice import rollDice

UNLIKELY: bool = False
LIKELY: bool = False

wildernessEncounterTable: dict = {
    1: 'Two encounters',
    2: 'Two encounters',
    3: 'One encounter in the morning (dawn to noon)',
    4: 'One encounter in the afternoon (noon to dusk)',
    5: 'One encounter in the evening (dusk to midnight)',
    6: 'One encounter at night (midnight to dawn)',
    7: 'No random encounter',
    8: 'No random encounter'
}


def fetchWildernessEncounter() -> str:
    # Roll twice to handle likelihood options
    rolls = [rollDice(8) for _ in range(2)]

    if LIKELY:
        # pick lower roll
        result: str = min(rolls)
    elif UNLIKELY:
        # pick highest roll
        result: str = max(rolls)
    else:
        # pick first roll
        result: str = rolls[0]

    output: str = wildernessEncounterTable[result]

    # Handle double encounter result
    if result in [1, 2]:
        resultFirstEncounter: str = rollDice(4) + 2
        resultSecondEncounter: str = rollDice(4) + 2

        # Sort results into correct order
        results: list = sorted([
            resultFirstEncounter,
            resultSecondEncounter
        ])

        outputs: list = [
            wildernessEncounterTable[res] for res in results
        ]

        output += f': {outputs[0]} and {outputs[1]}'

    return output


if __name__ == '__main__':
    # Get number of days to roll from user
    numDays: str = input('Number of days to roll encounters for: ')
    # Convert to integer
    try:
        numDays: int = int(numDays)
    except ValueError:
        print('Input was not an integer. Try again.')
        quit()

    # Get day number to start on
    dayStart: str = input('What day do you want to begin with? ')
    # Convert to integer
    try:
        dayStart: int = int(dayStart)
    except ValueError:
        print('Input was not an integer. Try again.')
        quit()

    for i in range(numDays):
        encounter = fetchWildernessEncounter()
        print(f'**Day {dayStart + i}.** {encounter}')
