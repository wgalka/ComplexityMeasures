"""3. Współczynnik asymetrii
https://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_asymetrii"""

# Zaimportowanie pakietu pandas
import numpy as np
from sklearn import datasets as data

from statslib.statslib import statslib

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartośći nan
X = X.iloc[:, 1:5]
print(X)

# Obiczenie współczynników asymetrii
asymmetry = X.apply(statslib.assymetryfactor)
print(asymmetry)

## Obliczanie min, max, avg, std
asymetry_min = np.nanmin(asymmetry)
asymetry_max = np.nanmax(asymmetry)
asymetry_avg = np.nanmean(asymmetry)
asymetry_std = np.nanstd(asymmetry)
print(f'''\
min: {asymetry_min} 
max: {asymetry_max}
avg: {asymetry_avg}
std: {asymetry_std}''')
