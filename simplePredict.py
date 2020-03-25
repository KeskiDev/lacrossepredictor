import csv
import pandas

#compareGoalsFor(team_one_stat, team_two_stat)

#compareGoalsAgainst(team_one_stat, team_two_stat)

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
data_set = pandas.read_csv('opponents.csv')

print data_set

#pull out the needed data_set
#send it to the respective methods/variables
#print out the predicted winner