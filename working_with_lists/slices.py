#Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

animals = ['Lion', 'Tiger', 'Leopard', 'Puma', 'Fox', 'Hyena', 'Jackal', 'Wolf', 'Lynx']

#Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
print("The first three animals are:")
for animal in animals[:3]:
    print(animal)

# Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print("Three animals from the middle of the list are:")
for animal in animals[3:6]:
    print(animal)

# Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

print("The last three animals are:")
for animal in animals[6:]:
    print(animal)
