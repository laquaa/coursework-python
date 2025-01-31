import pandas as pd
from sklearn.ensemble import IsolationForest
import numpy as np
from find_critical_points import find_critical_points
all_critical_points_position = []
dataframe = pd.read_csv('AAPL.csv')
iso_forest = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.01), random_state=42)
iso_forest.fit(dataframe['Close'].values.reshape(-1, 1))
dataframe['scores'] = iso_forest.decision_function(dataframe['Close'].values.reshape(-1, 1))
dataframe['anomaly'] = iso_forest.predict(dataframe['Close'].values.reshape(-1, 1))
dataframe[ 'close_interpolated'] = dataframe['Close']
dataframe.loc[dataframe['anomaly'] == -1, 'close_interpolated'] = np.nan
dataframe['close_interpolated'] = dataframe['close_interpolated'].interpolate(method='linear')
dataframe['close_interpolated'] = dataframe['close_interpolated'].bfill()
critical_points_position = find_critical_points(dataframe['close_interpolated'])
dataframe['critical_points'] = 0
for j in critical_points_position:
    dataframe.loc[j, 'critical_points'] = 1