import numpy as np


# coefficient facor https://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_zmienno%C5%9Bci
def coeff(X):
    return np.nanstd(X) / np.nanmean(X)


# Assymetry factor https://pl.wikipedia.org/wiki/Wsp%C3%B3%C5%82czynnik_asymetrii
def assymetryfactor(X):
    # TODO test this implementation
    X = X.copy()
    ## Obliczenie trzeciego momentu
    # Obliczenie średniej
    mean = np.mean(X)
    # Od każdego elementu odejmujemy średnią
    X = X - mean
    # Podnosimy obliczoną wartość do potęgi 3
    X = np.power(X, 3)
    # Sumujemy wartości
    sum_ = np.sum(X)
    # Obliczenie odchylenia standardowego
    std = np.nanstd(X)
    return sum_ / (std ** 3)
