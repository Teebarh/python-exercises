# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"I want the T-shirt in a size {size.title()} with this message printed on it:\n{message.title()}")
    
make_shirt('medium', 'I love Python!')
make_shirt(size='medium', message='I love Python')
    