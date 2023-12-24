# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.

# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'variable':'This is like a container for storing a value',
    
    'boolean':'This is a True or False value',
    
    'integer':'It is a whole number without any decimal or fraction',
    
    'float':'This is a decimal number',
    
    'string':'This is a text value',
}

for k,v in glossary.items():
    print(f"{k}:\n{v}")