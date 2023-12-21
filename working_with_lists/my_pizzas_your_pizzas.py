# Start with your program from Exercise 4-1 (page 56). 
pizzas = ['Pepperoni', 'Chicken', 'Mushroom']

# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
friends_pizza = pizzas[:]

# Add a new pizza to the original list.
pizzas.append('Pineapple')

# Add a different pizza to the list friend_pizzas.
friends_pizza.append('Neopolitan')

# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print("My favourite pizzas are:")
print(pizzas)

print("\nMy friends favourite pizzas are:")
print(friends_pizza)