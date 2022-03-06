"""1. Wartości w macierzy korelacji cech warunkowych zbioru danych
https://pl.wikipedia.org/wiki/Macierz_korelacji"""

# Zaimportowanie pakietu pandas
import numpy as np
from sklearn import datasets as data

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartośći nan
X = X.iloc[:, 1:4]
print(X)

# Macierz korelacji można wykonać tylko dla danych numerycznych
print(X.dtypes)

# Stworznie macierzy korelacji. Dostępne metody:
#             * pearson : standard correlation coefficient
#             * kendall : Kendall Tau correlation coefficient
#             * spearman : Spearman rank correlation
#             * callable : input two 1d ndarrays
#                 and returning a float. Must be simetric
corrMatrix = X.corr('spearman')
print(corrMatrix)

## Obliczanie min, max, avg, std
n_cols = corrMatrix.shape[1]
# Stworzenie maski odrzucającej jedynki na przekątnej
mask = np.eye(n_cols, dtype=bool)
m_corrMatrix = np.ma.masked_array(data=corrMatrix, mask=mask)
print(m_corrMatrix)
corr_min = np.nanmin(m_corrMatrix)
corr_max = np.nanmax(m_corrMatrix)
corr_avg = np.nanmean(m_corrMatrix)
corr_std = np.nanstd(m_corrMatrix)
# https://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_zmienno%C5%9Bci
corr_V = corr_std / corr_avg
print(f'''\
min: {corr_min} 
max: {corr_max}
avg: {corr_avg}
std: {corr_std}
V:   {corr_V}''')
