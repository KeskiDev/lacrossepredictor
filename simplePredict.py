import csv
import pandas

def compareGoalsFor(team_one_stat, team_two_stat):
	if(team_one_stat > team_two_stat):
		#team_one wins this one
		return (1, 0)
	elif(team_two_stat > team_one_stat):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

def compareGoalsAgainst(team_one_stat, team_two_stat):
	if(team_one_stat < team_two_stat):
		#team_one wins this one
		return (1, 0)
	elif(team_two_stat < team_one_stat):
		#team_two wins this one
		return (0,1)
	else:
		#both get zero point
		return (0,0)

#compareFaceOff(team_one_stat, team_two_stat)

#compareManUp(team_one_stat, team_two_stat)

#compareManDownKill(team_one_stat, team_two_stat)

#compareSaves(team_one_stat, team_two_stat)

#compareGroundBalls(team_one_stat, team_two_stat)

#compareTurnovers(team_one_stat, team_two_stat)

#compareCausedTurnovers(team_one_stat, team_two_stat)

#compareShotPrecent(team_one_stat, team_two_stat)

#compareClear(team_one_stat, team_two_stat)



#read the csv
file = open('opponents.csv')
csv_f = csv.reader(file)
round = 0

team_one_count = 0
team_two_count = 0

#print csv_f
for row in csv_f:
#	print row
	if(round == 1):
		team1_name, goals_for1, goals_against1, faceoff1, man_up1, man_down1, scoring_margin1, saves1, ground_balls1, turnovers1, caused_turnovers1, shot_percent1, clearing_percent1  = row
	elif(round == 2):
		team2_name, goals_for2, goals_against2, faceoff2, man_up2, man_down2, scoring_margin2, saves2, ground_balls2, turnovers2, caused_turnovers2, shot_percent2, clearing_percent2 = row
	round += 1


print "%s vs. %s" % (team1_name, team2_name)

print "goals for team 1 = %s : team 2 = %s" % (goals_for1, goals_for2)

goalsFor1, goalsFor2 = compareGoalsFor(goals_for1, goals_for2)
team_one_count += goalsFor1
team_two_count += goalsFor2
print "team 1 %s vs. team 2 %s" % (team_one_count, team_two_count)
goalsAgainst1, goalsAgainst2 = compareGoalsAgainst(goals_against1, goals_against2)
team_one_count += goalsAgainst1
team_two_count += goalsAgainst2
print "team 1 %s vs. team 2 %s" % (team_one_count, team_two_count)





#data_set = pandas.read_csv('opponents.csv')




#pull out the needed data_set
#send it to the respective methods/variables
#print out the predicted winner
