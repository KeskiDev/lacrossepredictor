import pandas as pd
import numpy as np
from scipy import stats
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import csv

def GetGameData(team1_stats, team2_stats):
    #combine both team stats into one.

def NormalSituation(stat1, stat2):
	#higher stat wins
    if(stat1 is None or stat2 is None):
        retrun 0
    return float(stat1) - float(stat2)


def AbnormalSituation(stat1, stat2):
	#lower stat wins
    #so not a simple minus will work?


#predict the winner using machine learning
data = open('trainingData.csv')
csv_data = csv.reader(data)

row = 0
team_stats = []
game_stats = []
team_number = 1
correct_guess = 0


for round in csv_data:
    if team_number == 2:
        team_number = 1

    if row != 0:
        team_stats.append(round)

    row += 1

for team in range(0, len(team_stats),2):
    team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, scoring_margin_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, actual_winner_1 = team_stats[team]
	team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, scoring_margin_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, actual_winner_2 = team_stats[team + 1]
    team1 = [team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, scoring_margin_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, actual_winner_1]
    team2 = [team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, scoring_margin_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, actual_winner_2]

    gameInfo = GetGameData(team1, team2)
    game_stats.append(gameInfo)
