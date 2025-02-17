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
            # print(f"The series is stationary after {times_diff} differencing. {p_value}")
            break
        else:
            # Apply first difference and drop NaN values
            column_of_interest = column_of_interest.diff().dropna()
            times_diff += 1  # Increment the differencing count
            # print(f"Current p-value: {p_value}. Series is not stationary, applying differencing {times_diff}.")
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


d_urban_value = find_value_of_d_model('Urban Unemployment')
urban_df = main_df['Urban Unemployment']

model = ARIMA(urban_df, order=(1, 2, 1))
model_fit = model.fit()
forecase = model_fit.forecast(steps=9)

# For Urban unemployment, the p, d, q is 1, 2, 1

urban_forecast_data = {
    'Year': new_year_arr,
    'Urban Unemployment Prediction': forecase.values.flatten().tolist()
}
urban_prediction = pd.DataFrame(urban_forecast_data)

d_rural_value = find_value_of_d_model('Rural Unemployment')
rural_df = main_df['Rural Unemployment']
# visualize_for_pacf_and_acf_values(rural_df)
# p = 1
# q = 1
model_2 = ARIMA(rural_df, order=(1, 0, 1))
model_2_fit = model_2.fit()
forecast = model_2_fit.forecast(steps=9)

# For rural unemployment, the p, d, q is 1, 0, 1

rural_forecast_data = {
    'Year': new_year_arr,
    'Rural Unemployment Prediction': forecast.values.flatten().tolist()
}
rural_prediction = pd.DataFrame(rural_forecast_data)

urban_rural_prediction = pd.merge(urban_prediction, rural_prediction, on=['Year'])

urban_arr = urban_rural_prediction["Urban Unemployment Prediction"].values.flatten().tolist()
rural_arr = urban_rural_prediction['Rural Unemployment Prediction'].values.flatten().tolist()

previous_urban_arr = main_df['Urban Unemployment'].values.flatten().tolist()
previous_rural_arr = main_df['Rural Unemployment'].values.flatten().tolist()
year_arr = main_df['Year'].values.flatten().tolist()
plt.plot(year_arr, previous_urban_arr, color="red", label="Urban Unemployment")
plt.plot(year_arr, previous_rural_arr, color="blue", label='Rural Unemployment')
plt.title(f"Visualization of urban and rural distribution", fontweight='bold', fontsize=16)
plt.xlabel(f"Year", fontweight='bold', fontsize=13)
plt.ylabel(f"Unemployment Rate", fontweight='bold', fontsize=13)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.legend()
plt.show()

for values in urban_arr:
    previous_urban_arr.append(values)

for values in rural_arr:
    previous_rural_arr.append(values)

for values in new_year_arr:
    year_arr.append(values)

main_dataframe = {
    "Year": year_arr,
    'Urban Unemployment': previous_urban_arr,
    'Rural Unemployment': previous_rural_arr
}

main_df = pd.DataFrame(main_dataframe)

def visualize_graph():
    plt.plot(year_arr, previous_urban_arr, color="red", label="Urban trend")
    plt.plot(year_arr, previous_rural_arr, color="blue", label="Rural trend")
    plt.title(f"Prediction for 9 years ahead and trend for Unemployment Rate", fontweight='bold', fontsize=16)
    plt.xlabel(f"Year", fontweight='bold', fontsize=13)
    plt.ylabel(f"Unemployment Rate", fontweight='bold', fontsize=13)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend()
    plt.show()

visualize_graph()
