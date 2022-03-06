"""1. Wartości w macierzy korelacji cech warunkowych zbioru danych
https://pl.wikipedia.org/wiki/Macierz_korelacji"""

# Zaimportowanie pakietu pandas
import pandas as pd
from sklearn import datasets as data



# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
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

# Obliczanie min, max, avg
n_cols = corrMatrix.shape[1]

