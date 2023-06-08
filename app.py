import requests
import json
import threading
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

class CoinMarketAPI:
    def __init__(self, url, parameters, headers):
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.data = None

    def fetch_data(self):
        try:
            response = self.session.get(self.url, params=self.parameters)
            self.data = json.loads(response.text)
        except (requests.ConnectionError, requests.Timeout, requests.TooManyRedirects) as e:
            print("Error")
            print(e)

# Define the API details
url = 'https://pro-api.coinmarketcap.com/v1/tools/postman'
parameters = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'token': '2aa13a4a-a3c5-42b2-8209-1f989957763e',
}

# Create an instance of the CoinMarketAPI class
coin_market_api = CoinMarketAPI(url, parameters, headers)

# Create a lock object for thread synchronization
lock = threading.Lock()

# Define a thread function for fetching data
def fetch_data_thread():
    with lock:
        coin_market_api.fetch_data()

# Create and start the thread
thread = threading.Thread(target=fetch_data_thread)
thread.start()

# Perform other tasks while the data is being fetched
print("Performing other tasks...")

thread.join()

data = coin_market_api.data

# Print the data
if data:
    print("Success")
    print(data)
