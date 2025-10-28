#1  # Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data.countries import countries   
countries_with_land = [country for country in countries if 'land' in country.lower()]
for c in countries_with_land:
    print("-", c)
print("Total countries with 'land':", len(countries_with_land))

#2  # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for item in fruits:
    reversed_fruits = [item] + reversed_fruits
print("Original fruits:", fruits)
print("Reversed fruits:", reversed_fruits)

