import pandas as pd

from MATRIX_MANIPULATION import matrix_collation
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

main_df = matrix_collation()

new_year_arr = [str(num) for num in range(2024, 2033)]

def find_value_of_d_model(key: str):
    column_of_interest = main_df[key]
    times_diff = 0

    while True:
        result = adfuller(column_of_interest)
        p_value = result[1]  # Get the p-value from the test result

        if p_value < 0.05:  # Check if the series is stationary
            print(f"The series is stationary after {times_diff} differencing. {p_value}")
            break
        else:
            # Apply first difference and drop NaN values
            column_of_interest = column_of_interest.diff().dropna()
            times_diff += 1  # Increment the differencing count
            print(f"Current p-value: {p_value}. Series is not stationary, applying differencing {times_diff}.")
    return times_diff

def visualize_for_pacf_and_acf_values(column_of_interest):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    plot_acf(column_of_interest, ax=axs[0])

    plot_pacf(column_of_interest, ax=axs[1])

    plt.tight_layout()
    plt.show()

def model_score(column_of_interest, forecast):
    mse = mean_squared_error(column_of_interest, forecast)
    print(f"MSE: {mse}")

column_of_interest = main_df['GDP Per Capita Growth']
# d_value = find_value_of_d_model('GDP Per Capita Growth')
# d = 2

# visualize_for_pacf_and_acf_values(column_of_interest)
# p = 1
# q = 1

pred_model = ARIMA(column_of_interest, order=(1, 4, 1))
pred_model_fit = pred_model.fit()

forecast = pred_model_fit.forecast(steps=9)
new_GDP_arr = forecast.values.flatten().tolist()
previous_GDP_arr = column_of_interest.values.flatten().tolist()
previous_GDP_arr.extend(new_GDP_arr)

previous_year_arr = main_df['Year'].values.flatten().tolist()
previous_year_arr.extend(new_year_arr)

new_df = {
    "Year": previous_year_arr,
    'GDP Per Capita Growth': previous_GDP_arr
}
predicted_df = pd.DataFrame(new_df)

def visualize_graph():
    plt.plot(previous_year_arr, previous_GDP_arr, color="red", label="GDP Prediction trend")
    plt.title(f"Prediction for 9 years ahead and trend for GDP per Capita Growth", fontweight='bold', fontsize=16)
    plt.xlabel(f"Year", fontweight='bold', fontsize=13)
    plt.ylabel(f"GDP per capita growth (%)", fontweight='bold', fontsize=13)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend()
    plt.show()

visualize_graph()