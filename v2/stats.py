import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser
import pandas as pd
import os
import csv


def url_get_contents(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        f = urllib.request.urlopen(req)

        return f.read()
    except urllib.error.HTTPError:
        contents = urllib.error.HTTPError
        print(contents)


def get_stats(team_name, school,year,weeklyRank):
    url = "https://www.insidelacrosse.com/team/stats/{}/{}".format(team_name, year)
    
    xhtml = url_get_contents(url).decode('utf-8')
    p = HTMLTableParser()

    p.feed(xhtml)
    df = pd.DataFrame(p.tables[0], columns=['Number', 'Name', 'Position', 'GamesPlayed', 'goals', 'assists', 'points', 'shots', 'shot %', 'sog', 'sog%', 'gb', 'ct', 'to','saves', 'goals allowed', 'shots faced', 'save%', 'faceoff won', 'faceoff attempt', 'fo%'])
    #df.to_csv(os.path.join(location, filename))
    df = df.iloc[1:]
    df['GamesPlayed'] = df['GamesPlayed'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['goals'] = df['goals'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['assists'] = df['assists'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['points'] = df['points'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['shots'] = df['shots'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['sog'] = df['sog'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['gb'] = df['gb'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['ct'] = df['ct'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['to'] = df['to'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['saves'] = df['saves'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['goals allowed'] = df['goals allowed'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['shots faced'] = df['shots faced'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['faceoff won'] = df['faceoff won'].apply(pd.to_numeric, downcast='float', errors='coerce')
    df['faceoff attempt'] = df['faceoff attempt'].apply(pd.to_numeric, downcast='float', errors='coerce')


    #get the team ranking?
    #how long a team has been in D1?
    
    gamesPlayed = df['GamesPlayed'].max()
    
    if(gamesPlayed > 0):
        goals = df['goals'].sum()
        shots = df['shots'].sum()
        goalsAllowed = df['goals allowed'].sum()
        if(shots > 0):
            shotPercent = round((goals/shots),2)
        else:
            shotPercent = 0
        
        #turnovers per game
        turnovers = df['to'].sum()
        toPerGame = round(turnovers/gamesPlayed,2)
        #saves per game
        saves = df['saves'].sum()
        savesPerGame = round(saves/gamesPlayed,2)
        #gb per game
        totalGroundBalls = df['gb'].sum()
        gbPerGame = round((totalGroundBalls/gamesPlayed),2)
        
        causedTO = df['ct'].sum()
        faceoffsWon = df['faceoff won'].sum()
        faceoffAttempted = df['faceoff attempt'].sum()
        #double scalar error
        if(faceoffAttempted > 0):
            faceOffPercent = round((faceoffsWon/faceoffAttempted),2)
        else:
            faceOffPercent = 0

        manup = 0
        mandown = 0
        clearing = 0

        #team name, goals for, goals against, faceoff %, man up, man down, saves per game, gb per game, to per game, caused to, shot %, clearing %
        #team_data = "{},{},{},{},{},{},{},{},{},{},{},{}".format(school, goals, goalsAllowed, faceOffPercent, manup, mandown, savesPerGame, gbPerGame,toPerGame,causedTO, shotPercent,clearing)
        team_data = [school, goals, goalsAllowed, faceOffPercent, manup, mandown, savesPerGame, gbPerGame,toPerGame,causedTO, shotPercent,clearing,weeklyRank]
        
        return team_data
    else:
        #team has played no games this year
        team_data = [school,0,0,0,0,0,0,0,0,0,0,0,weeklyRank]
        return team_data
    #newDF = pd.DataFrame(team_data)

    # filepath = os.path.dirname(os.path.abspath(__file__))
    # location = os.path.join("teamstats")
    # filename = "{}.csv".format(school)
    # newDF.to_csv(filename)

    
    # filepath = os.path.dirname(os.path.abspath(__file__))
    # location = os.path.join("teamstats")
    # filename = "{}.csv".format(school)

    
def GetRanking(year):
    url = "https://www.insidelacrosse.com/league/di/polls/{}".format(year)
    
    xhtml = url_get_contents(url).decode('utf-8')
    p = HTMLTableParser()

    p.feed(xhtml)
    #each for is for 1 row
    #can't do in for loop function recursion most likely
    count = 0
    how_many_things = len(p.tables[1][0])

    team_rankings = []


    while count < how_many_things:
        rank,teamName, new_count = GetTeamRankings(p.tables[1][0], count)
        team_rank_info = {"team": teamName, "rank": rank}
        team_rankings.append(team_rank_info)
        if(rank == '20'):
            break
        count = new_count
        
    
    return team_rankings

def GetTeamRankings(data, position):
    rank = 0
    teamName = ""
    next_position = 0

    if(data[position] == ''):
        position += 1

    if(position +1 < len(data)):
        rank = data[position]

        name_and_record = data[position +1]
        #trim the record off of the team name
        team_split = name_and_record.split('(')
        teamName = team_split[0].strip()

        #??????
        next_position = (position + 4) if (position + 4) < len(data) else len(data) 
        if((position + 4) <= len(data)):
            if(data[position + 4] == ' '):
                next_position = position + 6 if (position + 6) < len(data) else len(data)

    return rank,teamName, next_position



def Run():
    #read the file for the game(s)
    file = open("teams.csv")
    csv_f = csv.reader(file)
    teams = []
    team_number = 1
    line = 0
    year = '2021'
    stats = []

    #get the current weekly rankings
    ranking = GetRanking(year)

    for row in csv_f:
        if(line != 0):
            teams.append(row)

        line += 1
        team_number += 1

    for team in range(0,len(teams)):
        school, team_name = teams[team]
        
        weeklyRank = 0
        for schoolRank in ranking:
            if(schoolRank["team"] == school):
                weeklyRank = schoolRank["rank"]

        teamstats = get_stats(team_name, school, year, weeklyRank)
        stats.append(teamstats)

    #team name, goals for, goals against, faceoff %, man up, man down, saves per game, gb per game, to per game, caused to, shot %, clearing %
    fields = ['name','goals','goals against','faceoff%','man up','man down','aves per game','gb per game','to per game','caused to','shot %','clearing %','rank']
    with open('stats.csv', 'w') as statsFile:
        csvWriter = csv.writer(statsFile)
        csvWriter.writerow(fields)
        csvWriter.writerows(stats)

Run()