# Wrap your code from Exercise 10-6 in a while loop 
# so the user can continue entering numbers even if they make a mistake and 
# enter text instead of a number.

while True: 
    print("Type 'q' at any time to quit")
    
    first_input = input("Input a number: ")
    if first_input == 'q':
        break
    
    second_input = input("Input another number: ")
    if second_input == 'q':
        break
    
    try:
        total = int(first_input) + int(second_input)
        print(total)
        
    except ValueError:
        print("Please input a valid number.")
        