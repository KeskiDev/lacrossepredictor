import csv
import pandas
from random import *
import os

#Giving the rules
def GoalsFor(team1, team2):
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(2,0)
    elif(float() < float()):
        return(0,2)
    else:
        return(0,0)

def GoalsAgainst(team1, team2):
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) < float(team2)):
        return(1.5,0)
    elif(float(team1) > float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def FaceOff(team1, team2):
    #weight of 1.5
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def ManUp(team1, team2):
    #weight of 1
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1,0)
    elif(float(team1) < float(team2)):
        return(0,1)
    else:
        return(0,0)

def ManDown(team1, team2):
    #weight of 1.5
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def Saves(team1, team2):
    #weight of 1.5
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def Groundballs(team1, team2):
    #weight of 1.5
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def Turnovers(team1, team2):
    #weight of 1
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) < float(team2)):
        return(1,0)
    elif(float(team1) > float(team2)):
        return(0,1)
    else:
        return(0,0)

def CausedTurnovers(team1, team2):
    #weight of 1
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1,0)
    elif(float(team1) < float(team2)):
        return(0,1)
    else:
        return(0,0)

def ShotPercent(team1, team2):
    #weight of 1
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def Clearing(team1, team2):
    #weight of 1.5
    if(not team1 or not team2):
        return (0,0)
    elif(float(team1) > float(team2)):
        return(1.5,0)
    elif(float(team1) < float(team2)):
        return(0,1.5)
    else:
        return(0,0)

def PrintWinner(team1Points, team1Name, team2Points, team2Name, team1_home, team2_home):
    #which team has the most points
    if(team1Points > team2Points):
        print("{} should win the game.".format(team1Name))
        score = "{} ({}) vs {} ({})".format(team1Name, team1Points,team2Name, team2Points)
        print(score)
    elif(team1Points < team2Points):
        print("{} should win the game.".format(team2Name))
        score = "{} ({}) vs {} ({})".format(team1Name, team1Points,team2Name, team2Points)
        print(score)
    else:
        if(team1_home == 1):
            print("close game but {} has home field, I call the game for them.".format(team1Name))
        else:
            print("close game but {} has home field, I call the game for them.".format(team2Name))


def Run():
    #read the file for the game(s)
    file = open("gameday2.csv")
    csv_f = csv.reader(file)
    team_stats = []
    team_number = 1
    line = 0
    game = 1

    for row in csv_f:
        if team_number == 2:
            team_number = 1
            game += 1

        if(line != 0):
            team_stats.append(row)

        line += 1
        team_number += 1
    
    #call the methods
    for team in range(0, len(team_stats), 2):
        team_name_1, goals_for_1, goals_against_1, faceoff_1, man_up_1, man_down_1, saves_1, ground_balls_1, turnovers_1, caused_turnovers_1, shot_1, clearing_percent_1, home_1 = team_stats[team]
        team_name_2, goals_for_2, goals_against_2, faceoff_2, man_up_2, man_down_2, saves_2, ground_balls_2, turnovers_2, caused_turnovers_2, shot_2, clearing_percent_2, home_2 = team_stats[team+1]

        goalsFor1, goalsFor2 = GoalsFor(goals_for_1, goals_for_2)
        goalsAgainst1, goalsAgainst2 = GoalsAgainst(goals_against_1, goals_against_2)
        faceoff1, faceoff2 = FaceOff(faceoff_1, faceoff_2)
        manup1, manup2 = ManUp(man_up_1, man_up_2)
        mandown1, mandown2 = ManDown(man_down_1, man_down_2)
        saves1, saves2 = Saves(saves_1, saves_2)
        ground1, ground2 = Groundballs(ground_balls_1, ground_balls_2)
        turnover1, turnover2 = Turnovers(turnovers_1, turnovers_2)
        caused1, caused2 = CausedTurnovers(caused_turnovers_1, caused_turnovers_2)
        shot1, shot2 = ShotPercent(shot_1, shot_2)
        clearing1, clearing2 = Clearing(clearing_percent_1, clearing_percent_2)

        team1Points = goalsFor1 + goalsAgainst1 + faceoff1 + manup1 + mandown1 + saves1 + ground1 + turnover1 + caused1 + shot1 + clearing1 + home_1
        team2Points = goalsFor2 + goalsAgainst2 + faceoff2 + manup2 + mandown2 + saves2 + ground2 + turnover2 + caused2 + shot2 + clearing2 + home_2

        #print winner
        PrintWinner(team1Points, team_name_1, team2Points, team_name_2, home_1, home_2)


Run()

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
