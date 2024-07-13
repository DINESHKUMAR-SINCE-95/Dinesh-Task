import requests

# Task 1: Fetching data from restcountries API

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to fetch data from the URL")

    def display_country_currency(self):
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                for currency, details in currencies.items():
                    currency_name = details.get('name', 'N/A')
                    currency_symbol = details.get('symbol', 'N/A')
                    print(f"Country: {name}, Currency: {currency_name}, Symbol: {currency_symbol}")

    def countries_with_currency(self, currency_name):
        if self.data:
            countries = [country.get('name', {}).get('common', 'N/A') for country in self.data if currency_name in country.get('currencies', {})]
            print(f"Countries with {currency_name} as currency: {', '.join(countries)}")


# Usage example:
restcountries_url = 'https://restcountries.com/v3.1/all'
country_data = CountryData(restcountries_url)
country_data.fetch_data()
country_data.display_country_currency()
country_data.countries_with_currency('USD')  # For Dollar
country_data.countries_with_currency('EUR')  # For Euro


# Task 2: Fetching data from openbrewerydb API

class BreweryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to fetch data from the URL")

    def list_breweries_in_states(self, states):
        if self.data:
            for state in states:
                print(f"Breweries in {state}:")
                breweries = [brewery['name'] for brewery in self.data if brewery['state'] == state]
                for brewery in breweries:
                    print(brewery)

    def count_breweries_in_states(self, states):
        if self.data:
            for state in states:
                count = len([brewery for brewery in self.data if brewery['state'] == state])
                print(f"Number of breweries in {state}: {count}")

    def count_brewery_types_in_cities(self, states):
        if self.data:
            for state in states:
                cities = set([brewery['city'] for brewery in self.data if brewery['state'] == state])
                for city in cities:
                    types = {}
                    for brewery in self.data:
                        if brewery['city'] == city and brewery['state'] == state:
                            brewery_type = brewery['brewery_type']
                            if brewery_type in types:
                                types[brewery_type] += 1
                            else:
                                types[brewery_type] = 1
                    print(f"Brewery types in {city}, {state}: {types}")

    def count_breweries_with_websites(self, states):
        if self.data:
            for state in states:
                count = len([brewery for brewery in self.data if brewery['state'] == state and brewery['website_url']])
                print(f"Number of breweries with websites in {state}: {count}")


# Usage example:
openbrewerydb_url = 'https://api.openbrewerydb.org/breweries'
brewery_data = BreweryData(openbrewerydb_url)
brewery_data.fetch_data()
brewery_data.list_breweries_in_states(['Alaska', 'Maine', 'New York'])
brewery_data.count_breweries_in_states(['Alaska', 'Maine', 'New York'])
brewery_data.count_brewery_types_in_cities(['Alaska', 'Maine', 'New York'])
brewery_data.count_breweries_with_websites(['Alaska', 'Maine', 'New York'])
