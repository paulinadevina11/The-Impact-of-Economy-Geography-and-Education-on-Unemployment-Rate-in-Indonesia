import csv
from visualization import visualize_unemployment_bar_all_years
class UnemploymentData:
    def __init__(self, area, years_data):
        self.area = area
        self.years_data = years_data

    def display_data(self):
        print(f"Unemployment Rate for {self.area}:")
        for year, value in self.years_data.items():
            print(f"{year}: {value}%")
        print("-" * 40)

def read_unemployment_file(file_path):
    unemployment_data_list = []

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        next(reader)
        header = next(reader)[1:]

        for row in reader:
            if row[0]:
                area = row[0]
                years_data = {year: row[i+1].replace(",", ".") for i, year in enumerate(header)}
                unemployment_data = UnemploymentData(area, years_data)
                unemployment_data_list.append(unemployment_data)

    return unemployment_data_list

file_path = "Unemployment Rate by Urban-Rural Classification.csv"
unemployment_data_list = read_unemployment_file(file_path)
for unemployment_data in unemployment_data_list:
    unemployment_data.display_data()
visualize_unemployment_bar_all_years(unemployment_data_list)
