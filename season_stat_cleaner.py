#data: https://www.kaggle.com/datasets/andrewsundberg/college-basketball-dataset?select=cbb.csv
import pandas as pd
import numpy as np 
import scipy as sci
import os

tournament_teams_13_19 = {
 'Abilene Christian',
 'Akron',
 'Alabama',
 'Alabama-Birmingham',
 'Albany (NY)',
 'American',
 'Arizona',
 'Arizona State',
 'Arkansas',
 'Auburn',
 'Austin Peay',
 'BYU',
 'Baylor',
 'Belmont',
 'Bradley',
 'Bucknell',
 'Buffalo',
 'Butler',
 'Cal Poly',
 'Cal State Bakersfield',
 'Cal State Fullerton',
 'California',
 'Chattanooga',
 'Cincinnati',
 'Clemson',
 'Coastal Carolina',
 'Colgate',
 'College of Charleston',
 'Colorado',
 'Colorado State',
 'Creighton',
 'Davidson',
 'Dayton',
 'Delaware',
 'Duke',
 'ETSU',
 'Eastern Kentucky',
 'Eastern Washington',
 'Fairleigh Dickinson',
 'Florida',
 'Florida Gulf Coast',
 'Florida State',
 'Fresno State',
 'Gardner-Webb',
 'George Washington',
 'Georgetown',
 'Georgia',
 'Georgia State',
 'Gonzaga',
 'Green Bay',
 'Hampton',
 'Harvard',
 'Hawaii',
 'Holy Cross',
 'Houston',
 'Illinois',
 'Indiana',
 'Iona',
 'Iowa',
 'Iowa State',
 'Jacksonville State',
 'James Madison',
 'Kansas',
 'Kansas State',
 'Kent State',
 'Kentucky',
 'LSU',
 'La Salle',
 'Lafayette',
 'Liberty',
 'Lipscomb',
 'Little Rock',
 'Louisiana',
 'Louisville',
 'Loyola (IL)',
 'Manhattan',
 'Marquette',
 'Marshall',
 'Maryland',
 'Memphis',
 'Mercer',
 'Miami (FL)',
 'Michigan',
 'Michigan State',
 'Middle Tennessee',
 'Milwaukee',
 'Minnesota',
 'Mississippi State',
 'Missouri',
 'Montana',
 "Mount St. Mary's",
 'Murray State',
 'NC State',
 'Nebraska',
 'Nevada',
 'New Mexico',
 'New Mexico State',
 'North Carolina A&T',
 'North Carolina Central',
 'North Dakota',
 'North Dakota State',
 'Northeastern',
 'Northern Iowa',
 'Northern Kentucky',
 'Northwestern',
 'Northwestern State',
 'Notre Dame',
 'Ohio State',
 'Oklahoma',
 'Oklahoma State',
 'Old Dominion',
 'Ole Miss',
 'Oregon',
 'Oregon State',
 'Pacific',
 'Penn',
 'Pitt',
 'Princeton',
 'Providence',
 'Purdue',
 'Radford',
 'Rhode Island',
 'Robert Morris',
 'SMU',
 'Saint Louis',
 "Saint Mary's",
 'San Diego State',
 'Seton Hall',
 'South Carolina',
 'South Dakota State',
 'Southern',
 'St. Bonaventure',
 "St. John's (NY)",
 "St. Joseph's",
 'Stanford',
 'Stephen F. Austin',
 'Stony Brook',
 'Syracuse',
 'TCU',
 'Temple',
 'Tennessee',
 'Texas',
 'Texas A&M',
 'Texas Southern',
 'Texas Tech',
 'Troy',
 'Tulsa',
 'UC-Davis',
 'UC-Irvine',
 'UCF',
 'UCLA',
 'UConn',
 'UMBC',
 'UMass',
 'UNC',
 'UNC Asheville',
 'UNC Greensboro',
 'UNC Wilmington',
 'UNLV',
 'USC',
 'Utah',
 'Utah State',
 'VCU',
 'Valparaiso',
 'Vanderbilt',
 'Vermont',
 'Villanova',
 'Virginia',
 'Virginia Tech',
 'Washington',
 'Weber State',
 'West Virginia',
 'Western Kentucky',
 'Western Michigan',
 'Wichita State',
 'Winthrop',
 'Wisconsin',
 'Wofford',
 'Wright State',
 'Wyoming',
 'Xavier',
 'Yale'
 }
tournament_teams_13_19 = {ele.lower() for ele in tournament_teams_13_19}

def fix_team_name(team): # for an apply method
    team = team.lower()
    orig_to_jacob = {
        'gardner webb':'gardner-webb',
        'uab': 'alabama-birmingham',
        "east tennessee st." : "etsu",
        "mount st. mary's": "mount st. mary's", 
        'uc davis': 'uc-davis',
        'mississippi': 'ole miss',
        "st. john's": "st. john's (ny)",
        'miami fl': 'miami (fl)',
        'north carolina': 'unc',
        'connecticut': 'uconn',
        'uc irvine': 'uc-irvine',
        "saint joseph's": "st. joseph's",
        'louisiana lafayette': 'louisiana',
        'loyola chicago': 'loyola (il)',
        "st. bonaventure": "st. bonaventure",
        'massachusetts': 'umass',
        "north carolina st.": 'nc state',
        'pittsburgh': 'pitt',
        'albany': 'albany (ny)'
    }
    change = True
    if team in orig_to_jacob.keys():
            team = orig_to_jacob[team]
            change = False
    if 'st.' in team and change:
        team = team.replace('st.', 'state')
    return team

#def make_win_rate():
    

def make_season_stats_data(make_csv = False):
    seasons_stats_csv = os.getcwd() + "\\March Madness Data\\Season_Stat_Data_13_21\\cbb.csv"
    df = pd.read_csv(seasons_stats_csv)
    df = df.drop(['SEED','POSTSEASON'], axis = 1)
    years = list(df.YEAR.unique())
    assert min(years) == 2013
    assert max(years) == 2019
    
    df['TEAM'] = df['TEAM'].apply(fix_team_name)
    df =  df[df['TEAM'].apply(lambda x: x in tournament_teams_13_19)]
    assert sorted(list(df['TEAM'].unique())) == sorted(tournament_teams_13_19)
    
    df['WIN_RATE'] = df['W']/df['G']
    df = df.drop(['G','W'], axis = 1)
    assert 'G' not in list(df.columns)
    assert 'W' not in list(df.columns)
    assert df['WIN_RATE'].isna().sum() == 0
    
    df = df.rename(columns={'YEAR': 'Year', "TEAM" : "Team"})
    assert df['Year'].isna().sum() == 0
    assert df['Team'].isna().sum() == 0
    assert df[df['Team'] == ""].shape[0] == 0
    
    if(make_csv):
         make_season_stat_csv(df)
    return df
    

def make_season_stat_csv(df):
     df.to_csv("C:\\Users\\user\\CU_2023_Spring\Macine Learning\\ML Application Project\\MLApplication\March Madness Data\\Season_Stat_Data_13_21\\ncaam_season_stats_13-19.csv")