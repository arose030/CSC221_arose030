import requests
import matplotlib.pyplot as plt

# Function to fetch stock price data from Alpha Vantage API
def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to process the fetched data and create a plot
def create_plot(data):
    # Extracting daily closing prices
    dates = list(data['Time Series (Daily)'].keys())
    dates.reverse()  # Reverse the order to plot from oldest to newest
    closing_prices = [float(data['Time Series (Daily)'][date]['4. close']) for date in dates]

    # Creating the plot
    plt.plot(dates, closing_prices, marker='o', linestyle='-')
    plt.title('Historical Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.grid(True)

    # Save the plot as special.png
    plt.savefig('special.png')

    # Display the plot
    plt.show()

def main():
    symbol = 'AAPL'  # Example stock symbol (Apple Inc.)
    api_key = 'ZT6JERTCSGKHC29E'  # Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
    data = fetch_stock_data(symbol, api_key)
    create_plot(data)

if __name__ == "__main__":
    main()
