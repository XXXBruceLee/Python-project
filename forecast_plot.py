
import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(arima_result, stationary_series, forecast_steps=10):
    forecast_result = arima_result.get_forecast(steps=forecast_steps)
    forecast_mean = forecast_result.predicted_mean  
    forecast_ci = forecast_result.conf_int()  

    forecast_index = pd.date_range(start=stationary_series.index[-1], periods=forecast_steps+1, freq='YS')[1:]

    forecast_mean.index = forecast_index
    forecast_ci.index = forecast_index

    plt.figure(figsize=(12, 6))
    plt.plot(stationary_series, label="Observed", color="blue") 
    plt.plot(forecast_mean, label="Forecast", color="green")  
    plt.fill_between(
        forecast_ci.index, forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1],
        color="gray", alpha=0.3, label="Confidence Interval"
    ) 
    plt.title("ARIMA Model Forecast")
    plt.xlabel("Year")
    plt.ylabel("Log Transformed GDP")
    plt.legend()
    plt.grid(True)
    plt.show()
