
from statsmodels.tsa.stattools import adfuller
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def process_gdp_data(combined_data):
    """ Process GDP data and return log-transformed time series """
    KOR_GDP = combined_data.filter(like="GDP_YR").loc["KOR"]
    KOR_GDP.index = KOR_GDP.index.str.replace("GDP_YR", "", regex=True)
    KOR_GDP.index = pd.to_datetime(KOR_GDP.index, format="%Y")
    KOR_GDP.replace(0, np.nan, inplace=True)
    KOR_GDP.ffill(inplace=True)

    print("Number of missing values:", KOR_GDP.isna().sum())
    print(KOR_GDP.head())

    KOR_GDP_log = np.log1p(KOR_GDP)

    if KOR_GDP_log.nunique() == 1:
        print("Warning: The data is a constant, and the first-order difference is performed")
        KOR_GDP_log = KOR_GDP_log.diff().dropna()

    return KOR_GDP_log

def adf_test(series):
    """ Perform ADF test and plot log-transformed GDP """
    result = adfuller(series.dropna())
    print("Original Log GDP ADF Statistic:", result[0], "p-value:", result[1])

    plt.figure(figsize=(12, 6))
    plt.plot(series, label="Log Transformed GDP")
    plt.title("Log Transformed GDP (South Korea)")
    plt.legend()
    plt.show()
