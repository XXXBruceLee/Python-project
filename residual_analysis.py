
from statsmodels.stats.diagnostic import acorr_ljungbox
import scipy.stats as stats
import matplotlib.pyplot as plt

def analyze_residuals(arima_result, lags=10):
    residuals = arima_result.resid
    ljungbox_test = acorr_ljungbox(residuals, lags=[lags], return_df=True)
    print("Ljung-Box Test Results:\n", ljungbox_test)

    plt.figure(figsize=(8, 6))
    stats.probplot(residuals, dist="norm", plot=plt)
    plt.title("QQ Plot of Residuals")
    plt.grid(True)
    plt.show()
