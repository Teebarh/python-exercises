# Write a program that prompts for the user’s favorite 
# number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite 
# number! It’s _____.”

import json

prompt = input("What is your favorite number?")

filename = 'prompt.json'
with open(filename, 'w') as p:
    json.dump(prompt, p)


filename = 'prompt.json'    
with open(filename) as p:
    response = json.load(p)
    
print("I know your favourite number, it's" + " " + response + "!")

