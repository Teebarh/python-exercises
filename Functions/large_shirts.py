# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Function one
def make_shirt(message, size='Large'):
    """This is to print a large T-shirt with a custom message"""
    print(f"I want the T-shirt in a size {size} with this message printed on it:\n{message.title()}")
    
make_shirt('I love Python!')

# Function two
def make_shirt(size, message='I love Python'):
    """This is to print a any sized T-shirt with a default 'I love Python' message"""
    print(f"I want the T-shirt in a size {size} with this message printed on it:\n{message.title()}")

make_shirt('medium')
make_shirt('large')

# Function three
def make_shirt(size, message):
    """This is to print a any sized T-shirt with a custom message"""
    print(f"I want the T-shirt in a size {size} with this message printed on it:\n{message.title()}")
    
make_shirt('small', 'Python is very versatile')
make_shirt('medium', 'keep calm, I code in Python')