# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places = {
    'ileri': ['Russia', 'China', 'Maldives'],
    'kaycee': ['Maldives', 'Bora Bora', 'USA'],
    'muslimah': ['Dubai', 'Qatar', 'London'],
}

for k,v in favourite_places.items():
    print(f"\n{k.title()}'s favourite places are:")
    for place in v:
        print(place)