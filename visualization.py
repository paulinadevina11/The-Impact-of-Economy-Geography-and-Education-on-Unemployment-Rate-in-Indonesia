import matplotlib.pyplot as plt
import numpy as np

def visualize_unemployment_bar_all_years(unemployment_data_list):
    years = list(unemployment_data_list[0].years_data.keys())
    x = np.arange(len(years))
    width = 0.35

    urban_totals = []
    rural_totals = []

    for year in years:
        urban_total = sum(float(data.years_data[year]) for data in unemployment_data_list if "Urban" in data.area)
        rural_total = sum(float(data.years_data[year]) for data in unemployment_data_list if "Rural" in data.area)
        urban_totals.append(urban_total)
        rural_totals.append(rural_total)

    plt.figure(figsize=(12, 7))
    plt.bar(x - width/2, urban_totals, width, label='Urban', color='blue')
    plt.bar(x + width/2, rural_totals, width, label='Rural', color='green')
    plt.xlabel('Year')
    plt.ylabel('Unemployment Rate')
    plt.title('Urban vs Rural Unemployment Rate Over Years')
    plt.xticks(x, years)
    plt.legend()
    plt.tight_layout()
    plt.show()








