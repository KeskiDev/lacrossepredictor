import csv
import pandas as pd
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

def WeeklyRank(team1, team2):
    team_1_rank = 0
    team_2_rank = 0

    if(float(team1) != 0):
        team_1_rank = float(team1)

    if(float(team2) != 0):
        team_2_rank = float(team2)

    if(team_1_rank == team_2_rank):
        return(0,0)
    elif(team_1_rank < team_2_rank):
        return(.5,0)
    elif(team_2_rank < team_1_rank):
        return(0,.5)



def PrintWinner(team1Points, team1Name, team2Points, team2Name, team1_home, team2_home):
    #which team has the most points
    if(team1Points > team2Points):
        print("{}({}) should win the game against {}({}).\n".format(team1Name,team1Points, team2Name, team2Points))
    elif(team1Points < team2Points):
        print("{}({}) should win the game against {}({}).\n".format(team2Name, team2Points, team1Name, team1Points))
    else:
        print("close game but {} has home field, I call the game for them.\n".format(team1Name))

def Run():
    #read the file for the game(s)
    statsFile = open("stats.csv")
    file = open("gameday.csv")
    stats_csv = csv.reader(statsFile)
    csv_f = csv.reader(file)
    games = []
    stats = []
    line = 0
    game = 1
    stats_line = 0
    home_field_advantage = 1

    for row in stats_csv:
        if(stats_line > 0):
            stats.append(row)
        stats_line += 1
    
    stats_df = pd.DataFrame(stats, columns=['name', 'goals for', 'goals against', 'faceoff %', 'man up', 'man down', 'saves','ground balls','turnovers','caused turnovers','shot %','clearing %','rank'])
    

    #then read from the stats file
    for row in csv_f:
        games.append(row)
        line += 1

    gamenumber = 1
    for game in games:
        if(gamenumber == 13):
            wairt = "wait"
        home_team_name, away_team_name = game
        
        #get home team stats
        home_team = stats_df.loc[stats_df['name'] == home_team_name].to_numpy()
        #get away team stats
        away_team = stats_df.loc[stats_df['name'] == away_team_name].to_numpy()

        if home_team.size > 0 and away_team.size > 0:
            #tally the points
            goalsFor1, goalsFor2 = GoalsFor(home_team[0][1], away_team[0][1])
            goalsAgainst1, goalsAgainst2 = GoalsAgainst(home_team[0][2], away_team[0][2])
            faceoff1, faceoff2 = FaceOff(home_team[0][3], away_team[0][3])
            manup1, manup2 = ManUp(home_team[0][4], away_team[0][4])
            mandown1, mandown2 = ManDown(home_team[0][5], away_team[0][5])
            saves1, saves2 = Saves(home_team[0][6], away_team[0][6])
            ground1, ground2 = Groundballs(home_team[0][7], away_team[0][7])
            turnover1, turnover2 = Turnovers(home_team[0][8], away_team[0][8])
            caused1, caused2 = CausedTurnovers(home_team[0][9], away_team[0][9])
            shot1, shot2 = ShotPercent(home_team[0][10], away_team[0][10])
            clearing1, clearing2 = Clearing(home_team[0][11], away_team[0][11])
            rank1,rank2 = WeeklyRank(home_team[0][12], away_team[0][12])

            team1Points = goalsFor1 + goalsAgainst1 + faceoff1 + manup1 + mandown1 + saves1 + ground1 + turnover1 + caused1 + shot1 + clearing1 + home_field_advantage + rank1
            team2Points = goalsFor2 + goalsAgainst2 + faceoff2 + manup2 + mandown2 + saves2 + ground2 + turnover2 + caused2 + shot2 + clearing2 + rank2

            #print winner
            PrintWinner(team1Points, home_team_name, team2Points, away_team_name, 1,0)
        else:
            print("No data found for one of the teams. Home team win {} vs. {}.\n".format(home_team_name,away_team_name))



Run()
