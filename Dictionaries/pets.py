# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pets = {
    '1': {
        'Owner': 'ileri',
        'Pet': 'Dog', 
    },
    
    '2': {
        'Owner': 'kaycee',
        'Pet': 'Cat',
    },
    
    '3': {
        'Owner': 'Muslimah',
        'Pet': 'Cat',
    }
}

for key, value in pets.items():
    print(f"\n Pet Owners: {key}")
    owner = value['Owner']
    pet = value['Pet']
    
    print(f"\t{owner.title()} owns a {pet}")
