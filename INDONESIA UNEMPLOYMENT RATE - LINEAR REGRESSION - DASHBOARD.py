import numpy as np

from ML_MAIN import *
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.linear_model as lm

year_arr, unemployment_arr, main_df = first_analysis()

X_idx = np.array(main_df.index).reshape(-1, 1)
unemployment_df = pd.DataFrame(unemployment_arr)

X_train, X_test, Y_train, Y_test = ms.train_test_split(X_idx, unemployment_df, test_size=0.5, random_state=0)

# Find the value of c and m
model = lm.LinearRegression()
model.fit(X_train, Y_train)

m = model.coef_.flatten().astype("float")
m = float(m[0])
c = model.intercept_.flatten().astype("float")
c = float(c[0])

def visualize(x_arr = year_arr, y_arr = unemployment_arr, coef = m, intercept = c):
    plt.title("Unemployment Rate and Prediction Trend in Indonesia")
    plt.plot(x_arr, y_arr, marker='x')
    plt.xlabel("Year")
    plt.ylabel("Unemployment rate")
    x1 = np.linspace(0, 10)
    y1 = intercept + coef * x1
    plt.plot(x1, y1)
    plt.show()

visualize()


