from bs4 import BeautifulSoup # Gets Everything
import urllib2

#List of player html object
tr_list = []

#List of player last names
last_names = []

page = urllib2.urlopen("http://www.rotowire.com/daily/nhl/value-report.htm")
soup = BeautifulSoup(page)
i=0
for tr in soup.findAll('tr'):
    tr_list.append(tr)
    try:
        #print str(tr_list[i].contents[1].span.get_text())
        last_names.append(tr_list[i].get_text().split(' ')[0])
        last_names[i] = last_names[i][:-1]
        print last_names[i]
    except IndexError:
        continue

    i = i + 1
    print i
#print soup.prettify()
#for thing in soup('td', width="90%"):
#    where, linebreak, what = incident.contents[:3]
#    print where.strip()
#    print what.strip()
#    print
