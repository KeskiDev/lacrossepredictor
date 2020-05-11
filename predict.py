import pandas as pd
import numpy as np
import math
import csv
from sklearn.externals import joblib
from sklearn.svm import SVC

def PredictingGameData(team1_stats, team2_stats):
    #combine both team stats into one.
    gameInfo = []

    #goals for
    goalsFor = NormalSituation(team1_stats[0], team2_stats[0])
    gameInfo.append(goalsFor)
    #goals against
    goalsAgainst = AbnormalSituation(team1_stats[1], team2_stats[1])
    gameInfo.append(goalsAgainst)
    #faceoff
    face_off = NormalSituation(team1_stats[2], team2_stats[2])
    gameInfo.append(face_off)
    #manup
    manup = NormalSituation(team1_stats[3], team2_stats[3])
    gameInfo.append(manup)
    #mandown
    mandown = NormalSituation(team1_stats[4], team2_stats[4])
    gameInfo.append(mandown)
    #saves
    saves = NormalSituation(team1_stats[5], team2_stats[5])
    gameInfo.append(saves)
    #groundBalls
    groundBalls = NormalSituation(team1_stats[6], team2_stats[6])
    gameInfo.append(groundBalls)
    #turnovers
    turnOvers = AbnormalSituation(team1_stats[7], team2_stats[7])
    gameInfo.append(turnOvers)
    #caused turnovers
    causedTurnovers = NormalSituation(team1_stats[8], team2_stats[8])
    gameInfo.append(causedTurnovers)
    #shot percent
    shotPercent = NormalSituation(team1_stats[9], team2_stats[9])
    gameInfo.append(shotPercent)
    #clearing
    clearingPercent = NormalSituation(team1_stats[10], team2_stats[10])
    gameInfo.append(clearingPercent)
    
    return gameInfo

def GetGameData(team1_stats, team2_stats):
    #combine both team stats into one.
    gameInfo = []

    #goals for
    goalsFor = NormalSituation(team1_stats[1], team2_stats[1])
    gameInfo.append(goalsFor)
    #goals against
    goalsAgainst = AbnormalSituation(team1_stats[2], team2_stats[2])
    gameInfo.append(goalsAgainst)
    #faceoff
    face_off = NormalSituation(team1_stats[3], team2_stats[3])
    gameInfo.append(face_off)
    #manup
    manup = NormalSituation(team1_stats[4], team2_stats[4])
    gameInfo.append(manup)
    #mandown
    mandown = NormalSituation(team1_stats[5], team2_stats[5])
    gameInfo.append(mandown)
    #saves
    saves = NormalSituation(team1_stats[6], team2_stats[6])
    gameInfo.append(saves)
    #groundBalls
    groundBalls = NormalSituation(team1_stats[7], team2_stats[7])
    gameInfo.append(groundBalls)
    #turnovers
    turnOvers = AbnormalSituation(team1_stats[8], team2_stats[8])
    gameInfo.append(turnOvers)
    #caused turnovers
    causedTurnovers = NormalSituation(team1_stats[9], team2_stats[9])
    gameInfo.append(causedTurnovers)
    #shot percent
    shotPercent = NormalSituation(team1_stats[10], team2_stats[10])
    gameInfo.append(shotPercent)
    #clearing
    clearingPercent = NormalSituation(team1_stats[11], team2_stats[11])
    gameInfo.append(clearingPercent)
    #score
    finalScore = NormalSituation(team1_stats[12], team2_stats[12])
    gameInfo.append(finalScore)

    gameInfo.append(team1_stats[13])

    return gameInfo

def NormalSituation(stat1, stat2):
	#higher stat wins
    if(stat1 is None or stat1 == "" or stat2 is None or stat2 == ""):
        return 0

    stat = float(stat1) - float(stat2)
    return stat

def AbnormalSituation(stat1, stat2):
    statScore = 0
    if(stat1 is None or stat1 == "" or stat2 is None or stat2 == ""):
        return statScore
    else:
        if float(stat1) > float(stat2):
            statScore = float(stat2) - float(stat1)
        else:
            statScore = float(stat1) - float(stat2)
    
    return statScore

def createModels(labels, trainingData):
    X = []
    Y = []
    svc = SVC(kernel = 'linear')
    #r = LogisticRegression()
    #rf = RandomForestClassifier()
    
    Y = labels
    X = trainingData
    X = np.array(X).reshape(-1,1) 

    #lr.fit(X, Y)
    #joblib.dump(lr, 'lrTraining.pkl')

    #rf.fit(X, Y)
    #joblib.dump(rf, 'rfTraining.pkl')
    
    svc.fit(X, Y)
    joblib.dump(svc, 'svcTraining.pkl')

def predictWinner(data, team1_name, team2_name):
    winner = ""
    #open pickle file
    #gi = pd.read_pickle('svcTraining.pkl')
    #gi.head();
    gi = joblib.load('svcTraining.pkl')
    game = np.array(data).reshape(-1,1)

    #prediict winner
    prediction = gi.predict(game)[0]

    if(prediction == 1):
        winner = team1_name
    else:
        winner = team2_name

    return winner


#predict the winner using machine learning
data = open('2019.csv')
csv_data = csv.reader(data)

row = 0
team_stats = []
game_stats = []
team_number = 1
correct_guess = 0

gamePlayed = 1

for round in csv_data:
    if team_number == 2:
        team_number = 1

    if row != 0:
        team_stats.append(round)

    row += 1

for team in range(0, len(team_stats),2):
    #print team_stats[team]
    #print team_stats[team+1]
    #training - add the missing variables
    #team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2 = team_stats[team + 1]
    #team1 = [goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, team1_score]
    #team2 = [goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, team2_score]
    #gameInfo = GetGameData(team1, team2)
    #labels = ["goals for", "goals against",	"faceoff winning %", "man-up off", "man down def", "saves per game", "ground balls per game", "turnovers per game", "caused turnovers", "shot %",	"clearing %", "score", "actual winner"]

    #predicting
    team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1 = team_stats[team]
    team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2 = team_stats[team + 1]
    team1 = [goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1]
    team2 = [goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2]
    
    predictInfo = PredictingGameData(team1, team2)
    
    #createModels(labels, gameInfo)

    print str(gamePlayed) + " - " + predictWinner(predictInfo, team_name_1, team_name_2)
    gamePlayed += 1