# Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

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
        
show_messages(original_messages[:], moved_messages)
print(original_messages, moved_messages)