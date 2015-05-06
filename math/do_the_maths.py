from get_team_data import get_team_data
from get_player_data import get_player_data

def main():
	#Gets the average goals against list for opponents
	team_GAPG = get_team_data()

	#Gets the stat data for today's players
	player_objects = get_player_data()

	#print team_GAPG

	

	#for player in player_objects:
	#	print player.playerName

	
	before_list = []
	for player in player_objects:
		before_list.append(player)


	not_injured = []


	#Remove injured players
	num = 0
	for player in player_objects:
		if str(player.injury) in ['DTD', 'IR', 'Out'] or player.salary < 4000:
			player_objects.remove(player)
			#print "GOT HERE"
			#print player.injury
		else:
			not_injured.append(player)
		num = num + 1


	#for player in before_list:
	#	if player not in player_objects:
	#		print player.playerName




	#Current player's opponent's AGAPG
	opp_gapg = 0.0

	#Current player projection

	#Loop through today's players and give the highest projected totals
	for player in not_injured:
		opp_gapg = team_GAPG[player.opponent]
		player.wpv = (float(opp_gapg) * float(player.fppg)) / float(player.salary)

	#=========================================================
	# How to sort list of objects 
	# sorted(student_objects, key=lambda student: student.age)
	#=========================================================

	sorted_list = sorted(not_injured, key=lambda player: player.wpv, reverse=True)

	#Print the sorted list of players
	"""for player in sorted_list:
		print player.playerName
		print player.wpv * 1000
		print player.injury
	"""

	num = 0
	#for player in player_objects

	#break down by position
	left_wings = []
	centers = []
	right_wings = []
	defense = []
	goalies = []

	for player in sorted_list:
		if player.position == 'LW':
			left_wings.append(player)
		elif player.position == 'C':
			centers.append(player)
		elif player.position =='RW':
			right_wings.append(player)
		elif player.position == 'D':
			defense.append(player)
		else:
			goalies.append(player)

	count = 0
	print "LEFT WINGS===================="
	for player in left_wings:
		if count < 10:
			print player.playerName
			print player.wpv * 1000
		count = count + 1

	count = 0
	print "\nRIGHT WINGS===================="
	for player in right_wings:
		if count < 10:
			print player.playerName
			print player.wpv * 1000
		count = count + 1

	count = 0
	print "\nCENTERS===================="
	for player in centers:
		if count < 10:
			print player.playerName
			print player.wpv * 1000
		count = count + 1

	count = 0
	print "\nDEFENSE===================="
	for player in defense:
		if count < 10:
			print player.playerName
			print player.wpv * 1000
		count = count + 1



if __name__ == '__main__':
	main()




































