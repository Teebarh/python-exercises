#  Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(original_messages, moved_messages):
    while original_messages:
        current_message = original_messages.pop()
        print(f"Printing message: {current_message}")
        moved_messages.append(current_message)
        
original_messages = ['Python is fun', 'Python is easy to learn', 'Python is versatile']
moved_messages = []

print(f"The following messages have been printed:")
for message in moved_messages:
    print(message)
        
show_messages(original_messages, moved_messages)
print(original_messages, moved_messages)