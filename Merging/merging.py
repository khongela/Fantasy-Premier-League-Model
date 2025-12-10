import numpy as np 
import pandas as pd

"""
1: 2020-21
2: 2021-22
3: 2022-23
4: 2023-24
5: 2024-25
6: 2025-26

This is meant to merge all the season's data into a single master file used for training
"""

tableOne = pd.read_csv('merged_gw_20_21.csv', low_memory=False)
tableTwo = pd.read_csv('merged_gw_21_22.csv', low_memory=False)
tableThree = pd.read_csv('merged_gw_22_23.csv', low_memory=False)
tableFour = pd.read_csv('merged_gw_23_24.csv', low_memory=False)
tableFive = pd.read_csv('merged_gw_24_25_cleaned.csv',low_memory=False)

#adding season column to each data frame
tableOne['season_x'] = "2020-21"
tableTwo['season_x'] = "2021-22"
tableThree['season_x'] = "2022-23"
tableFour['season_x'] = "2023-24"
tableFive['season_x'] = "2024-25"

frames = [tableOne, tableTwo, tableThree, tableFour, tableFive]
merged_seasons = pd.concat(frames, ignore_index=True, sort=False)

merged_seasons.to_csv('merged_seasons.csv', index=False)



