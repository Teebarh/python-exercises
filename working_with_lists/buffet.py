# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

menu = ('Fried Rice', 'Jollof Rice', 'Yam and Egg Sauce', 'Fried Yam', 'Amala')

# Use a for loop to print each food the restaurant offers.
for food in menu:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
menu[0] = 'Coconut Rice'

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
menu = ('Coconut Rice', 'Jollof Rice', 'Yam and Egg Sauce', 'Fried Yam', 'Semo')
for food in menu:
    print(food)