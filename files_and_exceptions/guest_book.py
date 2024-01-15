#  Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

while True:
    prompt = input("What is your first name? (Type 'q' to quit) ")
    
    if prompt == 'q':
        break
    
    print(f"Hello {prompt}!")
    
    filename = 'guest_book.txt'
    
    with open(filename, 'a') as file:
        file.write(f"{prompt}\n")
    