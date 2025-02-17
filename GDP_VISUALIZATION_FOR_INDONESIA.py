import pandas as pd
import matplotlib.pyplot as plt

year_arr = [str(year) for year in range(2015, 2024)]
GDP_growth_world_df = pd.read_csv("GDP GROWTH INDONESIA - WORLD BANK.csv", delimiter=",")
GDP_growth_indonesia = GDP_growth_world_df[(GDP_growth_world_df["Country Name"] == "Indonesia")].drop(columns=['Unnamed: 68'])
GDP_growth_indonesia_per_year = GDP_growth_indonesia.loc[:, [year for year in GDP_growth_indonesia.columns if year.isdigit() and int(year) >= 2015]]
GDP_growth_indonesia_per_year = GDP_growth_indonesia_per_year.transpose()
GDP_growth_arr = GDP_growth_indonesia_per_year.values.flatten().tolist()

plt.plot(year_arr, GDP_growth_arr, color="green", label="GDP Growth")
plt.title("Visualization of GDP per capita growth for Indonesia", fontweight="bold", fontsize=16)
plt.xlabel("Year", fontsize=13, fontweight='bold')
plt.ylabel("GDP growth", fontweight="bold", fontsize=13)
plt.legend()
plt.show()





