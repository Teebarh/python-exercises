# One common problem when prompting for numerical input 
# occurs when people provide text instead of numbers. When you try to convert 
# the input to an int, you’ll get a ValueError. 

# Write a program that prompts for 
# two numbers. Add them together and print the result. Catch the ValueError if 
# either input value is not a number, and print a friendly error message. Test your 
# program by entering two numbers and then by entering some text instead of a 
# number.

first_input = input("Input a number: ")
second_input = input("Input another number: ")

try:
    total = int(first_input) + int(second_input)
except ValueError:
    print("Please input a valid number.")
else:
    print(total)