def main():
    # Replace with your list of encounters
    encounters: str = [
        'Raging Blizzard',
        'Giant on Mammoth',
        'Ancient White Dragon Sighting',
        'Nautiloid Crash',
        'Axebeak Issues',
        'Many-Arrows Tribe of Orcs',
        'Awakened Wolves',
        'Harpies',
        'Saber-Toothed Tigers',
        'Duergar Mining Chardalyn'
    ]

    rankedEncounters: list = rankEncounters(encounters)

    print("Encounters ranked from most likely to least likely:")
    for rank, encounter in enumerate(rankedEncounters, start=1):
        print(f"{rank}. {encounter}")

    # Make a table
    printTable(rankedEncounters)


def getUserPreference(item1: str, item2: str) -> int:
    while True:
        choice = input(
            f"Which is more likely: '{item1}' or '{item2}'? "
        )
        if choice in ('1', '2'):
            return int(choice)


def rankEncounters(encounters: list) -> list:
    encounterRanks: dict = {encounter: 0 for encounter in encounters}
    n = len(encounters)

    for i in range(n):
        for j in range(i + 1, n):
            preference: int = getUserPreference(encounters[i], encounters[j])
            if preference == 1:
                encounterRanks[encounters[i]] += 1
            else:
                encounterRanks[encounters[j]] += 1

    sortedEncounters: list = sorted(
        encounterRanks, key=lambda x: encounterRanks[x], reverse=True
    )
    return sortedEncounters


def printTable(rankedEncounters: list) -> None:
    # Get Dice roll for list in form of 1d20
    format = input('What is the dice format? (Ex: 3d4): ')

    minimum = int(format.split('d')[0])

    bellCurveList: list = []
    for i, encounter in enumerate(rankedEncounters, start=minimum):
        if (i) % 2 == 1:
            bellCurveList.append(encounter)
        else:
            bellCurveList.insert(0, encounter)

    print(f'| {format} | encounter |')
    print('| - | - |')
    for i, encounter in enumerate(bellCurveList, start=minimum):
        print(f'| {i} | {encounter} |')


if __name__ == "__main__":
    main()
