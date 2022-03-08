# 4. Kurtoza
# https://pl.wikipedia.org/wiki/Kurtoza
# Cechy to: Min, Max, Avg, StdDev dla kurtoz wszystkich cech warunkowych

# Zaimportowanie pakietu pandas
import numpy as np
from scipy.stats import kurtosis
from sklearn import datasets as data

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartość -3?
X = X.iloc[:, 0:5]
print(X)

# Obiczenie kurtoz
kurtosis = X.apply(kurtosis)
print(kurtosis)

## Obliczanie min, max, avg, std
kurtosis_min = np.nanmin(kurtosis)
kurtosis_max = np.nanmax(kurtosis)
kurtosis_avg = np.nanmean(kurtosis)
kurtosis_std = np.nanstd(kurtosis)
print(f'''\
min: {kurtosis_min} 
max: {kurtosis_max}
avg: {kurtosis_avg}
std: {kurtosis_std}''')
