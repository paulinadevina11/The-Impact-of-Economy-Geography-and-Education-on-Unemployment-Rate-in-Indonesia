import pandas as pd

year_arr = [str(year) for year in range(2015, 2024)]

def matrix_collation():
    # Read the matrix of unemployment rate by urban-rural classification
    unemployment_urban_rural_df = pd.read_csv("Unemployment Rate by Urban-Rural Classification.csv", delimiter=";")
    unemployment_urban_rural_df = unemployment_urban_rural_df.transpose()
    urban_arr = unemployment_urban_rural_df["Urban"].tolist()
    rural_arr = unemployment_urban_rural_df["Rural"].tolist()

    dataframe_data = {
        'Year': year_arr,
        "Urban Unemployment": urban_arr,
        "Rural Unemployment": rural_arr
    }
    unemployment_urban_rural_df = pd.DataFrame(dataframe_data)

    # Read the matrix of GDP Growth INDONESIA
    GDP_growth_world_df = pd.read_csv("GDP GROWTH INDONESIA - WORLD BANK.csv", delimiter=",")
    GDP_growth_indonesia = GDP_growth_world_df[(GDP_growth_world_df["Country Name"] == "Indonesia")].drop(columns=['Unnamed: 68'])
    GDP_growth_indonesia_per_year = GDP_growth_indonesia.loc[:, [year for year in GDP_growth_indonesia.columns if year.isdigit() and int(year) >= 2015]]
    GDP_growth_indonesia_per_year = GDP_growth_indonesia_per_year.transpose()
    GDP_growth_arr = GDP_growth_indonesia_per_year.values.flatten().tolist()
    dataframe_data = {
        "Year": year_arr,
        "GDP Per Capita Growth": GDP_growth_arr
    }
    GDP_growth_indonesia_df = pd.DataFrame(dataframe_data)

    # Read education df
    education_df = pd.read_csv("BPS STATISTIK TINGKAT PENDIDIKAN.csv", delimiter=";")
    education_df.to_excel("BPS STATISTIK EDUCATION.xlsx")
    def read_education_df_per_category(filename, type):
        file_df = pd.read_csv(filename, delimiter=";")
        average_arr_per_year = []
        for year in year_arr:
            average_value = file_df[year].mean()
            average_arr_per_year.append(average_value)

        column_2 = f"Average Education Completion {type}"

        dataframe_data_dict = {
            'Year': year_arr,
            column_2: average_arr_per_year
        }

        return pd.DataFrame(dataframe_data_dict)


    SD_education_completion_dataframe = read_education_df_per_category("BPS STATISTIK EDUCATION - SD.csv", "SD")
    SMP_education_completion_dataframe = read_education_df_per_category("BPS STATISTIK EDUCATION - SMP.csv", "SMP")
    SMA_education_completion_dataframe = read_education_df_per_category("BPS STATISTIK EDUCATION - SMA.csv", "SMA")
    SD_to_SMP = pd.merge(SD_education_completion_dataframe, SMP_education_completion_dataframe, on=['Year'])
    SD_SMP_SMA_df = pd.merge(SD_to_SMP, SMA_education_completion_dataframe, on=['Year'])

    # Collate all dataframe into 1 dataframe
    urban_rural_to_GDP = pd.merge(unemployment_urban_rural_df, GDP_growth_indonesia_df, on=['Year'])
    main_df = pd.merge(urban_rural_to_GDP, SD_SMP_SMA_df, on=['Year'])

    return main_df

def find_indonesia_unemployment_rate():
    main_dataframe = pd.read_csv("unemployment analysis.csv", delimiter=",")

    indonesia_dataframe = main_dataframe[main_dataframe["Country Name"] == "Indonesia"]

    indonesia_main_df = indonesia_dataframe.loc[:, [year for year in indonesia_dataframe.columns if year.isdigit() and int(year) >= 2012]]

    with open("ASEAN unemployment rate.csv", "r+") as unemployment_file:
        # Skip the first two lines
        next(unemployment_file)
        next(unemployment_file)

        # Initialize the main dataframe
        main_dataframe = pd.read_csv(unemployment_file, delimiter=";")
        main_dataframe = main_dataframe.drop(columns=['Unnamed: 5'])

    indonesia_dataframe = main_dataframe[(main_dataframe['Region'] == "Indonesia") & (main_dataframe['Year'] == 2023)]
    indonesia_unemployment_df = indonesia_dataframe[indonesia_dataframe["Series"].str.contains('Unemployment rate')]

    average_per_year = indonesia_unemployment_df.groupby('Year')['Value'].mean().astype("str")

    indonesia_main_df[2023] = round(float(average_per_year[2023]),2)

    year_arr = list(indonesia_main_df.keys().astype("str"))

    unemployment_values_arr = indonesia_main_df.values.flatten().tolist()

    df = pd.DataFrame(unemployment_values_arr, index=year_arr)

    df = df.reset_index()

    df.columns = ['Year', 'Unemployment Rate']

    return df