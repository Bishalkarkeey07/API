from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class URL:
    def __init__(self, url):
        self.url = url


class CMCReq:
    def __init__(self, api_key):
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }


class CoinMarketAPI:
    def __init__(self, url, parameters, tokens):
        self.url = url.url
        self.parameters = parameters
        self.tokens = tokens.headers
        self.session = Session()
        self.session.headers.update(self.tokens)

    def get_data(self):
        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print("Error")
            print(e)


url = URL('https://pro-api.coinmarketcap.com/v1/tools/postman')
tokens = CMCReq('2aa13a4a-a3c5-42b2-8209-1f989957763e')

parameters = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
}

api = CoinMarketAPI(url, parameters, tokens)
data = api.get_data()

print("Success")
print(data)
