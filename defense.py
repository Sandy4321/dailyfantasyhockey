class Defense(object):
    name = ""
    team = ""
    fpts = 0
    gp = 0
    fpts_g = 0.0
    sack = 0
    fr = 0
    ints = 0
    td = 0
    sfty = 0
    ryda = 0
    pyda = 0
    tyda = 0

    def __init__(self, name, team, fpts, gp, fpts_g, sack, fr, ints, td, sfty, ryda, pyda, tyda):
        self.name = name
        self.team = team
        self.fpts = fpts
        self.gp = gp
        self.fpts_g = fpts_g
        self.sack = sack
        self.fr = fr
        self.ints = ints
        self.td = td
        self.sfty = sfty
        self.ryda = ryda 
        self.pyda = pyda
        self.tyda = tyda