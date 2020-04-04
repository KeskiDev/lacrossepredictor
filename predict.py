import pandas as pd
import csv

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

    winningTeamName = ""
    if(team1_stats[13] == "1"):
        winningTeamName = team1_stats[0]
    else:
        winningTeamName = team2_stats[0]

    gameInfo.append(winningTeamName)

    return gameInfo

def NormalSituation(stat1, stat2):
	#higher stat wins
    if(stat1 is None or stat1 == "" or stat2 is None or stat2 == ""):
        return 0

    stat = float(stat1) - float(stat2)
    result = round(stat,2)

    return result

def AbnormalSituation(stat1, stat2):
    statScore = 0
    if(stat1 is None or stat1 == "" or stat2 is None or stat2 == ""):
        return statScore
    else:
        if float(stat1) > float(stat2):
            statScore = float(stat2) - float(stat1)
        else:
            statScore = float(stat1) - float(stat2)

    return round(statScore,2)


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
    #print len(team_stats[team])
    team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, scoring_margin_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, team1_score, actual_winner_1 = team_stats[team]
    team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, scoring_margin_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, team2_score, actual_winner_2 = team_stats[team + 1]
    team1 = [team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, scoring_margin_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_percent_1, clearing_percent_1, actual_winner_1]
    team2 = [team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, scoring_margin_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_percent_2, clearing_percent_2, actual_winner_2]

    gameInfo = GetGameData(team1, team2)
    print gameInfo
    #game_stats.append(gameInfo)


print game_stats[1]
