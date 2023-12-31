# Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a prize.
from random import choice

series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd',]

first_choice = choice(series)
second_choice = choice(series)
third_choice = choice(series)
fourth_choice = choice(series)

print(f"The person with lottery number {first_choice}{second_choice}{third_choice}{fourth_choice} wins a prize!")