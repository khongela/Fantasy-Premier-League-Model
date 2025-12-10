import pandas as pd
import numpy as np

cleanedPlayers = pd.read_csv('cleanedPlayers.csv', low_memory=False)
cleanedPlayers = cleanedPlayers[cleanedPlayers['position'] != 0]

#replacing the xG values with -1s
replacingDict = {
 "expected_assists": -1,
 "expected_goal_involvements": -1,
 "expected_goals": -1,
 "expected_goals_conceded": -1,
 "starts": -1,
 "modified": -1   
}
cleanedPlayers.fillna(replacingDict, inplace=True) 

print(cleanedPlayers.dtypes)

