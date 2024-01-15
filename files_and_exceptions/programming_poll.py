#  Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

while True:
    prompt = input("Why do you like programming? (Type 'q' to quit) ")
    
    if prompt == 'q':
        break
    
    filename = 'programming_poll.txt'
    
    with open(filename, 'a') as file:
        file.write(f"{prompt}\n")