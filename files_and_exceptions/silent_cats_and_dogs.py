# Modify your except block in Exercise 10-8 to fail 
# silently if either file is missing.

try: 
    with open('cat.txt') as c:
        cat_contents = c.read()

    
    with open('dog.txt') as d:
        dog_contents = d.read()


except FileNotFoundError:
    pass
    
else: 
    print(cat_contents)
    print("\n")
    print(dog_contents)