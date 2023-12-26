# Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)
        
messages_list = ['Python is fun', 'Python is easy to learn', 'Python is versatile']
show_messages(messages_list)