import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import sklearn.model_selection as ms
from MATRIX_MANIPULATION import matrix_collation

main_df = matrix_collation()
# research_df = main_df.drop(columns=['Year'])
# correlation = research_df.corr(method="pearson")
# print(correlation.to_string())
X_df = main_df[['GDP Per Capita Growth', 'Average Education Completion SD', 'Average Education Completion SMP', 'Average Education Completion SMA']]
Y_df = main_df[['Urban Unemployment', 'Rural Unemployment']]

X_train, X_test, Y_train, Y_test = ms.train_test_split(X_df, Y_df, test_size=0.2, random_state=0)

# Map the Unemployment Rate
main_df['Urban Unemployment'] = pd.to_numeric(main_df['Urban Unemployment'])
urban_values = main_df['Urban Unemployment']
urban_arr = urban_values.values.flatten().tolist()

year_arr = main_df['Year'].values.flatten().tolist()

main_df['Rural Unemployment'] = pd.to_numeric(main_df['Rural Unemployment'])
rural_values = main_df['Rural Unemployment']
rural_arr = rural_values.values.flatten().tolist()

main_df['GDP Per Capita Growth'] = pd.to_numeric(main_df['GDP Per Capita Growth'])
GDP_values = main_df['GDP Per Capita Growth']
GDP_arr = GDP_values.values.flatten().tolist()

def visualize_year_urban_rural():
    plt.plot(year_arr, urban_arr, color='red', label='Urban Unemployment')
    plt.plot(year_arr, rural_arr, color='blue', label='Rural Unemployment')
    plt.title("Visualization of urban and rural distribution for Indonesia", fontweight='bold', fontsize=16)
    plt.xlabel("Year", fontweight='bold', fontsize=13)
    plt.ylabel("Unemployment rate", fontweight='bold', fontsize=13)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend()
    plt.show()

visualize_year_urban_rural()

def visualize_gdp_growth():
    plt.plot(year_arr, GDP_arr, color="green", label='GDP Growth')
    plt.title("Visualization of GDP per capita growth for Indonesia", fontweight='bold', fontsize=16)
    plt.xlabel("Year", fontweight='bold', fontsize=13)
    plt.ylabel("GDP growth", fontweight='bold', fontsize=13)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend()
    plt.show()

visualize_gdp_growth()

prediction_model = lm.LinearRegression()
prediction_model.fit(X_train, Y_train)

intercept = prediction_model.intercept_
print(intercept)
coef = prediction_model.coef_
print(coef)

# Find the score
model_score = prediction_model.score(X_test, Y_test)
print(model_score)

urban_y_values = intercept[0]
rural_y_values = intercept[1]

urban_predictor_values = coef[0]
rural_predictor_values = coef[1]

def get_urban_trend():
    plt.scatter(year_arr, urban_arr)
    plt.scatter(year_arr, rural_arr)
    # x1 = np.linspace(0, 8)
    # x2 = x1
    # x3 = x1
    # x4 = x1
    # y1 = urban_y_values + urban_predictor_values[0] * x1 + urban_predictor_values[1] * x2 + urban_predictor_values[2] * x3 + urban_predictor_values[3] * x4
    # y2 = rural_y_values + rural_predictor_values[0] * x1 + rural_predictor_values[1] * x2 + rural_predictor_values[2] * x3 + rural_predictor_values[3] * x4
    # plt.plot(x1, y1)
    # plt.plot(x1, y2)
    plt.show()

# get_urban_trend()