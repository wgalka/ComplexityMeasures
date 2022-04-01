# Zaimportowanie pakietu pandas
import numpy as np
import pandas as pd
import scipy
from sklearn import datasets as data
from complexitymeasures.stats import statslib
from scipy.stats import bartlett
from scipy.stats import shapiro

def asymmetry_measures(X):
    '''

    Returns
    -------
    asymetry_min : float
        Minimum asymmetry value from all columns
    asymetry_max : float
        Maximum asymmetry value from all columns
    asymetry_avg : float
        Average asymmetry value from all columns
    asymetry_std : float
        Standard deviation asymmetry value from all columns
    '''
    # TODO test this function
    # Przekonwertowanie na numpyarray
    X = pd.DataFrame(X)
    # Obiczenie współczynników asymetrii dla poszczególnych kolumn
    asymmetry = X.apply(statslib.assymetryfactor)
    print(asymmetry)

    # Obliczanie min, max, avg, std
    asymetry_min = np.nanmin(asymmetry)
    asymetry_max = np.nanmax(asymmetry)
    asymetry_avg = np.nanmean(asymmetry)
    asymetry_std = np.nanstd(asymmetry)

    return asymetry_min, asymetry_max, asymetry_avg, asymetry_std


def bartelet_measures(X):
    '''

    Returns
    -------
    statistic : float
        The test statistic.
    pvalue : float
        The p-value of the test.
    '''
    # TODO test this function
    # Lista zawierająca kolumny by możliwe było użycie operatora * w celu użycia jej jako parametr
    args = [X[col] for col in X.columns]

    # Obliczenie testu barteleta
    statistic, pvalue = bartlett(*args)
    return statistic, pvalue


def coefficient_measure(X):
    '''
    Returns
    -------
    asymetry_min : float
        Minimum coefficient value from all columns
    asymetry_max : float
        Maximum coefficient value from all columns
    asymetry_avg : float
        Average coefficient value from all columns
    asymetry_std : float
        Standard deviation coefficient value from all columns
    '''

    coeff = X.apply(statslib.coeff)

    ## Obliczanie min, max, avg, std
    coeff_min = np.nanmin(coeff)
    coeff_max = np.nanmax(coeff)
    coeff_avg = np.nanmean(coeff)
    coeff_std = np.nanstd(coeff)

    return coeff_min, coeff_max, coeff_avg, coeff_std


def correlation_measures(X):
    '''
    Returns
    -------
    corr_min : float
        Minimum corelation value from corelationmatrix
    corr_max : float
        Maximum corelation value from corelationmatrix
    corr_avg : float
        Average corelation value from corelationmatrix
    corr_std : float
        Standard derviation corelation value from corelationmatrix
    corr_V : float
        Coefficient of variation from corelation matrix
    '''
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

    return corr_min, corr_max, corr_avg, corr_std, corr_V


def kurtosis_measure(X):
    '''
    Returns
    -------
    corr_min : float
       Minimum kurtosis value from all comlumns
    corr_max : float
       Maximum kurtosis value from all comlumns
    corr_avg : float
       Average kurtosis value from all comlumns
    corr_std : float
       Standard derviation kurtosis value from all comlumns
    '''
    kurtosis = X.apply(scipy.stats.kurtosis)
    print(kurtosis)

    ## Obliczanie min, max, avg, std
    kurtosis_min = np.nanmin(kurtosis)
    kurtosis_max = np.nanmax(kurtosis)
    kurtosis_avg = np.nanmean(kurtosis)
    kurtosis_std = np.nanstd(kurtosis)

    return kurtosis_min, kurtosis_max, kurtosis_avg, kurtosis_std

def shapiro_measure(X):
    '''

    Returns
    -------
    statistic : float
        The test statistic.
    pvalue : float
        The p-value of the test.
    '''

    statistic, pvalue = shapiro(X)
    return statistic, pvalue