#  Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def pizza_toppings(*toppings):
    print(f"Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
pizza_toppings('mushroom', 'pepperoni', 'pineapple')