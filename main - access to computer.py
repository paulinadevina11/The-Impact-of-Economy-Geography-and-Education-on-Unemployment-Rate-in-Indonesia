import csv
from visualization import visualize_pie_chart

class EducationExpenditure:
    def __init__(self, country, year, series, value):
        self.country = country
        self.year = int(year)
        self.series = series
        self.value = float(value)

    def display_data(self):
        print(f"Country: {self.country}, Year: {self.year}")
        print(f"Series: {self.series}")
        print(f"Value: {self.value}")
        print("-" * 40)

def read_expenditure_csv(file_path):
    expenditure_data_list = []

    with open(file_path) as csvfile:
        reader = csvfile.readlines()

        for row in reader:
            data_split = row.split(";")
            country = data_split[1]
            year = data_split[2]
            series = data_split[3]
            value = data_split[4].strip()
            if year >= "2012" and "Basic access to computers by level of education" in series:
                expenditure = EducationExpenditure(country, year, series, value)
                expenditure_data_list.append(expenditure)

    return expenditure_data_list

def display_asean_expenditure(expenditure_data_list):
    asean_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar',
                       'Philippines', 'Singapore', 'Thailand', 'Vietnam']

    print("Displaying education expenditure data for ASEAN countries:\n")

    for expenditure in expenditure_data_list:
        if expenditure.country in asean_countries:
            expenditure.display_data()

def extract_country_data(expenditure_data_list, country_name):
    return [expenditure for expenditure in expenditure_data_list if expenditure.country == country_name]

def aggregate_expenditure_by_series(country_data):
    series_dict = {}

    for exp in country_data:
        if exp.series in series_dict:
            series_dict[exp.series] += exp.value
        else:
            series_dict[exp.series] = exp.value

    return series_dict

expenditure_data_list = read_expenditure_csv("Public expenditure.csv")
display_asean_expenditure(expenditure_data_list)

#Visualize for Brunei
brunei_data = extract_country_data(expenditure_data_list, "Brunei Darussalam")
brunei_series_data = aggregate_expenditure_by_series(brunei_data)
visualize_pie_chart(brunei_series_data, "Brunei Darussalam")

# Visualize for Cambodia
cambodia_data = extract_country_data(expenditure_data_list, "Cambodia")
cambodia_series_data = aggregate_expenditure_by_series(cambodia_data)
visualize_pie_chart(cambodia_series_data, "Cambodia")

# Visualize for Indonesia
indonesia_data = extract_country_data(expenditure_data_list, "Indonesia")
indonesia_series_data = aggregate_expenditure_by_series(indonesia_data)
visualize_pie_chart(indonesia_series_data, "Indonesia")

#Visualize for Malaysia
malaysia_data = extract_country_data(expenditure_data_list, "Malaysia")
malaysia_series_data = aggregate_expenditure_by_series(malaysia_data)
visualize_pie_chart(malaysia_series_data, "Malaysia")

#Visualize for Myanmar
myanmar_data = extract_country_data(expenditure_data_list, "Myanmar")
myanmar_series_data = aggregate_expenditure_by_series(myanmar_data)
visualize_pie_chart(myanmar_series_data, "Myanmar")

#Visualize for Philippines
philippines_data = extract_country_data(expenditure_data_list, "Philippines")
philippines_series_data = aggregate_expenditure_by_series(philippines_data)
visualize_pie_chart(philippines_series_data, "Philippines")

#Visualize for Singapore
singapore_data = extract_country_data(expenditure_data_list, "Singapore")
singapore_series_data = aggregate_expenditure_by_series(singapore_data)
visualize_pie_chart(singapore_series_data, "Singapore")



