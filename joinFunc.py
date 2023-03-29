import pandas as pd
import numpy as np
import scipy as sp

def joinCols(columnList, TG, otherData, teamColName, yearColName):
    
    for statColName in columnList:
        statTeam1 = [];
        statTeam2 = [];
        for i in range(0,len(TG)):
            teamRowJacob = TG[TG['id'] == i]
            team1Name = teamRowJacob.Team1
            #print(team1Name[i])
            team2Name = teamRowJacob.Team2
            year = teamRowJacob.Year
            #print(year[i])
            team1RowJack = otherData[((otherData[teamColName] == team1Name[i]) & (otherData[yearColName] == year[i]))]
            team2RowJack = otherData[((otherData[teamColName] == team2Name[i]) & (otherData[yearColName] == year[i]))]
            #print()

            statTeam1Val = team1RowJack[statColName]
            statTeam2Val = team2RowJack[statColName]
            if(statTeam1Val.empty):
                statTeam1.append(None)
            else:
                #print(kenPomAdjEffTeam1Val[team1RowJack.index[0]])
                #print('--------------------')
                statTeam1.append(statTeam1Val[team1RowJack.index[0]])

            if(statTeam2Val.empty):
                statTeam2.append(None)
            else:
                #print(team2Name[i])
                #print(kenPomAdjEffTeam2Val[team2RowJack.index[0]])
                #print('--------------------')
                statTeam2.append(statTeam2Val[team2RowJack.index[0]])

        TG[f'{statColName} Team1'] = statTeam1
        TG[f'{statColName} Team2'] = statTeam2
    
    return TG