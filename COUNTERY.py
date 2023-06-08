import requests
import json
API_KEY = "627bf10f18a31a51e83f81ac131d401e"
capital = "Kathmandu"  
def get_country_by_capital():
    API_URL = f"https://api.countrylayer.com/v2/capital/{capital}?access_key={API_KEY}"

    response = requests.get(API_URL)

    if response.status_code == 200:
        country_data = json.loads(response.text)
        return country_data
    else:
        print("Error retrieving country data.")
        return None

country_data = get_country_by_capital()

if country_data:
    print(country_data)
else:
    print("No country data available.")


    # print(country_data)
    # print("Name:", country_data["name"])
    # print("Top Level Domain:", country_data["topLevelDomain"])
    # print("Alpha-2 Code:", country_data["alpha2Code"])
    # print("Alpha-3 Code:", country_data["alpha3Code"])
    # print("Calling Codes:", country_data["callingCodes"])