import csv
import pandas
from random import *

def compareNormalSituation(team_one_stat, team_two_stat):
	if(team_one_stat > team_two_stat):
		#team_one wins this one
		return (1, 0)
	elif(team_two_stat > team_one_stat):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

def compareAbnormalSituation(team_one_stat, team_two_stat):
	if(team_one_stat < team_two_stat):
		#team_one wins this one
		return (1, 0)
	elif(team_two_stat < team_one_stat):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

def RandomWinner(team1, team2):
	x = randint(1,2)
	if x == 1:
		print "It's a pretty even match, but I'm guessing %s will win" % (team1)
	else:
		print "It's a pretty even match, but I'm guessing %s will win" % (team2)


#read the csv
file = open('opponents4.csv')
csv_f = csv.reader(file)
round = 0
team_number = 1
game = 1

#print csv_f
for row in csv_f:
#	print row
	if team_number == 2:
		team_number = 1
		game += 1

	if(round != 1):
		team_name_ + str(team_number) + "_" + str(game),
		goals_for_ + str(team_number) + "_" + str(game),
		goals_against_ + str(team_number) + "_" + str(game),
		faceoff, man_up_ + str(team_number) + "_" + str(game),
		man_down_ + str(team_number) + "_" + str(game),
		scoring_margin_ + str(team_number) + "_" + str(game),
		saves_ + str(team_number) + "_" + str(game),
		ground_balls_ + str(team_number) + "_" + str(game),
		turnovers_ + str(team_number) + "_" + str(game),
		caused_turnovers_ + str(team_number) + "_" + str(game),
		shot_percent_ + str(team_number) + "_" + str(game),
		clearing_percent_ + str(team_number) + "_" + str(game)  = row

	round += 1
	team_number += 1

#goals for
goalsFor1, goalsFor2 = compareNormalSituation(float(goals_for1), float(goals_for2))

#goals against
goalsAgainst1, goalsAgainst2 = compareAbnormalSituation(float(goals_against1), float(goals_against2))

#faceoff
face_off1, face_off2 = compareNormalSituation(float(faceoff1), float(faceoff2))

#manup
manup1, manup2 = compareNormalSituation(float(man_up1), float(man_up2))

#mandown
mandown1, mandown2 = compareNormalSituation(float(man_down1), float(man_down2))

#scoringMaring ?

#saves
save_team1, save_team2 = compareNormalSituation(float(saves1),float(saves2))

#groundBalls
ground1, ground2 = compareNormalSituation(float(ground_balls1), float(ground_balls2))

#turnovers
turn1, turn2 = compareAbnormalSituation(float(turnovers1), float(turnovers2))

#caused turnovers
caused1, caused2 = compareNormalSituation(float(caused_turnovers1), float(caused_turnovers2))

#shot percent
shot1, shot2 = compareNormalSituation(float(shot_percent1), float(shot_percent2))

#clearing
ground1, ground2 = compareNormalSituation(float(clearing_percent1), float(clearing_percent2))


team_one_count = goalsFor1 + goalsAgainst1 + face_off1 + manup1 + save_team1 + ground1 + turn1 + caused1 + shot1 + ground1
team_two_count = goalsFor2 + goalsAgainst2 + face_off2 + manup1 + save_team2 + ground2 + turn2 + caused2 + shot2 + ground2

if(team_one_count > team_two_count):
	print "%s should win the game" % (team1_name)
elif(team_one_count < team_two_count):
	print "%s should win the game" % (team2_name)
else:
	RandomWinner(team1_name, team2_name)
