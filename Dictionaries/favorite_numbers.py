# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'Ileri': [5, 6, 7],
    'Kaycee': [9, 10, 11],
    'Muslimah': [12, 13, 14],
    'Rahmah': [15, 16, 17],
    'Fawziyyat': [18, 19, 20],
}

for key, value in favorite_numbers.items():
    print(f"\n{key}'s favorite numbers are:")
    for number in value:
        print(number)