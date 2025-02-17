import csv
import matplotlib.pyplot as plt


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


def calculate_average_expenditure(expenditure_data_list):
    asean_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', 'Laos',
                       'Malaysia', 'Myanmar', 'Philippines', 'Singapore',
                       'Thailand', 'Vietnam']

    country_expenditure = {country: [] for country in asean_countries}

    for expenditure in expenditure_data_list:
        if expenditure.country in asean_countries:
            country_expenditure[expenditure.country].append(expenditure.value)

    average_expenditure = {country: (sum(values) / len(values) if values else 0) for country, values in
                           country_expenditure.items()}
    return average_expenditure


def visualize_average_expenditure(average_expenditure):
    countries = list(average_expenditure.keys())
    averages = list(average_expenditure.values())

    plt.figure(figsize=(12, 6))
    plt.bar(countries, averages, color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Average Expenditure on Computers')
    plt.title('Average Expenditure on Access to Computers by ASEAN Country', fontsize=16, fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

expenditure_data_list = read_expenditure_csv("Public expenditure.csv")
average_expenditure = calculate_average_expenditure(expenditure_data_list)
visualize_average_expenditure(average_expenditure)
