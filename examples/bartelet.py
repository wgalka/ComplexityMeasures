# 5. Cecha mówiąca o tym, czy macierz korelacji jest istotnie różna od jednostkowej (test Bartleta)
# https://statystycznie-istotne.pl/slownik-statystyczny/wspolczynnik-kmo-test-sferycznoscibartletta

from scipy.stats import bartlett
# Zaimportowanie pakietu pandas
from sklearn import datasets as data

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartość inf pvalue=0.0?
X = X.iloc[:, 1:5]
print(X)

args = []
for col in X.columns:
    args.append(X[col])

# Obliczenie testu barteleta
statisctic, pvalue = bartlett(*args)
print(statisctic, pvalue)
