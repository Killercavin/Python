import unittest
from city_functions import cityCountry # Importing this module cityCountry from city_functions.py

def test_city_country(city, country):
    print(f"My city is {city.title()} and country is {country.title()}.")
test_city_country('santiago', 'chile')


