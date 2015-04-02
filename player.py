class Player(object):
    playerName = ""
    injury = ""
    position = ""
    team = ""
    opponent = ""
    salary = 0
    fppg = 0
    wpv = 0

    def __init__(self, playerName, injury, position, team, opponent, salary, fppg, wpv):
        self.playerName = playerName
        self.injury = injury
        self.position = position
        self.team = team
        self.opponent = opponent
        self.salary = salary
        self.fppg = fppg
        self.wpv = wpv