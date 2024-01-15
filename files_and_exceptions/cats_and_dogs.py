# Make two files, cats.txt and dogs.txt. Store at least three 
# names of cats in the first file and three names of dogs in the second file. Write 
# a program that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block 
# executes properly.
try: 
    with open('cat.txt') as c:
        cat_contents = c.read()

    
    with open('dog.txt') as d:
        dog_contents = d.read()


except FileNotFoundError:
    print("Oh no, the file is missing.")
    
else: 
    print(cat_contents)
    print("\n")
    print(dog_contents)