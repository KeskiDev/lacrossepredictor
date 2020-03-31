import csv
import pandas
from random import *

def compareNormalSituation(team_one_stat, team_two_stat):
	if(not team_one_stat  or not team_two_stat):
		return (0,0)
	elif(float(team_one_stat) > float(team_two_stat)):
		#team_one wins this one
		return (1, 0)
	elif(float(team_two_stat) > float(team_one_stat)):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

def compareAbnormalSituation(team_one_stat, team_two_stat):
	if(team_one_stat == " " or team_two_stat == " "):
		return (0,0)
	elif(float(team_one_stat) < float(team_two_stat)):
		#team_one wins this one
		return (1, 0)
	elif(float(team_two_stat) < float(team_one_stat)):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

def RandomWinner(team1, team2):
	x = randint(1,2)
	if x == 1:
		print "It's a pretty even match, but I'm guessing %s will win" % (team1)
		return 1
	else:
		print "It's a pretty even match, but I'm guessing %s will win" % (team2)
		return 2

def DecideWinner(team1_score, team2_score, team1_name, team2_name):
	chosenWinner = 0
	if(team1_score > team2_score):
		print "%s should win the game" % (team1_name)
		chosenWinner = 1
	elif(team_one_count < team_two_count):
		print "%s should win the game" % (team2_name)
		chosenWinner = 2
	else:
		chosenWinner = RandomWinner(team1_name, team2_name)

	return chosenWinner

#read the csv
file = open('2018.csv')
csv_f = csv.reader(file)
round = 0
team_number = 1
game = 1
team_stats = []
correct_guesses = 0

#print csv_f
for row in csv_f:
#	print row
	if team_number == 2:
		team_number = 1
		game += 1

	if(round != 0):
		team_stats.append(row)

	round += 1
	team_number += 1

for team in range(0, len(team_stats), 2):
	team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, scoring_margin_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, actual_winner_1  = team_stats[team]
	team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, scoring_margin_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, actual_winner_2  = team_stats[team + 1]

	#goals for
	goalsFor1, goalsFor2 = compareNormalSituation(goals_for_1, goals_for_2)

	#goals against
	goalsAgainst1, goalsAgainst2 = compareAbnormalSituation(goals_against_1,goals_against_2)

	#faceoff
	face_off1, face_off2 = compareNormalSituation(faceoff_1, faceoff_2)

	#manup
	manup1, manup2 = compareNormalSituation(man_up_1, man_up_2)

	#mandown
	mandown1, mandown2 = compareNormalSituation(man_down_1, man_down_2)

	#scoringMaring ?

	#saves
	save_team1, save_team2 = compareNormalSituation(saves_1,saves_2)

	#groundBalls
	ground1, ground2 = compareNormalSituation(ground_balls_1, ground_balls_2)

	#turnovers
	turn1, turn2 = compareAbnormalSituation(turnovers_1, turnovers_2)

	#caused turnovers
	caused1, caused2 = compareNormalSituation(caused_turnovers_1, caused_turnovers_2)

	#shot percent
	shot1, shot2 = compareNormalSituation(shot_percent_1, shot_percent_2)

	#clearing
	ground1, ground2 = compareNormalSituation(clearing_percent_1, clearing_percent_2)


	team_one_count = goalsFor1 + goalsAgainst1 + face_off1 + manup1 + save_team1 + ground1 + turn1 + caused1 + shot1 + ground1
	team_two_count = goalsFor2 + goalsAgainst2 + face_off2 + manup1 + save_team2 + ground2 + turn2 + caused2 + shot2 + ground2

	winner = DecideWinner(team_one_count, team_two_count, team_name_1, team_name_2)

	if winner == int(actual_winner_1):
		correct_guesses += 1

game_count = float(len(team_stats)/2)
correctPercent = (correct_guesses/game_count) * 100
percent = "%"

print "%s%s correct guesses." % (correctPercent, percent)
