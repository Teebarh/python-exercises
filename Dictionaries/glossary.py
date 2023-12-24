#  A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'variable':'This is like a container for storing a value',
    
    'boolean':'This is a True or False value',
    
    'integer':'It is a whole number without any decimal or fraction',
    
    'float':'This is a decimal number',
    
    'string':'This is a text value',
}

print(f"Variable:\n{glossary['variable']}")
print(f"Boolean:\n{glossary['boolean']}")
print(f"Integer:\n{glossary['integer']}")
print(f"Float:\n{glossary['float']}")
print(f"String:\n{glossary['string']}")