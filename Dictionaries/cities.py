# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'New York': {
        'Country': 'USA',
        'Population': 8_800_000,
        'Fact': 'More than 800 languages are spoken throughout the city.'
    },
    
    'London': {
        'Country': 'England',
        'Population': 8_800_000,
        'Fact': 'London is the smallest city in England.'
    },
    
    'Tokyo': {
        'Country': 'Japan',
        'Population': 14_000_000,
        'Fact': 'Shinjuku is the capital of Tokyo.'
    },
}

for key, value in cities.items():
    print(f"\nCity Profile: {key}")
    country = value['Country']
    population = value['Population']
    fact = value['Fact']
    
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")