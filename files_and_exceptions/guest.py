# Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

prompt = input("What is your first name? ")

filename = 'guest.txt'

with open(filename, 'w') as file:
    file.write(prompt)