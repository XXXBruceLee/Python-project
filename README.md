# Final Project: GDP Forecasting Model Based on Data from Three East Asian Countries

## 📌 Project Overview
This project analyzes economic indicators such as **GDP, Household Consumption, Government Spending, Exports, and Imports** for three countries: **China (CHN), South Korea (KOR), and Japan (JPN)**.

The data is retrieved from the **World Bank API (WBGAPI)** and processed using **Python**.  
It allows for insights into economic trends over time, helping users visualize key indicators from **1970 to 2022**.

To predict future GDP trends, we use the **ARIMA (AutoRegressive Integrated Moving Average) model**, a widely used statistical model for time series forecasting. By applying ARIMA to historical GDP data, we can generate reliable forecasts and observe economic patterns over time.

### ✅ GDP Calculation Formula
In this project, GDP is calculated using the expenditure approach, which sums up the following components:

\[
GDP = C + I + G + (X - M)
\]

Where:
- **C** = Consumer spending (Household consumption)
- **I** = Private investment (Gross investment)
- **G** = Government spending
- **X - M** = Net exports (Exports - Imports)

The formula provides a comprehensive view of how different sectors (household, investment, government, and foreign trade) contribute to a country's GDP.


## 🛠 Technologies Used
- **Python 3.x**
- **Pandas & NumPy** (Data manipulation)
- **Matplotlib & Seaborn** (Data visualization)
- **WBGAPI** (World Bank API for economic data)


## 📊 Dataset Information
The project collects data for the following indicators:

- GDP (Gross Domestic Product)
- Household Consumption
- Gross Investment
- Government Spending
- Exports
- Imports

The dataset spans from 1970 to 2022, with yearly data for China, South Korea, and Japan.


## 📈 Example Visualization
This project provides visualizations to explore economic trends:

### - GDP Trend Over Years
  
  <img src="https://github.com/user-attachments/assets/c046d286-6fb1-4ea3-a4f7-759a30373059" alt="GDP Chart" width="800"/>

  This visualization represents the **GDP growth trends** of China, Japan, and South Korea over time. By analyzing these trends, we can briefly compare the economic growth patterns of each country and identify major economic shifts, such as rapid growth or recessions.


### - GDP Composition Breakdown Over Time

  <img src="https://github.com/user-attachments/assets/cae57939-cff8-4433-b201-66cc542b5d21" alt="GDP Composition" width="800"/>

  This visualization illustrates how the **composition of GDP** (household consumption, investment, government spending, exports, and imports) has changed over time. By analyzing these proportions, we can observe how the share of consumption, investment, exports, etc., has changed over time and compare the **economic structures** of different countries.

  
### - Trends in GDP Composition Over Time

  <img src="https://github.com/user-attachments/assets/b96cea01-3c12-430a-b3b4-7ac88f40f1fc" alt="Trends in GDP Composition" width="800"/>

  Unlike the previous chart, this line graph highlights **how these GDP components evolve over time**. It allows us to analyze **long-term economic transformations** and detect shifts in economic strategy.


### - GDP Composition Comparison Across Countries

  <img src="https://github.com/user-attachments/assets/69892e95-5281-423f-9f36-a7a323f83d1a" alt="GDP Composition Comparison" width="800"/>

  This bar chart compares the **average proportion of GDP components** for the three countries. By analyzing these differences, we can determine whether a country’s economy is **consumption-driven, investment-driven, or export-driven**  and compare **government spending, investment, and trade dependency** across nations. This visualization provides insights into the **structural differences between their economies.**

---
The insights gained from the above analyses and  visualizations serve as a foundation for the **ARIMA model**:
- **Identifying patterns:** The visualizations help detect patterns in GDP and its components, which ARIMA uses for accurate forecasting.
- **Understanding key drivers:** By analyzing GDP components, we can better interpret the ARIMA predictions, linking future GDP growth to specific factors like exports or government spending.
- **Improving forecasting reliability:** The background analysis ensures that ARIMA is not just a "black box" model, but is supported by clear economic insights.


## 👥 Team Members
- Eungyeol Kang
- Awuzhaer Abudurexiti
