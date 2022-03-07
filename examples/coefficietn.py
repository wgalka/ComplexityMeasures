# 2. Współczynnik zmienności
# https://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_zmienno%C5%9Bci

# Zaimportowanie pakietu pandas
import numpy as np
from sklearn import datasets as data

from statslib.statslib import statslib

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Odrzucamy kolumny z samymi 0 - wpsółczynnik zmiennośći wyniesie wtedy nan
X = X.iloc[:, 1:4]
print(X)

# Obiczenie współczynników zmiennośći
# Co w sytuacji gdy odchylenie jest bardzo wysokie?

coeff = []
for col_name in X.columns:
    coeff.append(statslib.coeff(X[col_name]))  # TODO Optymalizacja impotru pakietów
print(coeff)

## Obliczanie min, max, avg, std
coeff_min = np.nanmin(coeff)
coeff_max = np.nanmax(coeff)
coeff_avg = np.nanmean(coeff)
coeff_std = np.nanstd(coeff)
print(f'''\
min: {coeff_min} 
max: {coeff_max}
avg: {coeff_avg}
std: {coeff_std}''')
