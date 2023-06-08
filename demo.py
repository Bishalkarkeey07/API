
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#url = 'https://pro-api.coinmarketcap.com/v1/blockchain/statistics/latest'# 403 Forbidden
#url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/historical'
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# url =  'https://pro-api.coinmarketcap.com/v1/tools/postman'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2aa13a4a-a3c5-42b2-8209-1f989957763e',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)  #for getoperatrions
  data = json.loads(response.text)
  print("sucess")
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print("Error")
  print(e)

#for post operations
# payload = {
#     'timestamp': '2023-06-07T08:03:58.954Z',
#     'symbol': 't7tb1slvwv'
# }

# try:
#     response = session.post(url, data=json.dumps(payload), headers=headers)
#     data = json.loads(response.text)
#     print("Success")
#     print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#     print("Error")
#     print(e)