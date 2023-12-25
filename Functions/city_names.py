# : Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    full_name = f"{city.title()}, {country.title()}"
    return full_name

city_country('London', 'England')
city_country('Lagos', 'Nigeria')
city_country('New York', 'America')