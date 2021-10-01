class CombatTracker:

    def __init__(self, members=[], log=True):
        self.members = members
        self.log = log
        self.tracker = []
        self.started = False
        self.current = None
    
    def start(self):
        if self.log:
            print('Combat has started - roll initiative!')

        for member in self.members:
            initiative = member.rollInitiative()
            self.tracker.append({
                'member': member,
                'initiative': initiative
            })

        self.sortTracker()
        self.current = self.tracker[0]['member']
        self.started = True

    def clean(self):
        if self.log:
            print('Cleaning Combat Tracker')

        self.members = []
        self.tracker = []
        self.started = False
        self.current = None

    def endTurn(self):
        # cleanup dead folks
        self.removeDead()

        # Change Current 
        for i, member in enumerate(self.tracker):
            if member['member']==self.current:
                if self.tracker[i]==self.tracker[-1]:
                    self.current = self.tracker[0]['member']
                else:
                    self.current = self.tracker[i+1]['member']
                break

        if self.log:
            print(f'Current Turn: {self.current.name}')

    def addMember(self, member):
        self.members.append(member)

        if self.started:
            initiative = member.rollInitiative()
            self.tracker.append({
                'member': member,
                'initiative': initiative
            })
            self.sortTracker()

            if self.log:
                print(f'{member.name} added to combat')

    def sortTracker(self):
        self.tracker.sort(
            key = lambda member: member['initiative'],
            reverse=True
            )

    def removeDead(self):
        dead = []
        for member in self.members:
            if member.dead:
                dead.append(member)

        for member in dead:
            if self.log:
                print(f'{member.name} has been removed from combat')

            self.members.remove(member)
            for tracked in self.tracker:
                if tracked['member'] == member:
                    self.tracker.remove(tracked)
