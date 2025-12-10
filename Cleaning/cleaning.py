import pandas as pd
import numpy as np
import datetime as dt

playerData = pd.read_csv('../Merging/merged_seasons.csv', low_memory=False)
teamData = pd.read_csv('../data/master_team_list.csv')

cleanedPlayers = playerData

cleanedPlayers['season_x'] = cleanedPlayers['season_x'].astype(str)
cleanedPlayers['name'] = cleanedPlayers['name'].astype(str)
cleanedPlayers['position'] = cleanedPlayers['position'].astype(str)
cleanedPlayers['team'] = cleanedPlayers['team'].astype(str)
cleanedPlayers['saves'] = pd.to_numeric(cleanedPlayers['saves'], downcast='integer',errors='coerce')

cleanedPlayers['season_x'] = cleanedPlayers['season_x'].astype("category").cat.codes
cleanedPlayers['name'] = cleanedPlayers['name'].astype("category").cat.codes
cleanedPlayers['position'] = cleanedPlayers['position'].astype("category").cat.codes
cleanedPlayers['team'] = cleanedPlayers['team'].astype("category").cat.codes
cleanedPlayers['was_home'] = cleanedPlayers['was_home'].astype("category").cat.codes

cleanedPlayers['kickoff_time'] = pd.to_datetime(cleanedPlayers['kickoff_time'])
cleanedPlayers['day_of_week'] = cleanedPlayers['kickoff_time'].dt.dayofweek
cleanedPlayers['hour'] = cleanedPlayers['kickoff_time'].dt.hour

#just dropping the modified column
cleanedPlayers = cleanedPlayers.drop(['kickoff_time','modified'], axis=1)
"""
0 :2020-21
1 :2021-22
2 :2022-23
3 :2023-24
4 :2024-25
5 :2025-26
"""

tableOne = cleanedPlayers[cleanedPlayers['season_x'] == 0]
tableTwo = cleanedPlayers[cleanedPlayers['season_x'] == 1]
tableThree = cleanedPlayers[cleanedPlayers['season_x'] == 2]
tableFour = cleanedPlayers[cleanedPlayers['season_x'] == 3]
tableFive = cleanedPlayers[cleanedPlayers['season_x'] == 4]

cleanedPlayers.to_csv('cleanedPlayers.csv', index=False)