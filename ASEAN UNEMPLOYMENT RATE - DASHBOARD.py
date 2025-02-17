import csv
from visualization import visualize_average_unemployment

asean_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia',
                   'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam']

class LabourForceData:
    def __init__(self, country, year, series, value):
        self.country = country
        self.year = year
        self.series = series
        self.value = float(value)  # Convert to float for calculations

    def display(self):
        print(f"Country: {self.country}, Year: {self.year}, Series: {self.series}, Value: {self.value}")
        print("-" * 40)

class AseanLabourForce:
    def __init__(self, file_path):
        self.file_path = file_path
        self.asean_data = []

    def read_and_filter_data(self):
        with open(self.file_path, 'r') as csvfile:
            reader = csvfile.readlines()
            for row in reader[1:]:  # Skip header row if present
                row_split = row.split(';')
                country = row_split[1]
                year = row_split[2]
                series = row_split[3]
                value = row_split[4].strip()  # Remove whitespace
                if country in asean_countries and year >= "2012" and "unemployment rate" in series.lower():
                    data = LabourForceData(country, year, series, value)
                    data.display()
                    self.asean_data.append(data)

    def calculate_average_unemployment_rate(self):
        country_data = {country: [] for country in asean_countries}

        for data in self.asean_data:
            country_data[data.country].append(data.value)

        average_unemployment = {country: (sum(values) / len(values) if values else 0) for country, values in country_data.items()}
        return average_unemployment

# Example usage
file_path = "ASEAN unemployment rate.csv"

asean_labour_force = AseanLabourForce(file_path)
asean_labour_force.read_and_filter_data()
average_unemployment = asean_labour_force.calculate_average_unemployment_rate()
visualize_average_unemployment(average_unemployment)
