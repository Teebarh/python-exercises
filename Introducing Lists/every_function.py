# Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

countries = ['Norway', 'Nigeria', 'Senegal', 'Egypt', 'Pakistan', 'India', 'Canada', 'Brazil']

# Accessing elements in a list
print(countries[4])

# Using individual values
print(f"{countries[0]} is such a beautiful country.")

# Modifying elemnts
countries[1] = 'Netherlands'
print[countries]

# Appending elemnts to a list
countries.append('Ghana')
print(countries)

#inserting elements into a list
countries.insert(0, 'Portugal')
print(countries)

# Popping elements from a list
popped_countries = countries.pop()
print(popped_countries)

# deleting elements from a list
del countries[3]
print(countries)

#removing elements from a list
removed_countries = countries.remove('Brazil')
print(countries)

# organizing a list with sort() method
countries.sort()
print(countries)

# organizing a list with the sorted() function
print(sorted(countries))

# organizing a list with the reverse() method
countries.reverse()
print(countries)

# finding the length of a list
print(len(countries))

