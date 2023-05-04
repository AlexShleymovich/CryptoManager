import requests
from datetime import datetime

class CryptoAPI:
    def __init__(self):
        self.base_url = 'https://api.coingecko.com/api/v3/coins'
        self.tickers_list = []
        self.counter = 1

    def order_id_assignment(self):
        id = self.counter
        self.counter += 1
        return id

    def get_price_by_date(self, ticker, date_str):
        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Format the date to match the API's format
        formatted_date = date.strftime("%d-%m-%Y")

        # Make the API request
        response = requests.get(f"{self.base_url}/{ticker}/history?date={formatted_date}")
        data = response.json()
        # Get the price data for the given day
        price_data = data["market_data"]["current_price"]["usd"]
        rounded_price_data = round(price_data, 2)

        return rounded_price_data

    def get_tickers(self):
        # Declare the params to pull the top 100 coins with high maketcap
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
        }

        # Make the API request
        tickers = requests.get(f"{self.base_url}/markets", params=params).json()

        for ticker in tickers:
            self.tickers_list.append(ticker['id'])
        return self.tickers_list











