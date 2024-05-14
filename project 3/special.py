import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Set the backend explicitly
import matplotlib.pyplot as plt
import requests

# Function to fetch COVID-19 data from the Johns Hopkins University GitHub repository
def fetch_covid_data():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    response = requests.get(url)
    data = pd.read_csv(response.text)
    return data

# Function to process the fetched data and create a plot
def create_plot(data):
    # Extracting data for a specific country (e.g., United States)
    country_data = data[data['Country/Region'] == 'US']
    print(country_data.head())  # Print first few rows to verify if data is correct
    dates = country_data.columns[4:]  # Columns starting from the 5th column are dates
    cases = country_data.iloc[:, 4:].sum()  # Summing cases across all states for each date
    print(cases.head())  # Print first few entries to verify if data is correct

    # Converting dates to datetime objects for better plotting
    dates = pd.to_datetime(dates)

    # Creating the plot
    plt.plot(dates, cases, marker='o', linestyle='-')
    plt.title('COVID-19 Cases in the United States')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)

    # Save the plot as special.png
    plt.savefig('special.png')

    # Display the plot
    print("Plotting the graph...")
    plt.show()

def main():
    # Fetch COVID-19 data
    covid_data = fetch_covid_data()
    print(covid_data.head())  # Print first few rows of the entire dataset to verify if data is being fetched

    # Create and save the plot
    create_plot(covid_data)

if __name__ == "__main__":
    main()

