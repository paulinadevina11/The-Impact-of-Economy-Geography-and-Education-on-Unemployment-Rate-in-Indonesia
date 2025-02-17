import matplotlib.pyplot as plt
import pandas as pd

def first_analysis():
    with open("unemployment analysis.csv") as unemployment_file:
        main_dataframe = pd.read_csv(unemployment_file, delimiter=",")

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
    print(year_arr)

    unemployment_values_arr = indonesia_main_df.values.flatten().tolist()
    print(unemployment_values_arr)

    df = pd.DataFrame(unemployment_values_arr, index=year_arr)

    df = df.reset_index()

    df.columns = ['Year', 'Unemployment Rate']

    return year_arr, unemployment_values_arr, df

year_arr, unemployement_arr, main_df = first_analysis()
print(main_df)


# new_unemployement_df = pd.merge(indonesia_main_df, average_per_year.transpose())