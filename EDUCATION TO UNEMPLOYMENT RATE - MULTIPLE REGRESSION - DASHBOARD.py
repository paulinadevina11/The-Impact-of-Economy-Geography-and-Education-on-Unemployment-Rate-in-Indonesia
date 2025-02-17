import pandas as pd

from MATRIX_MANIPULATION import matrix_collation, find_indonesia_unemployment_rate
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error

main_df = matrix_collation()
main_df = main_df.loc[:6]

unemployment_df = find_indonesia_unemployment_rate()
unemployment_df = unemployment_df.loc[3:9]

collation_matrix = pd.merge(main_df, unemployment_df, on=['Year'])

feature_X = collation_matrix[['Average Education Completion SD', 'Average Education Completion SMP', 'Average Education Completion SMA']]
target = collation_matrix['Unemployment Rate']

X_train, X_test, Y_train, Y_test = ms.train_test_split(feature_X, target, test_size=0.2, random_state=10)

model = lm.LinearRegression()
model.fit(X_train, Y_train)

m = model.coef_.flatten().astype("float")
c = model.intercept_.flatten().astype("float")

Y_pred = model.predict(X_test)
# print(X_test)
# print(model_unemployment_pred_test)

error = mean_squared_error(Y_test, Y_pred)

score = model.score(X_test, Y_test)

# Step 1: Scatter plot of Year vs Actual Unemployment Rate
plt.figure(figsize=(8,6))
plt.scatter(collation_matrix['Year'].values.flatten().tolist(), target, label='Actual Unemployment Rate', color='blue')

# Step 2: Line plot showing the predicted values (if you have predictions)
y_pred = model.predict(feature_X)  # Assuming you've already trained the model and have predictions
plt.plot(collation_matrix['Year'].values.flatten().tolist(), y_pred, color='red', lw=2, label='Predicted Unemployment Rate')

# Step 3: Customize plot
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.title('Year vs Unemployment Rate (Actual vs Predicted)')
plt.legend()  # Adding a legend for clarity
plt.show()

