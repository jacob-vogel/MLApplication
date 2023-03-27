import pandas as pd
import numpy as np
import scipy as sp

def getTournamentGameByGame():

    df = pd.read_csv('March Madness Data/Tournament Data/TournamentGameByGameData.csv')
    #TournamentGameByGame = pd.read_csv('March Madness Data/Tournament Data/TournamentGameByGameData.csv')
    #TournamentGameByGame = pd.read_csv('/Users/jacobvogel/Desktop/Western/New_School/Machine Learning/MLApplication/March Madness Data/Tournament Data/TournamentGameByGameData.csv')

    #DF.describe()
    #TournamentGameByGame.describe()

    df = df.drop(['Unnamed: 0', 'Score1', 'Score2', 'G1', 'MP1', 'FG1', 'FGA1', 'FG%1', 'FT1', 'FTA1', 'FT%1', 'TRB1', 'AST1', 'STL1', 'BLK1', 'TOV1', 
    'PF1', 'PTS1', 'G2', 'MP2', 'FG2', 'FGA2', 'FG%2', 'FT2', 'FTA2', 'FT%2', 'TRB2', 'AST2', 'STL2', 'BLK2', 'TOV2', 'PF2', 'PTS2', '2P1', '2PA1',
    '2P%1', '3P1', '3PA1', '3P%1', '2P2', '2PA2', '2P%2', '3P2', '3PA2', '3P%2', 'ORB1', 'DRB1', 'ORB2', 'DRB2'], axis=1)

    df2 = df.loc[df["Year"] >= 2013]

    df2 = df2.iloc[::2]
    
    id = list(range(0,441))
    df2['id'] = id
    
    df2['Team1'] = df2['Team1'].str.lower()
    df2['Team2'] = df2['Team2'].str.lower()

    

    return df2
