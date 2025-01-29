
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

def plot_acf_pacf(series, lags=20):
    plt.figure(figsize=(12, 6))
    plot_acf(series, lags=lags)
    plt.title("Autocorrelation Function (ACF)")
    plt.show()

    plt.figure(figsize=(12, 6))
    plot_pacf(series, lags=lags, method='ywm')
    plt.title("Partial Autocorrelation Function (PACF)")
    plt.show()
