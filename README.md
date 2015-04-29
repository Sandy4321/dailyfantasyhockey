# dailyfantasyhockey
The scripts in this repo are used for the creation of an optimal daily fantasy hockey lineup. 

Usage   : python do_the_maths.py

Purpose : These scripts have 2 purposes. Firstly, they demonstrate an understanding of web parsing using the python "BeautifulSoup" library. I use BeautifulSoup in order to scrape the internet for NHL players who are active on the day of running the script, and their statistics. The second purpose of this work is to produce an "optimal" daily fantasy hockey lineup. Some creative formulas are used in order to predict success of the active players each day, and players at each position are recommended to the user. 

Common Problems : The players' teams are matched against a master list which is hard coded in a text file. Some times, the author of the website uses acronyms for the teams, which don't match the master list. The acronyms are currently fixed in the master list, but if the website author edits his list again, it will throw an error and the master list will need to be updated.

