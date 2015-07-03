from bs4 import BeautifulSoup # Gets Everything
import urllib2
from decimal import Decimal
from re import sub
from dfh2.player import Player



def make_player(playerName, injury, position, team, opponent, salary, fppg, wpv):
    player = Player(playerName, injury, position, team, opponent, salary, fppg, wpv)
    return player

#List of player html object
tr_list = []

#List of player last names
last_names = []
last_names_fin = []

#Attributes list ( will combine with name list later ) 
attributes = []

#List of opponents
opponents = []

player_objects = []

def get_player_data():
    """Retrieves data about today's active players from the internet."""

    # Website of active player data
    page = urllib2.urlopen("http://www.rotowire.com/daily/nhl/value-report.htm")
    soup = BeautifulSoup(page)
    i=0
    for tr in soup.findAll('tr'):
        tr_list.append(tr)
        try:
            #PUTS THE NAMES IN THE LIST
            last_names.append(tr_list[i].get_text().split(' ')[0])
            last_names[i] = last_names[i][:-1]
            attributes.append(tr_list[i].get_text().split(' ')[-1].split('\n'))
        except IndexError:
            continue
        i = i + 1

    for elem in last_names:
        elem = elem.lstrip()
        elem = str(elem)

    # Remove leading junk data
    del last_names[0:2]
    del attributes[0:2]

    # Fill list of player last names
    for name in last_names:
        real_name = name.split('\n')[-1]
        real_name = real_name.encode('ascii', 'ignore')
        last_names_fin.append(real_name)

    # Remove unnecessary data
    for att in attributes:
        del att[8]

    for att in attributes:
        for elem in att:
            elem = elem.lstrip()
            try:
                elem = str(elem)
            except UnicodeEncodeError:
                continue

    for (n,a) in zip(last_names, attributes):
        salar = Decimal(sub(r'[^\d.]', '', a[4]))
        if a[3][0] == '@':
            a[3] = a[3][1:]
        player = make_player(n, a[0], a[1], a[2], a[3], salar, a[5], 0)
        player_objects.append(player)

    player_objects.sort(key=lambda x: x.salary, reverse=False)
    for bro in player_objects:
        if bro.opponent in opponents:
            #opponents.append(bro.team)
            continue
        else:
            opponents.append(bro.opponent)

    return player_objects


#print opponents



