# 6. Cecha numeryczna, która zlicza udział cech warunkowych mających rozkład normalny do
# wszystkich cech (dla każdej cechy można to stwierdzić testem Shapiro-wilka)

# Zaimportowanie pakietu pandas
from sklearn import datasets as data
from scipy.stats import shapiro

# Wczytanie danych ASTMA
# X = pd.read_csv(r'C:\UR\ASTMA\mikromacierze.csv', ';', decimal=',').iloc[:, 2:]

# Wczytanie przykładowych danych
X, y = data.load_digits(n_class=2, return_X_y=True, as_frame=True)
# Jeśli w jakijś kolumnie pojawią się same 0 wtedy otzymamy wartośći nan
X = X.iloc[:, 1:5]
print(X)

# Test Shapiro-wilika
statistic, pvalue = shapiro(X)

print(f'''\
statistic: {statistic}
pvalue: {pvalue}\
''')
