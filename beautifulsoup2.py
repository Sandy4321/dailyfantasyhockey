from bs4 import BeautifulSoup # Gets Everything
import urllib2
from decimal import Decimal
from re import sub

class Player(object):
    playerName = ""
    injury = ""
    position = ""
    team = ""
    opponent = ""
    salary = 0
    fppg = 0

    def __init__(self, playerName, injury, position, team, opponent, salary, fppg):
        self.playerName = playerName
        self.injury = injury
        self.position = position
        self.team = team
        self.opponent = opponent
        self.salary = salary
        self.fppg = fppg

def make_player(playerName, injury, position, team, opponent, salary, fppg):
    player = Player(playerName, injury, position, team, opponent, salary, fppg)
    return player


#List of player html object
tr_list = []

#List of player last names
last_names = []
last_names_fin = []

#Attributes list ( will combine with name list later ) 
attributes = []


player_objects = []

page = urllib2.urlopen("http://www.rotowire.com/daily/nhl/value-report.htm")
soup = BeautifulSoup(page)
i=0
for tr in soup.findAll('tr'):
    tr_list.append(tr)
    try:
        #PUTS THE NAMES IN THE LIST
        last_names.append(tr_list[i].get_text().split(' ')[0])
        last_names[i] = last_names[i][:-1]
        #print last_names[i]

        attributes.append(tr_list[i].get_text().split(' ')[-1].split('\n'))
    except IndexError:
        continue

    i = i + 1
    #print i

for elem in last_names:
    elem = elem.lstrip()
    elem = str(elem)
  
    

del last_names[0:2]
del attributes[0:2]

for name in last_names:
    real_name = name.split('\n')[-1]
    #print real_name
    real_name = real_name.encode('ascii', 'ignore')
    last_names_fin.append(real_name)


#print last_names_fin
for att in attributes:
    del att[8]

for att in attributes:
    for elem in att:
        elem = elem.lstrip()
        #print elem
        try:
            elem = str(elem)
        except UnicodeEncodeError:
            continue

for thing in attributes[0]:
    print thing.encode('ascii', 'ignore').strip()



for (n,a) in zip(last_names, attributes):
    salar = Decimal(sub(r'[^\d.]', '', a[4]))
    player = make_player(n, a[0], a[1], a[2], a[3], salar, a[5])
    player_objects.append(player)


player_objects.sort(key=lambda x: x.salary, reverse=False)
for bro in player_objects:
    print bro.playerName
    print bro.injury
    print bro.position
    print bro.team
    print bro.salary
    print bro.fppg



