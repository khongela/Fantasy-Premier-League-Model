import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd

features = [
    'last_total_points', 
    'avg_total_points_3', 
    'last_minutes', 
    'avg_minutes_3', 
    'last_goals_scored',   
    'avg_goals_scored_3', 
    'last_assists',
    'avg_assists_3',
    'last_ict_index',
    'avg_ict_index_3',
    'last_threat',           
    'avg_threat_3',          
    'last_creativity',
    'avg_creativity_3',
    'last_influence',
    'avg_influence_3',
    'last_bps',
    'avg_bps_3',
    'last_bonus',
    'avg_bonus_3',
    'last_clean_sheets',
    'avg_clean_sheets_3',
    'last_expected_goals',
    'avg_expected_goals_3',
    'last_expected_assists',
    'avg_expected_assists_3',
    'last_expected_goal_involvements',
    'avg_expected_goal_involvements_3',
    'last_expected_goals_conceded',
    'avg_expected_goals_conceded_3',
    'last_value',
    'avg_value_3',
    'last_transfers_in',
    'last_goals_conceded',
    'avg_goals_conceded_3', 
    'value',            
    'was_home',        
    'opponent_team',    
    'position',
    'day_of_week',
    'hour'
]

"""
0 :2020-21
1 :2021-22
2 :2022-23
3 :2023-24
4 :2024-25
"""

dataset = pd.read_csv('../Feauture_Engineering/Lagged.csv')
dataset = dataset[dataset['minutes'] > 0]
train = dataset[dataset['season_x'].isin([0,1,2,3])]
test = dataset[dataset['season_x'] == 4]

x_train = train[features]
y_train = train['total_points']

x_test = test[features]
y_test = test['total_points']

model = xgb.XGBRegressor(
    objective='reg:squarederror', 
    n_estimators=500,             
    learning_rate=0.05,           
    max_depth=5,                  
    random_state=42
)

model.fit(x_train, y_train)
predictions = model.predict(x_test)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

print(f"Average Error (RMSE): {rmse:.2f}")

print("\n What mattered most?")
for feature, importance in zip(features, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")