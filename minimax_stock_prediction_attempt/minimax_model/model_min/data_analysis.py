import os
import re
import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
from find_critical_points import find_critical_points
folder_path = 'stock_data'
pattern = r'^AAPL\d+\.csv$'
files = os.listdir(folder_path)
aapl_files = [file for file in files if re.match(pattern, file)]
number_of_files = len(aapl_files)
aapl_files_paths = []
for file_name in aapl_files:
    file_name = 'stock_data/' + file_name
    aapl_files_paths.append(file_name)
dataframes = [pd.read_csv(file) for file in aapl_files_paths]
number_of_critical_points = []
all_critical_points_positions = []
for i in range(number_of_files):
    dataframes[i]['average_price'] = (dataframes[i]['开盘'] + dataframes[i]['收盘']) / 2
    iso_forest = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.01), random_state=42)
    iso_forest.fit(dataframes[i][['average_price']])
    dataframes[i].loc[:, 'scores'] = iso_forest.decision_function(dataframes[i][['average_price']])
    dataframes[i].loc[:, 'anomaly'] = iso_forest.predict(dataframes[i][['average_price']])
    dataframes[i].loc[:, 'average_price_interpolated'] = dataframes[i]['average_price']
    dataframes[i].loc[dataframes[i]['anomaly'] == -1, 'average_price_interpolated'] = np.nan
    dataframes[i].loc[:, 'average_price_interpolated'] = dataframes[i].loc[:,'average_price_interpolated'].interpolate(method='linear')
    dataframes[i].loc[:, 'average_price_interpolated'] = dataframes[i].loc[:, 'average_price_interpolated'].bfill()
    critical_points_position = find_critical_points(dataframes[i]['average_price_interpolated'])
    number_of_critical_points.append(len(critical_points_position))
    all_critical_points_positions.append(critical_points_position)
    dataframes[i]['critical_points'] = 0
    for j in critical_points_position:
        dataframes[i].loc[j, 'critical_points'] = 1