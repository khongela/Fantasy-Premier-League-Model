import pandas as pd 
import numpy as np
import datetime as dt

playerData = pd.read_csv('../Cleaning/cleanedPlayers.csv')
laggedPlayers = playerData.copy()
laggedPlayers = laggedPlayers.sort_values(by=['name','season_x','GW'])

features_to_lag = [
    'total_points', 
    'minutes', 
    'goals_scored', 
    'assists', 
    'ict_index', 
    'threat',           
    'creativity',      
    'selected',         
    'transfers_in',     
    'goals_conceded',
    'xP',
    'bps',
    'bonus',
    'clean_sheets',
    'influence',
    'saves',
    'expected_goals',
    'expected_assists',
    'expected_goal_involvements',
    'expected_goals_conceded',
    'value'
]

for col in features_to_lag:
    lag_col_name = f'last_{col}'
    laggedPlayers[lag_col_name] = laggedPlayers.groupby('name')[col].shift(1)
    laggedPlayers[f'avg_{col}_3'] = laggedPlayers.groupby('name')[lag_col_name].rolling(3).mean().reset_index(0, drop=True)

laggedPlayers = laggedPlayers.dropna()
print(laggedPlayers.dtypes)
print(laggedPlayers)
laggedPlayers.to_csv('Lagged.csv', index=False)

