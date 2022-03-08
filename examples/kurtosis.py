# 4. Kurtoza
# https://pl.wikipedia.org/wiki/Kurtoza
# Cechy to: Min, Max, Avg, StdDev dla kurtoz wszystkich cech warunkowych

# Zaimportowanie pakietu pandas
import numpy as np
from sklearn import datasets as data
from scipy.stats import kurtosis
from statslib.statslib import statslib

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartość -3?
X = X.iloc[:, 0:5]
print(X)

# Obiczenie kurtoz
curtosis = []
for col_name in X.columns:
    curtosis.append(kurtosis(X[col_name]))
print(curtosis)

## Obliczanie min, max, avg, std
curtosis_min = np.nanmin(curtosis)
curtosis_max = np.nanmax(curtosis)
curtosis_avg = np.nanmean(curtosis)
curtosis_std = np.nanstd(curtosis)
print(f'''\
min: {curtosis_min} 
max: {curtosis_max}
avg: {curtosis_avg}
std: {curtosis_std}''')